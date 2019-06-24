# -*- coding: UTF-8 -*-
import sys, os

install_path = os.path.expandvars("%LOCALAPPDATA%\\mcdp")
try:
	os.listdir(install_path)
except FileNotFoundError:
	os.mkdir(install_path)

# set environment path
os.environ["path"] = os.environ["path"] + ";" + install_path + "\\"
