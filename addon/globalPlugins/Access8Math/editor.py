import os
import re
import shutil
import wx

import addonHandler
import gui
import wx

from lib.viewHTML import Access8MathDocument

addonHandler.initTranslation()

PATH = os.path.dirname(__file__)

wildcard = \
"Text (*.txt)|*.txt|"\
"archive (*.zip)|*.zip|"\
"All (*.*)|*.*"


class EditorFrame(wx.Frame):
	def __init__(self, path=None):
		style = wx.DEFAULT_FRAME_STYLE
		super(EditorFrame, self).__init__(wx.GetApp().TopWindow, size=(400, 300), style=style)

		if not path:
			self.ad = Access8MathDocument()
		else:
			self.ad = Access8MathDocument(path)

		self.filename = os.path.basename(self.ad.raw_entry)
		self.dirname = self.ad.raw_folder

		self.modify = False

		# Simplified init method.
		self.CreateInteriorWindowComponents()
		self.CreateExteriorWindowComponents()
		self.CenterOnScreen()

		with open(os.path.join(self.dirname, self.filename), 'r', encoding='utf-8') as file:
			self.control.SetValue(file.read())
		self.modify = False

		Hotkey(self)

		self.findReplaceData = wx.FindReplaceData()
		self.pos = 0
		self.Bind(wx.EVT_FIND, self.OnFindAction)
		self.Bind(wx.EVT_FIND_NEXT, self.OnFindNextAction)
		self.Bind(wx.EVT_FIND_REPLACE, self.OnReplaceAction)
		self.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnReplaceAllAction)

		self.Bind(wx.EVT_CLOSE, lambda event: self.OnExit(event))

	def SetTitle(self):
		# Translators: The title of the Editor window
		super(EditorFrame, self).SetTitle(_("%s - Access8Math Editor") % self.filename)

	def CreateInteriorWindowComponents(self):
		self.control = wx.TextCtrl(self, -1, value="", style=wx.TE_MULTILINE)
		self.control.Bind(wx.EVT_TEXT, self.OnTextChanged)
		# self.font = wx.Font()
		# self.control.SetFont(self.font)
		# self.colour = wx.Colour()
		# self.control.SetForegroundColour(self.colour)

	def CreateExteriorWindowComponents(self):
		self.SetTitle()

		self.CreateMenu()
		self.CreateStatusBar()
		self.BindEvents()

	def CreateMenu(self):
		menuBar = wx.MenuBar()

		fileMenu = wx.Menu()

		for id, label, helpText, handler in [
			(
				wx.ID_NEW,
				# Translators: A menu item in the Editor window
				_("&New"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Open a new editor."),
				self.OnNew
			),
			(
				wx.ID_OPEN,
				# Translators: A menu item in the Editor window
				_("&Open..."),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Open a new file."),
				self.OnOpen
			),
			(
				wx.ID_SAVE,
				# Translators: A menu item in the Editor window
				_("&Save"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Save the current file."),
				self.OnSave
			),
			(
				wx.ID_SAVEAS,
				# Translators: A menu item in the Editor window
				_("Save &as..."),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Save the file under a different name."),
				self.OnSaveAs
			),
			(
				wx.ID_EXIT,
				# Translators: A menu item in the Editor window
				_("E&xit"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Terminate the program."),
				self.OnExit
			)
		]:
			if id is None:
				fileMenu.AppendSeparator()
			else:
				item = fileMenu.Append(id, label, helpText)

				# Bind some events to an events handler.
				self.Bind(wx.EVT_MENU, handler, item)

		# Add the fileMenu to the menuBar.
		# Translators: A menu item in the Editor window
		menuBar.Append(fileMenu, _("&File"))

		viewMenu = wx.Menu()

		for id, label, helpText, handler in [
			(
				wx.ID_ANY,
				# Translators: A menu item in the Editor window
				_("Preview"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Preview HTML file"),
				self.OnPreview
			),
			(
				wx.ID_ANY,
				# Translators: A menu item in the Editor window
				_("Export..."),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Export archive file"),
				self.OnExport
			),
		]:
			if id is None:
				viewMenu.AppendSeparator()
			else:
				item = viewMenu.Append(id, label, helpText)

				# Bind some events to an events handler.
				self.Bind(wx.EVT_MENU, handler, item)

		# Add the fileMenu to the menuBar.
		# Translators: A menu item in the Editor window
		menuBar.Append(viewMenu, _("&View"))

		otherMenu = wx.Menu()

		for id, label, helpText, handler in [
			(
				wx.ID_ANY,
				# Translators: A menu item in the Editor window
				_("Font"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Adjust font format"),
				self.OnFont
			),
			(
				wx.ID_ANY,
				# Translators: A menu item in the Editor window
				_("Find"),
				# Translators: The help description text shown in the status bar in the Editor window when a menu item is selected
				_("Find and replace"),
				self.OnFindReplace
			),
		]:
			if id is None:
				otherMenu.AppendSeparator()
			else:
				item = otherMenu.Append(id, label, helpText)

				# Bind some events to an events handler.
				self.Bind(wx.EVT_MENU, handler, item)

		# Add the fileMenu to the menuBar.
		# Translators: A menu item in the Editor window
		menuBar.Append(otherMenu, _("&Other"))

		# Add the menuBar to the frame.
		self.SetMenuBar(menuBar)

	def BindEvents(self):
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

	def DefaultFileDialogOptions(self):
		return dict(
			defaultFile=self.filename,
			defaultDir=self.dirname,
			wildcard=wildcard,
		)

	def AskUserForFilename(self, **dialogOptions):
		with wx.FileDialog(self, **dialogOptions) as dialog:
			if dialog.ShowModal() == wx.ID_OK:
				userProvidedFilename = True

				if self.ad.raw_entry != os.path.dirname(dialog.GetPath()):
					self.ad.raw_folder = os.path.dirname(dialog.GetPath())
					self.ad.raw_entry = dialog.GetPath()
				else:
					self.ad.raw_entry = dialog.GetPath()

				self.filename = os.path.basename(self.ad.raw_entry)
				self.dirname = self.ad.raw_folder

				# Update the window title with the new filename.
				self.SetTitle()
			else:
				userProvidedFilename = False
		# dialog.Destroy()
		return userProvidedFilename

	def OnNew(self, event):
		frame = self.__class__()
		frame.Show(True)

	def OnOpen(self, event):
		# Translators: The title of the Editor's Open file window
		if self.AskUserForFilename(message=_("Open file"), style=wx.FD_OPEN, **self.DefaultFileDialogOptions()):
			with open(os.path.join(self.dirname, self.filename), 'r', encoding='utf-8') as file:
				self.control.SetValue(file.read())
			self.modify = False

	def OnSave(self, event):
		# Translators: The name of the document in the Editor when it has never been saved to a file
		if self.ad.temp:
			# Translators: The title of the Editor's Save file window
			if self.AskUserForFilename(message=_("Save file"), style=wx.FD_SAVE, **self.DefaultFileDialogOptions()):
				with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
					file.write(self.control.GetValue())
				self.modify = False
				return True
			else:
				return False
		else:
			with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
				file.write(self.control.GetValue())
			self.modify = False
			return True

	def OnSaveAs(self, event):
		# Translators: The title of the Editor's Save as file window
		if self.AskUserForFilename(message=_("Save file"), style=wx.FD_SAVE, **self.DefaultFileDialogOptions()):
			with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
				file.write(self.control.GetValue())
			self.modify = False

	def OnExit(self, event):
		if self.modify:
			# Translators: The name of the document in the Editor when it has never been saved to a file
			if self.ad.temp:
				path = ' "' + self.filename + '"'
			else:
				path = ' "' + os.path.join(self.dirname, self.filename) + '"'
			val = gui.messageBox(
				# Translators: The message displayed
				_("Save file{path}?").format(path=path),
				# Translators: The title of the dialog
				_("Save"),
				wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION, self
			)
			if val == wx.YES:
				result = self.OnSave(event)
				if result:
					self.Destroy()
			elif val == wx.NO:
				self.Destroy()
		else:
			self.Destroy()

	def OnPreview(self, event):
		save_result = False
		if self.modify:
			val = gui.messageBox(
				# Translators: The message displayed
				_("Preview will only include the saved content. The content in the editor has been modified since the last save, do you want to save and preview it?"),
				# Translators: The title of the dialog
				_("Preview"),
				wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION, self
			)
			if val == wx.YES:
				with open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8') as file:
					file.write(self.control.GetValue())
				self.modify = False
				save_result = True
			elif val == wx.NO:
				save_result = True
			elif val == wx.CANCEL:
				return
		else:
			save_result = True

		if not save_result:
			return

		self.ad.raw2review()
		os.startfile(os.path.join(self.ad.review_entry))

	def OnExport(self, event):
		save_result = False
		# Translators: The name of the document in the Editor when it has never been saved to a file
		if self.ad.temp:
			save_result = self.OnSave(event)
		else:
			if self.modify:
				val = gui.messageBox(
					# Translators: The message displayed
					_("Export will only include the saved content. The content in the editor has been modified since the last save, do you want to save and export it?"),
					# Translators: The title of the dialog
					_("Export"),
					wx.YES_NO | wx.YES_DEFAULT | wx.CANCEL | wx.ICON_QUESTION, self
				)
				if val == wx.YES:
					save_result = self.OnSave(event)
				elif val == wx.NO:
					save_result = True
				elif val == wx.CANCEL:
					return
			else:
				save_result = True

		if not save_result:
			return

		self.ad.raw2review()
		with wx.FileDialog(
			# Translators: The title of the Editor's Export file window
			self, message=_("Export file..."),
			defaultDir=self.dirname, wildcard="zip files (*.zip)|*.zip"
		) as entryDialog:
			if entryDialog.ShowModal() != wx.ID_OK:
				return
			dst = entryDialog.GetPath()
		dst = dst[:-4]
		shutil.make_archive(dst, 'zip', self.ad.review_folder)

	def OnFont(self, event):
		data = wx.FontData()
		data.SetInitialFont(self.control.GetFont())
		data.SetColour(self.control.GetForegroundColour())
		with wx.FontDialog(self, data) as dialog:
			if dialog.ShowModal() == wx.ID_OK:
				font_data = dialog.GetFontData()
				# self.font = font_data.GetChosenFont()
				self.control.SetFont(font_data.GetChosenFont())
				# self.colour = font_data.GetColour()
				self.control.SetForegroundColour(font_data.GetColour())

	def OnFindReplace(self, event):
		wx.FindReplaceDialog(self, self.findReplaceData, style=wx.FR_REPLACEDIALOG).Show()

	def OnFindAction(self, event):
		fstring = self.findReplaceData.GetFindString()
		self.pos = self.control.GetInsertionPoint()
		self.pos = self.control.GetValue().find(fstring, self.pos)
		self.start_pos = self.pos
		self.end_pos = self.pos + len(fstring)
		self.control.SetSelection(self.start_pos, self.end_pos + 1)

	def OnFindNextAction(self, event):
		fstring = self.findReplaceData.GetFindString()
		self.pos += len(fstring)
		self.pos = self.control.GetValue().find(fstring, self.pos)
		self.start_pos = self.pos
		self.end_pos = self.pos + len(fstring)
		self.control.SetSelection(self.start_pos, self.end_pos + 1)

	def OnReplaceAction(self, event):
		fstring = self.findReplaceData.GetFindString()
		rstring = self.findReplaceData.GetReplaceString()
		text = self.control.GetValue()
		if self.findReplaceData.GetFlags() & 4 == 4:
			text = re.sub(re.escape(fstring), rstring, text, count=1)
		else:
			text = re.sub(re.escape(fstring), rstring, text, count=1, flags=re.IGNORECASE)
		self.control.SetValue(text)

	def OnReplaceAllAction(self, event):
		fstring = self.findReplaceData.GetFindString()
		rstring = self.findReplaceData.GetReplaceString()
		text = self.control.GetValue()
		if self.findReplaceData.GetFlags() & 4 == 4:
			text = re.sub(re.escape(fstring), rstring, text)
		else:
			text = re.sub(re.escape(fstring), rstring, text, flags=re.IGNORECASE)
		self.control.SetValue(text)

	def OnImport(self, event):
		# Translators: The title of the Editor's Open file window
		if self.AskUserForFilename(message=_("Open file"), style=wx.FD_OPEN, **self.DefaultFileDialogOptions()):
			with open(os.path.join(self.dirname, self.filename), 'r', encoding='utf-8') as file:
				self.control.SetValue(file.read())
			self.modify = False

	def OnCloseWindow(self, event):
		pass
		# self.Destroy()

	def Destroy(self):
		super().Destroy()
		self.ad = None

	def OnTextChanged(self, event):
		self.modify = True


class Hotkey(object):
	def __init__(self, obj):
		self.obj = obj
		self.obj.control.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
		self.obj.control.Bind(wx.EVT_KEY_UP, self.onKeyUp)

		self.key_down = set([])
		self.key_map_action = [
			{
				'key': [wx.WXK_CONTROL, ord('N')],
				'action': self.OnNew,
			},
			{
				'key': [wx.WXK_CONTROL, ord('O')],
				'action': self.OnOpen,
			},
			{
				'key': [wx.WXK_CONTROL, ord('S')],
				'action': self.OnSave,
			},
			{
				'key': [wx.WXK_CONTROL, ord('W')],
				'action': self.OnExit,
			},
			{
				'key': [wx.WXK_ALT, wx.WXK_F4],
				'action': self.OnExit,
			},
		]

	def OnNew(self, event):
		self.obj.OnNew(event)

	def OnOpen(self, event):
		self.obj.OnOpen(event)

	def OnSave(self, event):
		self.obj.OnSave(event)

	def OnSaveAs(self, event):
		self.obj.OnSaveAs(event)

	def OnReload(self, event):
		self.obj.OnReload(event)

	def OnExit(self, event):
		self.obj.OnExit(event)

	def onKeyDown(self, event):
		keycode = event.GetKeyCode()
		self.key_down.add(keycode)
		action = False
		for item in self.key_map_action:
			if self.key_down == set(item['key']):
				self.key_down.clear()
				item['action'](event)
				action = True
				break
		if not action:
			event.Skip()

	def onKeyUp(self, event):
		keycode = event.GetKeyCode()
		try:
			self.key_down.remove(keycode)
		except KeyError:
			self.key_down.clear()
		event.Skip()
