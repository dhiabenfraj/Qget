#! /usr/bin/env python3

'''
	author : xreaad
	name : Qget
	description: 
		Qget is a tool based on (python oop) created by xreaad to scrapping web sites && a lot more things like 
			[1] - post && get data
			[2] - download files from site
			[3] - get information from site 
			[4] - finding elemnts of the site 
			[.] - etc ..
'''

from bs4 import BeautifulSoup
from banner import logo
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

logo()

class searching():
	"""searching : search for all item in the site case the order of user
		searching process : 
			[1] - find the main files && all assets files of the site
			[2] - ...
	"""
	def __init__(self, url):
		self.url = url
		self.re = requests.get(url)
		self.soup = BeautifulSoup(re.text, 'html.parser')

	def all_element(self):
		pass

		







def start(job):
	""" print the job on the screen with coloring"""
	print(f'{blue}[{green}+{blue}]{yellow} {job}')

def error(err):
	""" print the error with coloring """
	print(f'{blue}[{red}!{blue}]{yellow} {err}')



start('building soup && directories')
input()