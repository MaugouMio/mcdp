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

	After declaring a variable, you can append some other flags like `from` and `as virtual`.
	`from` flag has to be followed by another declared variable. For example, `folder test2() from test()` copies the contents of the `namespace` `test` to the `test2` variable. If there are arguments for `test`, you have to pass corresponding arguments to it. If you want to copy the contents of the child variable of `test`, for example, `test3` folder variable, you can use `folder test2() from test().test3()`, using `.` to concatenate child variables.

	Be ware that the variable types must be compatible when using `from`. `func` vairable is only compatible to itself, but `namespace` and `folder` variables are compatible to each other.

	`as virtual` flag must be used after all the other syntax conponents, to make the declared variable *virtual*. Virtual variables can be referenced by other variables using `from`, but will not be built as a file in the datapack.

-	**Block:** After reading variable declaration, the program will start to read the following block.<br>
	A block is an area of codes embraced in curly brackets `{}`. Both `{` and `}` have to be in an individual line. You can use a `;` mark at the end of the variable declaration to represent an empty block. For example, `func test();`. If you are declaring a `func` variable `from` another variable, you must use `;` instead of writing no contents in curly brackets, or the contents copied from the other variable will be replaced. 

	The contents in a `folder` or `namespace` typed block can be `folder` and `func` variable declarations, including sub-blocks. However in a `func` typed block, each line is viewed as a single Minecraft command (excluding indents).

	If there are arguments assigned when declaring a variable, you can use `ARG(<argument name>)` in the block of the variable.<br>
	For example:
	```
	namespace test1(an_arg)
	{
		func say_ARG(an_arg)
		{
			say ARG(an_arg)
		}
	}
	
	namespace test2() from test("test1");
	# will be expanded as:
	# namespace test2()
	# {
	# 	func say_test1
	# 	{
	# 		say test1
	# 	}
	# }
	```
	Every `ARG(an_arg)` in the block (including sub-blocks) will be replaced by the passed argument when being referenced by other variables using `from`.<br>
	Besides, you can use `ARG(_PATH)` in the block of a `func` variable. This argument does not have to be assigned or passed, and will be replaced by the parent path of this `func` variable during the datapack building stage. For example, `sample:` of the function `sample:test` or `sample:test/` of the function `sample:test/test2`.

-	**Tag:** Declare the function tags `tick` and `load`, to make specific functions run every tick or during loading the datapack.<br>
	Uses `tag tick` and `tag load` to declare the two kinds of tags. There must be a block following the declaration, but `;` is not available here. Each line of the block will be viewed as a function name, just the same name as what you pass to the `function` command. Once you import another script, the tags of the script will be appended to the tag lists, excluding tags of non imported namespaces or virtual namespaces. When building a datapack, the tags will be appended to the file sequentially.

-	**Import:** <br>
	There are two syntaxes to import libraries. Both of them can be followed by the flag `as virtual` to make imported namespaces *virtual*.

	The first syntax is `import <library name 1>[, <library name 2> [, ...]]`<br>
	For example, `import test` and `import test1, test2`. There should not be spaces in the library name, and string objects are not available here. Library names should be seperated by commas or spaces. The program will try to find the project folders or dpl scripts in `mcdp/lib` folder or in this project folder with specific names, then import the declared namespaces and tags to your project.

	The second syntax is `from <library name> import <namespace 1>[, <namespace 2>[, ...]]`<br>
	For example, `from test import test1` and `from test import test1, test2`. Only one library name can be passed in this syntax. The program will import specific namespaces and tags of them to your project.

-	**Insert Python Codes:** <br>
	You can insert some Python 3 codes in the script to create script contents.

	To insert Python codes, you have to both start and end with a line of \`\`\` . The indents must align with the first line of \`\`\` , and tabs are viewed as 4 spaces. Use `print()` to create script contents. After executing the entire Python code block, the generated contents will be appended after the code block and then read by the program.

	Be ware that there are block level problems when parsing Python codes. Only Python codes in the current block will be parsed, those of the sub-blocks will not be parsed until reading that sub-block. Also there should not be a single line with only `{` or `}` mark in the Python codes to prevent errors when reading sub-blocks. (You can add a comment after those marks to avoid this situation.)
