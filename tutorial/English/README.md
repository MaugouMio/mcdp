# Tutorial

-	**Main Concept** <br>
	All MCDP commands have to be done in command line (cmd), it will based on the current directory to find files. For more information about changing current directory, please check [WIKI](https://en.wikipedia.org/wiki/Cd_(command)) page. Once you installed MCDP successfully, entering `mcdp` in cmd should display available mcdp commands.

-	**Creating Datapack Project** <br>
	Enter `mcdp create <project name>` to create a project folder in current directory with specific project name. `<Project name>` can be a directory path, the project name will be the basename of the path. You can move the project folder or rename it anytime.
	The project folder contains `__main__.dpl` and `build` folder. `__main__.dpl` is the main script file, You can not change its name or directory. Once the datapack is built, the built datapack will be in the `build` folder.

-	**Editing Script** <br>
	You can use any text editor to edit the dpl script. If you are using Notepad++ as your editor, you can download [highlight xml for notepad++](https://www.mediafire.com/file/93hgdfqin7kseq3/dpl.xml/file) to have highlight.

	**How to use Highlight:** Open Notepad++ ➔ Language ➔ Define your language... ➔ Import... ➔ Select the downloaded `dpl.xml` file ➔ Done!

-	**Building Datapack** <br>
	Enter `mcdp make <project folder directory>` to build a project into a datapack. The built datapack will be in the `build` folder in the project folder.

-	**Installing Library** <br>
	Enter `mcdp install <library name>` to download and install a library on the internet. (This command is not implemented yet.)

	Put other project folders or pure dpl scripts in the `lib` folder in the installed `mcdp` folder, also can you put them under the same directory of `__main__.dpl`. After that you can import the libraries according to their name.  Be ware that there should be no spaces in the library name.

	Enter `mcdp uninstall <library name>` to remove libraries with specific library name.

---

# dpl Format Introduction
For some example usage please check the codes in [samp](https://github.com/MaugouMio/MCDP/tree/master/samp)<br>
The script is read line by line. Indents are not restricted instead of inserted python codes.<br>
-	**Blank Line:** Simply get ignored.
-	**Comment:** Lines start with `#` (excluding indents) are comments, will be ignored like blank lines.
-	**String Object:** Contents in double quotation marks `""` are viewed as a string object.
-	**Datapack Description:** Written in `description = <Description String>` format. `<Description String>` can be a string object.
-	**Variable (File) Declaration:** <br>
	You can declare a `namespace folder`/`normal folder`/`function file` using `namespace`/`folder`/`func`. If you declare a duplicated name of a `namespace` variable and the formerly declared namespace is not *virtual*, it will cause error. However, if you declare a duplicated name of other type of variables under a namespace, the newly declared variable will replace the formerly declared variable.

	For instance you can use `namespace test()` to declare a `namespace folder` called `test`. Remember that all `folder` and `func` variables must belong to a `namespace`, and `namespace` variables must NOT belong to another namespace. There can be arguments in the parentheses, sepeated by spaces and commas. Arguments can be string objects. Be ware that variables with arguments can be only defined *virtual* (`as virtual`), which will be introduced later.

	宣告完一個檔案後可以在同一行後面加上其它參數，例如`from`與`as virtual`。
	其中`from`後面必須接續其它已定義的檔案，例如`folder test2() from test()`會將上述宣告的`test`這個`namespace`中定義的內容複製到`test2`這個資料夾。若`test`有設定參數，這邊也需要在`test`後面的小括號傳入對應數量的參數。假設`test`這個`namespace`中有另外宣告`test3`這個資料夾，若是想要複製`test3`的內容到`test2`中，則可以使用`folder test2() from test().test3()`，以點`.`來串接子檔案。

	要注意`from`的來源檔案類型必須與宣告的檔案類型相容，其中`func`不可以與`namespace`或`folder`相容，但`namespace`與`folder`類型則可相容。

	而`as virtual`必須宣告在該行的最後面，代表這個檔案是*虛擬檔案*。虛擬檔案可以被其它宣告的檔案使用`from`來引用，但是不會在建置資料包的時候被建置出來。

-	**區塊：** 完成檔案的宣告後，會從接下來的內容中讀取區塊。<br>
	區塊是由大括號`{}`包裝的範圍，其中`{`與`}`兩個符號都必須個別存在獨立的一行中，不可包含其它內容，否則會導致判讀錯誤。另外可以在宣告檔案的那行的末尾加上分號`;`代表一個空的區塊，例如`func test();`。分號在資料夾類型的檔案宣告中與空的括號無異，但在`function`檔案的宣告中，如果使用空括號則會由空的內容取代先前已經存在的內容。

	資料夾類型檔案的區塊中可以宣告其它資料夾檔案或`function`檔案，而`function`檔案的區塊中則是每一行都視為一條 Minecraft 指令，並且忽略縮排。

	若是宣告的檔案有包含參數，在接下來的區塊中可以使用`ARG(參數名稱)`代表當參數傳入時要被對應替代的內容。接下來在讀取這個區塊的時候，會先將所有參數替代成對應的內容再進行讀取。<br>
	另外在`function`檔案的指令內容中可以使用系統參數`ARG(_PATH)`。在建置資料包時會被替換為：使用 function 指令呼叫該 function 時，其所在資料夾的路徑。<br>
	例如`sample:test`中的`sample:`或`sample:test/test2`中的`sample:test/`。

-	**標籤：** 宣告`tick`與`load`兩種標籤，使指定 function 連閃或在載入時執行。<br>
	分別透過`tag tick`以及`tag load`來宣告兩種標籤，宣告完必須接續一個區塊，不可使用分號作為空區塊。區塊內每一行的內容會被視為一個 function 名稱，與 Minecraft 中呼叫 function 時輸入的名稱相同，並且依序添加到標籤當中。需要注意的是，若對應的`namespace`被設定為*虛擬檔案*，則與該`namespace`相關的標籤都不會被套用。

-	**引入：** <br>
	分為兩種引入方式，兩種均能在該行最後加上`as virtual`參數，將引入的`namespace`檔案設定為*虛擬檔案*。

	第一種格式為`import <函式庫名稱1>[, <函式庫名稱2> [, ...]]`<br>
	例如`import test`或`import test1, test2`。函式庫名稱不能有空格，也不接受字串形式的輸入，要引入的函式庫之間以逗號或空格隔開。程式會從專案資料夾以及系統安裝的函式庫中尋找對應名稱的腳本文件或專案內容，並將其中宣告的`namespace`檔案引入到你的專案中。

	第二種格式為`from <函式庫名稱> import <namespace1>[, <namespace2>[, ...]]`<br>
	例如`from test import test1`或`from test import test1, test2`。注意只能輸入一個函式庫，程式會從該函式庫找到對應名稱的`namespace`引入到你的專案中。

-	**安插 Python 程式碼：** <br>
	你可以安插部分 Python 3 的程式碼在腳本中，用以產生腳本內容。

	要安插 Python 程式碼，你必須先在獨立的一行中輸入\`\`\`作為開端，並同樣以獨立的一行\`\`\`作為結尾。其中程式碼內容的縮排必須與第一行的\`\`\`對齊，一個 tab 視為 4 個空格處理。將你要產生的腳本內容透過`print()`的方式打印出來，完整執行整段程式之後會將打印出來的內容視為一般腳本內容進行讀取。

	要注意在解析 Python 程式碼的時候有區塊層級問題，程式只會解析當前區塊中的 Python 程式碼，內層區塊中的 Python 程式碼會在讀取該區塊的時候才被解析。
