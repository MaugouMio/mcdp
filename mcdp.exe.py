# -*- coding: UTF-8 -*-
import sys

def build_datapack():
	filename = sys.argv[2]
	if filename[-4:] != ".dpl":
		filename += ".dpl"
	
	with open(filename, "r", encoding='UTF-8') as script:
		pass
	
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