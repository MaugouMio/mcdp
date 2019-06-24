# -*- coding: UTF-8 -*-
import sys, os

install_path = os.path.expandvars("%LOCALAPPDATA%\\mcdp")
module_path = ["./", install_path + "\\lib\\"]

class Folder:
	def __init__(self):
		self.items = dict()
		self.virtual = False



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

def find_lib(script_name):
	for path in module_path:
		if os.path.isfile(path + script_name + "dpl"):
			return path + script_name + "dpl"
	raise ImportError("No module named '" + script_name + "'")
	
def read_script(script):
	namespaces = {}

	line_index = 0
	while line_index < len(script):
		this_line = script[line_index].lstrip('\t')
		# delete comments
		if this_line[0] == '#':
			del script[line_index]
		else:
			splitted_line = split_by_chars(this_line)
			# not an empty row
			if len(splitted_line) > 0:
				if splitted_line[0] == "import":
					if len(splitted_line) < 2:
						raise SyntaxError(this_line)
						
					imported = read_script(find_lib(splitted_line[1]))
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
				elif splitted_line[0] == "from":
					if len(splitted_line) < 4 or splitted_line[2] != "import":
						raise SyntaxError(this_line)
					
					# delete unneeded namespaces
					imported = read_script(find_lib(splitted_line[1]))
					imported_namespaces = list(imported.keys())
					for key in imported_namespaces:
						if key in splitted_line[3:-2]:
							imported.pop(key)
					
					if splitted_line[-2] == "as" and splitted_line[-1] == "virtual":
						# set namespaces as virtual
						for key in imported.keys():
							imported[key].virtual = True
					
					merge_two_dicts(namespaces, imported)
				elif splitted_line
				
	return namespaces

def build_datapack():
	filename = sys.argv[2]
	if filename[-4:] != ".dpl":
		filename += ".dpl"
	
	with open(filename, "r", encoding='UTF-8') as script:
		namespaces = read_script(script.read().splitlines())
	
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