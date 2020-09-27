from colorama import *

red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
purple = '\033[35m'
yellow = '\033[93m'
nocolor = '\033[00m'
bold = '\033[01m'

def logo():
	print(r""" {bold}
	{red}	_____________________________________________________
	{green}			________   {yellow}               __   
	{green}			\_____  \  {yellow}  ____   _____/  |_
	{green}			 /  / \  \ {yellow} / ___\_/ __ \   __\
	{green}			/   \_/.  \{yellow}/ /_/  >  ___/|  |  
	{green}			\_____\ \_/{yellow}\___  / \___  >__|  
	{green}			       \__>{yellow}_____/      \/  {blue} created by{green} xreaad
	{red}	_____________________________________________________ {yellow}
    
	""".format(bold=bold, red=red, green=green, yellow=yellow, blue=blue))

