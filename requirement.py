#! /usr/bin/env python3

import os

try:
	os.system('pip3 install colorama')
	os.system('pip3 install BeautifulSoup4')
	os.system('pip install requests')
	os.system('clear')
except Exception:
	print('\033[93m [-] please install pip3 - python package \033[00m')
