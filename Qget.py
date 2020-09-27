#! /usr/bin/env python3

'''
	author : xreaad
	description: 

'''

import os
import sys
from colorama import *
from time import sleep
import requests
import argparse

__password__ = '0xreaad'

red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
purple = '\033[35m'
yellow = '\033[93m'
nocolor = '\033[00m'
bold = '\033[01m'

def logo():
	print(r""" {bold}
	{green}			________   {yellow}               __   
	{green}			\_____  \  {yellow}  ____   _____/  |_ 
	{green}			 /  / \  \ {yellow} / ___\_/ __ \   __\
	{green}			/   \_/.  \{yellow}/ /_/  >  ___/|  |  
	{green}			\_____\ \_/{yellow}\___  / \___  >__|  
	{green}			       \__>{yellow}_____/      \/      
	""".format(bold=bold, green=green, yellow=yellow))


