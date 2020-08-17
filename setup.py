''' this python file use the sys module to see your OS and choose the right version of script '''
''' os --> win/linux '''
''' made by xreaad '''
''' Copyright © xreaad '''

from sys import platform as _platform
import os

# python library to execute the script correctly

try:
	os.system('pip3 install colorama')
	os.system('pip3 install BeautifulSoup4')
	os.system('pip3 install requests')
except Exception:
	print('\033[91m [-] please install pip3 - python package \033[00m')



'''
# choose the right script
if _platform == "linux" or _platform == "linux2":
    import test
elif _platform == "darwin":
	import mainmac
elif _platform == "win32" or _platform == "win64":
    import test

ENJOY GUYS WITH THIS COOL SCRIPT'''
