# -*- coding: UTF-8 -*-
import sys, os
from io import StringIO

install_path = os.path.expandvars("%LOCALAPPDATA%/mcdp")
module_path = [install_path + "/lib/"]

class Folder:
	def __init__(self):
		self.items = dict()
		self.virtual = False
		
	def copy(self):
		new_folder = Folder()
		for key in self.items.keys():
			new_folder.items[key] = self.items[key].copy()
		new_folder.virtual = self.virtual
		
		return new_folder
		
	def build(self):
		pass
		
class Function:
	def __init__(self):
		self.commands = ""
		self.virtual = False

	def copy(self):
		new_function = Function()
		new_function.commands = self.commands
		new_function.virtual = self.virtual
		
		return new_function
		
	def build(self):
		pass
		


sep_char = [' ', ',']
def split_by_chars(string, sep = sep_char, clear_null = True):
	splitted = []
	first_char = 0
	for i in range(len(string)):
		if string[i] in sep_char:
			if not (clear_null and i == first_char):
				splitted.append(string[first_char:i])
			first_char = i + 1
	if not (clear_null and first_char == len(string)):
		splitted.append(string[first_char:])
	
	return splitted

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

###########################################
#             tool functions              #
# ======================================= #
#            normal functions             #
###########################################

def find_lib(script_name, search_path):
	for path in search_path:
		# fix directory path
		if path[-1] != '/' and path[-1] != '\\':
			path += '/'
			
		if os.path.isfile(path + script_name + "dpl"):
			with open(path + script_name + "dpl", "r", encoding='UTF-8') as f:
				script = f.read().splitlines()
			return script, path
		elif os.path.isfile(path + script_name + "/__main__.dpl"):
			with open(path + script_name + "/__main__.dpl", "r", encoding='UTF-8') as f:
				script = f.read().splitlines()
			return script, path + script_name
			
	raise ImportError("No module named '" + script_name + "'")

def parse_code(code):
	old_stdout = sys.stdout
	redirected_output = sys.stdout = StringIO()
	exec(code)
	sys.stdout = old_stdout
	
	return redirected_output.getvalue()

def read_block(code, this, args): # 'this' is a new Folder() or Function() object
	# replace arguments
	# read sub blocks
	pass

def parse_definition(line):
	end_index = line.find(' ') + 1
	
	return declare_name, argv, template, is_virtual, end_index

def add_namespace(name, namespace, namespaces):
	if name in namespaces.keys() and not namespaces[name].virtual:
		raise NameError("namespace " + name + " already defined!")
	
	namespaces[name] = namespace
	
def read_script(script, this_dir):
	search_path = [this_dir] + module_path
	
	namespaces = {}
	description = ""

	block_stack = 0
	block_content = ""
	this_block = None
	
	in_pycode = False
	pycode = ""
	
	line_index = 0
	while line_index < len(script):
		# parsing python codes
		if in_pycode:
			if script[line_index].rstrip(" \t") == "```":
				parsed_pycode = parse_code(pycode).split('\n')
				for i in range(len(parsed_pycode)):
					script.insert(line_index + 1, parsed_pycode[len(parsed_pycode) - i - 1])
				# reset stats
				in_pycode = False
				pycode = ""
			else:
				pycode += script[line_index] + '\n'
				line_index += 1
		else:
			this_line = script[line_index].replace('\t', '')
			# delete comments
			if this_line[0] == '#':
				del script[line_index]
			else:
				# reading block contents
				if block_stack > 0:
					# deal with block stack
					# copy this line to block_content (without the last '}')
					pass
				
				# parsing contents by lines
				else:
					splitted_line = split_by_chars(this_line)
					# not an empty row
					if len(splitted_line) > 0:
						# import module
						if splitted_line[0] == "import":
							if len(splitted_line) < 2:
								raise SyntaxError(this_line)
								
							imported = read_script(find_lib(splitted_line[1], search_path))
							if len(splitted_line) == 4 and splitted_line[2] == "as" and splitted_line[3] == "virtual":
								# set namespaces as virtual
								for key in imported.keys():
									imported[key].virtual = True
							elif len(splitted_line) != 2:
								raise SyntaxError(this_line)
							
							for key in imported.keys():
								if key in namespaces.keys() and namespaces[key].virtual == False:
									raise NameError("namespace " + key + " already defined!")
									
							merge_two_dicts(namespaces, imported)
							
							
							
						# from module import namespaces
						elif splitted_line[0] == "from":
							if len(splitted_line) < 4 or splitted_line[2] != "import":
								raise SyntaxError(this_line)
							
							# delete unneeded namespaces
							imported = read_script(find_lib(splitted_line[1], search_path))
							imported_namespaces = list(imported.keys())
							for key in imported_namespaces:
								if key in splitted_line[3:-2]:
									imported.pop(key)
							
							if splitted_line[-2] == "as" and splitted_line[-1] == "virtual":
								# set namespaces as virtual
								for key in imported.keys():
									imported[key].virtual = True
							
							merge_two_dicts(namespaces, imported)
							
							
							
						# define a namespace (blocks are separated by {} instead of LF)
						elif splitted_line[0] == "namespace":
							declare_name, argv, template, is_virtual, end_index = parse_definition(this_line)
							
							if (end_index + 1) == len(this_line):
								this_block = Folder()
								block_stack += 1
								
								# preview and ignore the next line
								line_index += 1
								if script[line_index].lstrip(" \t").rstrip(" \t") != '{':
									raise SyntaxError(script[line_index])
							else:
								rest_contents = this_line[(end_index + 1):].lstrip(" \t").rstrip(" \t")
								if rest_contents == '{':
									block_stack += 1
								elif rest_contents == ';':
									new_namespace = template.copy()
									new_namespace.virtual = is_virtual
									add_namespace(declare_name, new_namespace, namespaces)
								else:
									raise SyntaxError(this_line)
						
						
						
						# python codes to generate contents
						elif splitlines[0] == "```":
							in_pycode = True
						
						
						
						# add minecraft tags
						elif splitlines[0] == "tag":
							pass
						
						
						
						# unknown line
						else:
							raise SyntaxError(this_line)
						
						line_index += 1
						
	return description, namespaces

def build_datapack():
	filename = sys.argv[2]
	if filename[-4:] != ".dpl":
		filename += ".dpl"
	
	this_dir = os.path.dirname(os.path.abspath(filename))
	with open(filename, "r", encoding='UTF-8') as script:
		description, namespaces = read_script(script.read().splitlines(), this_dir)
	
def install_module():
	pass

	
	
if len(sys.argv != 3):
	print("Use 'mcdp make <script file path>' to build a datapack")
	print("Use 'mcdp install <module name>' to install a module from the internet")
	sys.exit(0)
else:
	if sys.argv[1][0].lower() == "m":
		build_datapack()
	elif sys.argv[1][0].lower() == "i":
		install_module()