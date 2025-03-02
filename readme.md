# Access8Math feature

This NVDA addon enhances the mathematical content reading and writing experience.

The reading feature includes improved language translation in the ability to segment long math content into smaller parts using interactive navigation.

The writing feature includes a command menu for easier LaTeX/AsciiMath/Nemeth input and the ability to export to a visually readable HTML document for better collaboration.

## reading feature

* Reads entire lines including text and mathematical content
* Provides interactive navigation to move, read, and zoom in or out on mathematical content snippets
* Allows for reviewing text while interactive navigation
* Uses simplified speech rules
* Breaks speech between items in mathematical content

## writing feature

* Allows writing of mathematical content using LaTeX/AsciiMath/Nemeth
* Provides a command menu for inputting LaTeX
* Offers shortcut gestures for inputting LaTeX
* Allows for more efficient cursor movement during editing
* Allows reads documents containing LaTeX/AsciiMath/Nemeth data in real-time while editing the document
* Provides  converting text files into HTML files for preview and export.

# Access8Math ReadMe

This NVDA add-on enhances speech and braille output for mathematical content. Although the NVDA already integrating MathPlayer, certain aspects require improvement, such as the lack or incompleteness of language-specific translation, language-specific interactive navigation.

Interactive navigation dissects mathematical content into smaller portions for speech or braille output, allowing for the selection of the desired fragment and mode of delivery through keyboard commands. This enhances one's understanding of the structure and elements of lengthy mathematical content, and the hierarchical relationships between items.

Additionally, this NVDA add-on enables the writing of mathematical content. Using the command menu, input can be executed without having to memorize LaTeX codes. Upon completion, the document can be transformed into a visually comprehensible HTML document via the view and export function, thereby enabling seamless collaboration and discourse with others.

## Reading feature

Access8Math is able to read MathML content in web browsers such as Mozilla Firefox, Google Chrome, and Microsoft Edge, as well as MathType content in Microsoft Word.

By pressing the space bar or enter key on a MathML math object, you can enter navigation mode and interact with the content by moving, and zooming in or out on reading snippets.

* Analyze the overall mathematical meaning of the content: analyze the structure of MathML, and when it meets a specific rule, read it aloud in the mathematical meaning of the rule
* Analyze the mathematical meaning of the content item: When navigating and browsing, it will prompt the meaning of the content under its upper content. For example, there are two score items, and moving between them will enroll the item as the denominator or numerator

### navigation interactive mode command：

The following commands are available in navigation interactive mode:

* "Down Arrow": shrink the reading snippet(zoom in)
* "Up Arrow": enlarge the reading snippet(zoom out)
* "Left Arrow": Moves to the previous math content.
* "Right Arrow": Moves to the next math content.
* "home": Moves back to the top of the entire math content.
* "ctrl+C": Copies the MathML source code of the object.
* "numpad 1~9": Reads the math content as serialized text using NVDA Reviewing Text.
* "ESC": Exits the navigation mode.

## Writing feature

Comprehensive content: Incorporating Both Text and Mathematical Content

For Windows 11, the Access8Math editor must be used, while for Windows 10 or earlier versions, either Access8Math editor or Notepad can be used. It is recommended to use the built-in Access8Math editor for writing comprehensive content.

To distinguish between text content and mathematical content, you can use delimiters to enclose the mathematical notation area. This means that any data within the mathematical notation area will be considered mathematical content according to the specified delimiter, while data outside of the mathematical notation area will be treated as text content.

| category | start delimiter | end delimiter |
| --- | --- | --- |
| LaTeX(bracket) | \( | \) |
| LaTeX(money) | $ | $ |
| AsciiMath | ` | ` |
| Nemeth(UEB) | _% | _: |
| Nemeth(at) | @ | @ |

You can choose what delimiter use for LaTeX/Nemeth in the writing setting.

### Command gesture (toggle: NVDA+alt+c)

alt+m: The mark command window pops up, select LaTeX/AsciiMath/Nemeth and press enter to add LaTeX/AsciiMath marks before and after the currently selected text (the current cursor when no text is selected) and automatically move the cursor into it. Enter content quickly.

alt+l: Pop up the LaTeX command window, select the LaTeX command item to be added and press the enter key to add the corresponding LaTeX syntax at the current cursor and automatically move the cursor to the appropriate input point for quick input.

LaTeX command window

* Move to any LaTeX command item and press English letters (a~z) or f1~f12 to set shortcuts
* Move any LaTeX command item and press delete/back space to remove the shortcut that has been set
* Move to any LaTeX command item and press enter to add the corresponding LaTeX syntax at the current cursor

alt+i: When the cursor stops on the math block, you can interact with the math block for navigation

alt+h: HTML documents that can convert text data and mathematical data can be viewed or exported. The content of the math block is converted into MathML and presented side by side with the text to facilitate visual reading.

* View: Open the converted HTML document through the default .HTML extension application set by the system.
* Export: Pack the converted HTML file and the original text file into a compressed file.

alt+t: The data of the block where the cursor is located can be converted between LaTeX and AsciiMath (the cursor needs to be in the LaTeX or AsciiMath block)

In the writing settings, you can choose whether to enable command gestures at startup. Press NVDA+alt+c in the editing area to enable or disable command gestures, which can be changed in input gestures.

### Writing block navigation gestures (toggle: NVDA+alt+n)

* alt+Left arrow key: move to the start point of the previous data block
* alt+Down arrow key: Only read the content of the current data block without moving
* alt+right arrow: move to the start point of the next data block
* alt+home: move to the starting point of the current data block
* alt+end: move to the end point of the current data block
* alt+shift+left arrow: move to the previous data block and select
* alt+shift+down key: do not move, only select the content of the current data block
* alt+shift+right arrow: move to the next data block and select

In the writing settings, you can choose whether to enable the block navigation gestures when starting. Press NVDA+alt+n in the editing area to enable or disable the block navigation gestures, which can be changed in the input gestures.

### Shortcut gestures (toggle: NVDA+alt+s)

When the cursor is in the LaTeX block, press the letter, f1~f12 to quickly insert the bound LaTeX. Press shift+letter, shift+f1~f12 to read out the LaTeX currently bound to the shortcut. (Need to set the shortcut key in the command menu first)

In the writing settings, you can choose whether to enable the quick navigation gestures at startup. Press NVDA+alt+s in the editing area to enable or disable the quick navigation gestures, which can be changed in the input gestures.

### Greek letter gestures (toggle: NVDA+alt+g)

When the cursor is in the LaTeX block, press the letter to quickly insert the corresponding Greek letter LaTeX.

Mapping table

| English letter | Greek letter | LaTeX |
| --- | --- | --- |
| a | α | \alpha |
| b | β | \beta |
| c | θ | \theta |
| d | δ | \delta |
| e | ε | \epsilon |
| f | φ | \phi |
| g | γ | \gamma |
| h | η | \eta |
| i | ι | \iota |
| k | κ | \kappa |
| l | λ | \lambda |
| m | μ | \mu |
| n | ν | \nu |
| o | ο | \omicron |
| p | π | \pi |
| r | ρ | \rho |
| s | σ | \sigma |
| t | τ | \tau |
| u | υ | \upsilon |
| v | φ | \psi |
| w | ω | \omega |
| x | χ | \chi |
| y | ξ | \xi |
| z | ζ | \zeta |


### Browse navigation mode (toggle: NVDA+space)

When the navigation mode is turned on, the mathematical data block read by the cursor mobile report will read the mathematical text content instead of the original grammatical data

You can use the following key gestures to move the editing cursor and interactive navigation

* Left key: move to the starting point of the previous data block and read it out
* Right arrow: move to the start point of the next data block and read it out
* Up key: move to the previous line and read out the contents of all data blocks in this line
* Down key: move to the next line and read out the contents of all data blocks in this line
* pageUp: move up ten lines and read out the content of all data blocks in that line
* pageDown: move down ten lines and read out the content of all data blocks in that line
* home: move to the first block of the line where the cursor is located
* end: move to the last block of the line where the cursor is located

Use the cursor to move the key plus the shift key to select the text together

space/enter: When the cursor stops on a math block, it can interact with the math content of the data block to navigate

For the following keys, if you only press the single key, the editing cursor will jump to the next data block position, if you press shift + the single key at the same time, the editing cursor will jump to the previous data block position:

* l: Move to the next LaTeX data block and read it out
* a: Move to the next AsciiMath data block and read it out
* n: Move to the next Nemeth data block and read it out
* m: move to the next MathML data block and read
* t: move to the next text block and read it
* tab: move to the next interactive block (math block) and read it out

The following key gestures can be used to edit contents

* ctrl+x: cut the current cursor block
* ctrl+c: copy the current cursor block
* ctrl+v: Paste content after the current cursor block
* delete/back space: delete the current cursor block

### Access8Math editor and Access8Math Document

The edit area of Notepad in Windows 11 is rich editing area not traditional editing area, so Access8Math editor must be used in Windows 11 to use the writing feature. This editor provides such as opening old files, saving files, and view feature.

Use the Access8Math editor to write markdown documents, and when document have some resource, the resources can put into workspace of editor and be referenced. When using export feature of the editor, the referenced resources in the document will be packaged into a Archive file by Access8Math editor.

The preview and export feature under the view menu are the same as the command gesture view feature (alt+h), which can generate an Access8Math Document. The only difference between the two is that the Access8Math editor will package referenced resources into a archive file

In order to allow the document exported by the Access8Math editor to be imported again and edited, the Access8Math editor will write a Access8Math.json when exporting, which is the meta data. We call the archive file/folder containing this meta is Access8Math Document

In File Explorer, you can press the NVDA+application, if the selected path is txt/Access8Math Document, a virtual context menu will open, which can quickly open this file to view or edit it.

### content example:

* LaTeX(bracket): The solution of the quadratic equation in one variable \(ax^2+bx+c=0\) is \(\frac{-b\pm\sqrt{b^2-4ac}}{2a}\) .
* LaTeX(dollar): The solution of the quadratic equation in one variable $ax^2+bx+c=0$ is $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ .
* AsciiMath: The solution of the quadratic equation in one variable `ax^2+bx+c=0` is `x=(-b+- \sqrt(b^2-4ac))/(2a)` .
* Nemeth(UEB): The solution of the quadratic equation in one variable _%⠁⠭⠘⠆⠐⠬⠃⠭⠬⠉⠀⠨⠅⠀⠴_: is _%⠭⠀⠨⠅⠀⠹⠤⠃⠬⠤⠜⠃⠘⠆⠐⠤⠲⠁⠉⠻⠌⠆⠁⠼_: .
* Nemeth(at): The solution of the quadratic equation in one variable @⠁⠭⠘⠆⠐⠬⠃⠭⠬⠉⠀⠨⠅⠀⠴@ is @⠭⠀⠨⠅⠀⠹⠤⠃⠬⠤⠜⠃⠘⠆⠐⠤⠲⠁⠉⠻⠌⠆⠁⠼@ .
* MathML: The solution of the quadratic equation in one variable <math display="inline"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> is <math display="inline"><mfrac><mrow><mo>−</mo><mi>b</mi><mi>±</mi><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math> .

## settings

All Access8Math settings are centralized in tools -> Access8Math->Settings

### Reading Settings

* Language: Access8Math read language
* Analyze mathematical meaning of content: perform semantic analysis on the mathematical content, and when it meets a specific rule, using that rule to speak.
* show interaction window when entering interaction navigation mode: Whether to show "Access8Math interaction window" when active event entering interaction navigation mode on math object
* Reading pre-defined meaning in dictionary in interaction navigation mode: When the pattern is definied in the dictionary, use dictionary to read the meaning of subpart in the upper layer part.
* Reading of auto-generated meaning in interaction navigation mode: When the pattern is not difined or incomplete in dictionary, use automatic generation function to read the meaning of subpart in the upper layer part.
* use tone indicate to no move in interaction navigation mode
* Item interval time: Setting break time between items. Values from 1 to 100, the smaller the value, the shorter the break time, and the greater the value, the longer the break time.

### Writing Settings

* Activate command gesture at startup
* Activate block navigate gesture at startup
* Activate shortcut gesture at startup
* Use audio indicate to switching of browse navigation mode
* HTML document display:
* HTML math display:
* LaTeX delimiter:

### Rule setting: Setting whether rules are actived

### Math reader

* Speech source:
* Braille source:
* Interact source:

## localization

If you want Access8Math to have speech/braille output for MathML in different languages, you need to create a Unicode dictionary (unicode.dic) and mathematical rules (math.rule). This can be done using the GUI in Access8Math -> Localization, or by referring to the globalPlugins/Access8Math/locale in the plugin folder.

The "Unicode Dictionary" enables you to customize speech or braille output for symbols and characters. The "Mathematics Rules" allow you to customize speech or braille output for different types of mathematics.

"New language" dialog can adding language not included in Access8Math built-in. Upon Adding language option will appear in the Reading Settings language selection, Allowing for the Definition of speech/braille  via the Unicode Dictionary and Mathematics Rules, Resulting in Localization.

### Math Rules

Access8Math establishes mathematical rules according to the mathematical type and logic to decide the reading math method and order. According to different local math reading logic, the math reading text and order can be changed. The method is as follows:

Edit: After entering the "math rule", the window lists 46 math rules. Choose any math rule and select the "Edit" to enter the editing entry.

The "editing entry" can be divided into two major blocks, the "Serialized ordering" and the "Child role".

* Serialized ordering: Math rule is divided into multiple blocks according to the reading order. In this area, the reading order of child node and the delimitation text of start, inter- and the end can be changed. Taking the fractional rule mfrac as an example, this rule is divided into five reading blocks. The order 0, 2, and 4 represent the initial prompt, the project segmentation prompt, and the end prompt, respectively, and the meanings text can be changed in each field. Order 1 and 3 adjust the reading sequence of child node which can be changed in the drop-down menu.
* Child role:  The next-level sub-item of the mathematical rule. Taking the fractional rule mfrac as an example, the rule contains the numerator and the denominator. The sub-content in the upper sub-content meaning can be changed in the child-node role field.

Example: You can check the reading method of this math rule after editing. After clicking, a math content is preset the corresponding math rules for confirming whether the reading method is as expected.

Recover default: Restores the list of math rules to their initial presets.

Import: Import math rules files, which can be used to load math rules files.

Export: Save the math rules file to the specified path to share or keep.

| category | example |
| - | - |
| math | <math><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn></math> |
| mfrac | <math><mrow><mfrac><mn>3</mn><mrow><mn>1</mn><mo>+</mo><mi>x</mi></mrow></mfrac></mrow></math> |
| single_fraction | <math><mfrac><mi>3</mi><mi>4</mi></mfrac></math> |
| AddIntegerFractionType | <math><mn>17</mn><mfrac><mn>2</mn><mn>5</mn></mfrac></math> |
| mfenced | <math><mfenced><mrow><mn>5</mn><mo>+</mo><mn>6</mn></mrow></mfenced></math> |
| set | <math><mfenced open="{" close="}"><mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>4</mn></mrow></mfenced></math> |
| determinant | <math><mrowdata-mjx-texclass="INNER"><modata-mjx-texclass="OPEN">|</mo><mtablecolumnalign="centercenter"columnspacing="1em"rowspacing="4pt"><mtr><mtd><mrowdata-mjx-texclass="ORD"><mn>1</mn></mrow></mtd><mtd><mrowdata-mjx-texclass="ORD"><mn>2</mn></mrow></mtd></mtr><mtr><mtd><mrowdata-mjx-texclass="ORD"><mn>3</mn></mrow></mtd><mtd><mrowdata-mjx-texclass="ORD"><mn>4</mn></mrow></mtd></mtr></mtable><modata-mjx-texclass="CLOSE">|</mo></mrow></math> |
| matrix | <math><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">[</mo><mtable columnspacing="1em" rowspacing="4pt"><mtr><mtd><mrow data-mjx-texclass="ORD"><mi>a</mi></mrow></mtd><mtd><mrow data-mjx-texclass="ORD"><mi>b</mi></mrow></mtd></mtr><mtr><mtd><mrow data-mjx-texclass="ORD"><mi>c</mi></mrow></mtd><mtd><mrow data-mjx-texclass="ORD"><mi>d</mi></mrow></mtd></mtr></mtable><mo data-mjx-texclass="CLOSE">]</mo></mrow></math> |
| msqrt | <math><msqrt><mi>4</mi><mo>+</mo><mi>9</mi></msqrt></math> |
| mroot | <math><mroot><mi>9</mi><mi>3</mi></mroot></math> |
| single_square_root | <math><msqrt><mi>4</mi></msqrt></math> |
| msubsup | <math><msubsup><mi>a</mi><mn>n</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>n+1</mn><mn>2</mn></msubsup></math> |
| msup | <math><mrow><msup><mi>x</mi><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></msup></mrow></math> |
| msub | <math><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msub></math> |
| munderover | <math><munderover><mi mathvariant="normal">&#x3C0;</mi><mrow><mi>x</mi><mo>=</mo><mn>0</mn></mrow><mi>N</mi></munderover></math> |
| munder | <math><mrow><munder><mrow><mi>lim</mi></mrow><mrow><mi>x</mi><mo>&#x2192;</mo><mi>&#x221E;</mi></mrow></munder></mrow></math> |
| mover | <math><mover><mrow><mi>A</mi><mo>+</mo><mi>B</mi></mrow><mo>&#xAF;</mo></mover></math> |
| SingleMsubsup | <math><msubsup><mi>a</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>a</mi><mn>1</mn><mn>2</mn></msubsup></math> |
| SingleMsub | <math><mrow><msub><mrow><mi>log</mi></mrow><mn>2</mn></msub><mn>10</mn></mrow></math> |
| SingleMsup | <math><msup><mi>f</mi><mo>'</mo></msup></math> |
| SingleMunderover | <math><munderover><mi>&#x391;</mi><mi>m</mi><mi>n</mi></munderover></math> |
| SingleMunder | <math><munder><mi>lim</mi><mi>a</mi></munder></math> |
| SingleMover | <math><mover><mi>A</mi><mo>&#xAF;</mo></mover></math> |
| power | <math><msup><mn>3</mn><mn>5</mn></msup></math> |
| SquarePowerType | <math><msup><mn>3</mn><mn>2</mn></msup></math> |
| CubePowerType | <math><msup><mn>2</mn><mn>3</mn></msup></math> |
| from_to | <math><msubsup><mo>&#x222B;</mo><mn>0</mn><mn>1</mn></msubsup><msqrt><mi>x</mi></msqrt></math> |
| from | <math><munder><mo>&#x2211;</mo><mi>N</mi></munder></math> |
| to | <math><mover><mo>&#x2211;</mo><mi>N</mi></mover></math> |
| mtable | <math><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn></mtd></mtr></mtable></math> |
| mtr | <math><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn></mtd></mtr></mtable></math> |
| mtd | <math><mtable><mtr><mtd><mi>x</mi><mo>+</mo><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>1</mn></mtd></mtr><mtr><mtd><mi>x</mi><mo>+</mo><mn>2</mn><mi>y</mi></mtd><mtd><mo>=</mo></mtd><mtd><mn>4</mn></mtd></mtr></mtable></math> |
| LineType | <math><mrow><mover accent='true'><mrow><mi>A</mi><mi>B</mi></mrow><mo stretchy='true'>&#x2194;</mo></mover></mrow></math> |
| RayType | <math><mrow><mover accent='true'><mrow><mi>A</mi><mi>B</mi></mrow><mo stretchy='true'>&#x2192;</mo></mover></mrow></math> |
| LineSegmentType | <math><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo>&#xAF;</mo></mover></math> |
| VectorSingleType | <math><mrow data-mjx-texclass="ORD"><mover><mi>A</mi><mo stretchy="false">→</mo></mover></mrow></math> |
| VectorDoubleType | <math><mrow data-mjx-texclass="ORD"><mover><mrow><mi>A</mi><mi>B</mi></mrow><mo stretchy="false">→</mo></mover></mrow></math> |
| ArrowOverSingleSymbolType | <math><mrow><mover accent='true'><mrow><mi>a</mi></mrow><mo stretchy='true'>&#x2192;</mo></mover></mrow></math> |
| FrownType | <math><mrow><mover accent='true'><mrow><mi>A</mi><mi>B</mi></mrow><mo stretchy='true'>&#x2322;</mo></mover></mrow></math> |
| DegreeType | <math ><msup ><mn>15</mn><mo>∘</mo></msup><mo>+</mo><msup ><mn>10</mn><mo>∘</mo></msup><mo>=</mo><msup ><mn>25</mn><mo>∘</mo></msup></math> |
| LogType | <math><msub><mi>log</mi><mn>10</mn></msub></math> |
| BinomialType | <math><mo>(</mo><mfrac linethickness = "0"><mi>n</mi><mi>k</mi></mfrac><mo>)</mo></math> |
| NegativeSignType | <math><mo>-</mo><mn>2</mn></math> |
| PositiveSignType | <math><mo>+</mo><mn>2</mn></math> |
| mmultiscripts | <math><mmultiscripts><mi>T</mi><mprescripts/><mi>n</mi><mi>m</mi></mmultiscripts></math> |
| mprescripts | <math><mmultiscripts><mi>T</mi><mprescripts/><mi>n</mi><mi>m</mi></mmultiscripts></math> |

## example

Math contents in Wiki are all written by MathML.

* Quadratic equation: https://en.wikipedia.org/wiki/Quadratic_equation
* Matrix multiplication: https://en.wikipedia.org/wiki/Matrix_multiplication
* Cubic function: https://en.wikipedia.org/wiki/Cubic_function

Quadratic equation

* LaTeX: \(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\)
* AsciiMath: `x=(-b+- \sqrt(b^2-4ac))/(2a)`
* MathML: <math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mo>-</mo><mi>b</mi><mo>&#xB1;</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>

github: https://github.com/tsengwoody/Access8Math

Please report any bugs or comments, thank you!

# Access8Math update log

## Access8Math v3.7 Update

* new feature: Auto-Complete feature in write feature.
* Added "mixed number" rule to the Nemeth to LaTeX translator.
* In Access8Math editor, Added close button on the upper right corner to close the Access8Math editor.
* Fixed SimultaneousEquationsType rule(read feature).
* Fixed "|" symbol don`t convert to text according in Unicode dictionary(read feature).
* Fix issues with Converting ∫ Nemeth Braille to LaTeX.

## Access8Math v3.6 Update

* new feature: Nemeth Braille Input, with the same functionality as LaTeX input. Allows for real-time interactive navigation (Alt+I) during editing and supports outputting HTML+MathML documents.
* new feature: Added Nemeth delimiter UEB/at(@@) for distinguish Nemeth content.
* new feature: You can convert and copy LaTeX from Math object in interactive navigation mode.
* Added the NVDA+Shift+F10 shortcut to open  virtual context menu in the file explorer.
* Fixed and optimized localized UI issues and cleaned localized file format.

## Access8Math v3.5 Update

* Vectors and rays can be distinguished correctly
* Utilizing dialogue to display image, video, or audio resources in an Access8Math HTML document
* Using a new window to open link resources in an Access8Math HTML document
* The MathML namespace is exported when copying MathML from the Math object in interactive navigation mode
* Display font adjustment, find and replace feature in Access8Math editor
* Compatibility with NVDA 2023.1

## Access8Math v3.4 Update

* Speech, Braille, and interactive source move to Preferences -> Settings -> Math Reader category.
* Integrated MathCAT, you can choose what speech, braille, and interactive source(Access8Math/Math Player/MathCAT) you need in Math Reader settings panel when having already installed Math Player/MathCat.
* Used MultiCategorySettingsDialog to collect settings dialog.
* Press NVDA+alt+e open text file with the built-in editor in File Explore.
* In virtual menus, submenu can open by enter
* Implenment MathML menclose tag rule
* new feature: virtual context menu in File Explorer. It can quickly open Access8Math Document to view or edit it(Please read "Access8Math editor and Access8Math Document" section to know detail information)

## Access8Math v3.3 Update

* Add built-in editor using traditional editing area because of windows 11 changed to UIA editing area
* built-in editor new/open/save feature
* Access8Math language initial setting is based on NVDA language setting
* Improved speech and braille display in virtual menus
* Compatibility with NVDA 2022.1
* Fixed marked menu cannot open when document is empty
* Fixed translate LaTeX/AsciiMath feature
* Fixed HTML document rendering problem when HTML document display setting choice text option

## Access8Math v3.2 Update

* New feature "`" to separate data blocks, the blocks enclosed by "`" are AsciiMath data
* New feature editing-shortcut for browse navigation mode cut (ctrl+x), copy (ctrl+c), paste (ctrl+v), delete (delete/back space)
* New feature moving-shortcut for browse navigation mode move between interactive data blocks (tab), move between AsciiMath data blocks (a)
* Change move cursor way in browse navigation mode - move cursor way with up, down, left and right arrow keys and read out the contents of the data block after the movement.
* When the cursor moves in the browse navigation mode, the math data block will read the serialized textual content of math instead of the source code
* When the cursor is in the math data block in the browse navigation mode, press the space or enter key to interact with the math data block.
* New feature English letters as shortcut keys that can be setted
* New feature greek alphabet shortcut gesture
* Shortcut key input is only apply in the LaTeX area
* set using audio or speech indicate to switching of browse navigation mode
* The LaTeX command menu can be opened in the text area and insert LaTeX separators when LaTeX command inserting
* New feature translation menu, which can convert the LaTeX/AsciiMath data format of the block where the cursor is located. It belongs to the command gesture group. When the cursor is in the LaTeX/AsciiMath block, press alt+t to open the translation menu (in the browse navigation mode, ctrl+t)
* New feature batch menu, which can convert the entire document LaTeX/AsciiMath data format to each other, and can convert the LaTeX separator between brackets and dollar. It belongs to the command gesture group. Press alt+b to open the batch menu
* Added MathML block type, support alt+i, single letter navigation "m", tab movement in browse navigation mode
* New feature braille custom-defined math rules and unicode dictionary, which are the same as speech
* The exported HTML can show with markdown
* The exported HTML is added page title and file name by notepad window title.

## Access8Math v3.1 Update

* HTML windows are now presented as virtual menu
* Fixed an issue where the HTML view cannot be converted when text include "`" character
* When the number of words in the document is greater than 4096, the content will not be converted to HTML view
* Added mathematical set LaTeX commands
* Update alt+m to insert "\(", "\)" LaTeX marks before and after the currently selected text (when there is no selected text, it is the current cursor position)
* In the General settings, you can choose whether the math content in the exported HTML is presented on a separate line(block/inline)
* When exporting HTML, save the original text file in the compressed file
* In the general settings, you can choose to use bracket or money symbol as the LaTeX delimiter
* In the general settings, you can choose the source of speech, braille, and interaction(Access8Math or Math Player)
* Activate/deactivate write/block navigate/shortcut gesture by gesture
* switch the source of speech/braille/interact source by gesture(Access8Math or Math Player)

## Access8Math v3.0 Update

* Write mathematical content in AsciiMath
* Write mathematical content in LaTeX
* Writing mixed content (text content and mathematical content)
* Use shortcut keys to move the cursor to different types of blocks in edit field
* Use command menu to select commands in edit field
* Set shortcuts in the LaTeX command menu
* Review and export content in edit field to HTML

## Access8Math v2.6 Update

* Auto entering interactive mode when showing Access8Math interaction window.
* You can choose how to hint no movement in interactive mode: beep or speech 'no move' two way.
* The content of the current item will be repeated again When there is no movement.

## Access8Math v2.5 Update

* Adding Russian translation of rules and UI. Thanks to the translation work of Futyn-Maker.
* Fixing compound symbol translation failed bug.
* Removing duplicates of lowercase letters and added general uppercases in en unicode.dic(0370~03FF).

## Access8Math v2.3 Update

* Fix bug.

## Access8Math v2.3 Update

* Compatibility with Python3
* refactoring module and fix code style
* Adding one symbol vector rule

## Access8Math v2.2 Update

*fix bug incorrect speech when a single node has more characters.
* Fix compatibility issue in NVDA 2019.2, thanks to pull requests of CyrilleB79.
* Fix bug in unicode dict has duplicate symbols.
* Add translations in French, thanks to the translation work of CyrilleB79.
* Adjust keyboard shortcut.

## Access8Math v2.1 Update

* In "General Settings", you can set whether "Access8Math interaction window" is automatically displayed when entering interactive mode.
* In interactive mode, "interaction window" can be displayed manually via ctrl+m when "interaction window" are not showed.
* Fix multi-language switching bug.
* Add translations in Turkish, thanks to the translation work of cagri (çağrı doğan).
* Compatibility update for nvda 2019.1 check for add-on`s manifest.ini flag.
* Refactoring dialog window source code.

## Access8Math v2.0 Update

* Add multi-language new-adding and customizing settings,and add three windows of "unicode dictionary", "math rule", "New language adding"
* The "unicode dictionary" can customize the reading way of each math symbolic text.
* "math rule" can customize the reading method and preview the modification through the sample button before completed.
* "New language adding" allows adding language not provided in the built-in system. The newly language will be added to the general settings, and multi-language customization can be achieved through reading definition of "unicode dictionary" and "mathematical rules".
* improved in interactive mode, you can use the number keys 7~9 to read sequence text in the unit of line.

## Access8Math v1.5 update log

* In "general setting" dialog box add setting pause time between items. Values from 1 to 100, the smaller the value, the shorter the pause time, and the greater the value, the longer the pause time.
* Fix setting dialog box can't save configure in NVDA 2018.2.

## Access8Math v1.4 update log

* Adjust settings dialog box which divided into "general setting" and "rules setting" dialog box. "General Settings" is the original "Access8Math Settings" dialog box, and "Rule Settings" dialog box is for selecting whether specific rules are enabled.
* New rules
 * vector rule: When there is a "⇀" right above two Identifier, the item is read as "Vector...".
 * frown rule：When there is a " ⌢ " right above two Identifier, the item is read as "frown...".
* Fix bug.

## Access8Math v1.3 update log

* New rule
 * positive rule: Read "positive" rather than "plus" when plus sign in first item or its previous item is certain operator.
 * square rule: When the power is 2, the item is read as "squared".
 * cubic rule: When the power is 3, the item is read as "cubed".
 * line rule: When there is "↔" right above two Identifier, the item is read as "Line ...".
 * line segment rule: When there is "¯" right above two Identifier, the item is read as "Line segement ...".
 * ray rule: When there is a "→" right above two Identifier, the item is read as "Ray ..."
* Add interaction window：　Pressing "Space" in math content to open "Access8Math interaction window" which contains "interaction" and "copy" button.
 * interaction: Into math content to navigate and browse.
 * copy: Copy MathML object source code.
* Add zh_CN UI language(.po).
* Adjust inheritance relationship between rules to ensure proper use of the appropriate rules in conflict.
* Fix bug.

## Access8Math v1.2 update log

* New rule
 * negative number rule: Read 'negative' rather than 'minus sign' when minus sign in first item or its previous item is certain operator.
 * integer add fraction rule: Read 'add' between integer and fraction when fraction previous item is integer.
* Program architecture improve
 * add sibling class
 * add dynamic generate Complement class
* Fix bug

## Access8Math v1.1 update log

* In navigation mode command, "Ctrl+c" copy object MathML source code.
* Settings dialog box in Preferences:
 * Language: Access8Math reading language on math content.
 * Analyze the mathematical meaning of content: Semantically analyze the math content, in line with specific rules, read in mathematical meaning of that rules.
 * Read defined meaning in dictionary: When the pattern is definied in the dictionary, use dictionary to read the meaning of subpart in the upper layer part.
 * Read of auto-generated meaning: When the pattern is not difined or incomplete in dictionary, use automatic generation function to read the meaning of subpart in the upper layer part.
* Add some simple rule. Single rules are simplified versions of various rules. When the content only has one single item, for better understanding and reading without confusion, you can omit to choose not to read the script before and after the content.
* Update unicode.dic.
* Fix bug.
