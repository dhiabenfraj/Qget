#! /usr/bin/env python3

__author__ = 'xreaad'
__password__ = '0xreaad'

__description__ = """
	Qget is a tool based on (python oop) created by xreaad to scrapping web sites && a lot more things like 
	post && get data, download files from site, get information from site, finding elemnts of the site, etc ..
"""

__help__ = """
	
"""

from bs4 import BeautifulSoup
from banner import logo
import os
import sys
from colorama import *
from time import sleep
import requests
import argparse

red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
purple = '\033[35m'
yellow = '\033[93m'
nocolor = '\033[00m'
bold = '\033[01m'

logo() # print the banner


def start(job): # print the starting job
	print(f'{blue}[{green}+{blue}]{yellow} {job}')

def error(err): # print the error
	print(f'{blue}[{red}!{blue}]{yellow} {err}')


class searching():
	"""	searching : search for all item in the site case the order of user
		searching process : 
		- find the main files && all assets files of the site
	"""
	
	bad_type = [None, '', '#'] # list to stay away when searching

	def __init__(self, url):
		self.url = url
		self.re = requests.get(url)
		self.soup = BeautifulSoup(self.re.text, 'html.parser')


	def all_files(self):
		""" search all the items in the site && put them in lists
			&& remove duplicates from the lists of elements 
			return html_files, img_files, css_files, script_files """

		html_files = [link.get('href') for link in self.soup.find_all('a') if not link.get('href') in self.bad_type]
		img_files = [link.get('src') for link in self.soup.find_all('img') if not link.get('src') in self.bad_type]
		css_files = [link.get('href') for link in self.soup.find_all('link') if not link.get('href') in self.bad_type]
		script_files = [link.get('src') for link in self.soup.find_all('script') if not link.get('src') in self.bad_type]

		# remove duplicates from the lists of elements
		html_files = list(dict.fromkeys(html_files))
		img_files = list(dict.fromkeys(img_files))
		css_files = list(dict.fromkeys(css_files))
		script_files = list(dict.fromkeys(script_files))

		return html_files, img_files, css_files, script_files

	def user_search(self, **filtres):
		pass

	def find_script(self):
		pass



def parse():
	parser = argparse.ArgumentParser(description=__description__)
	parser.add_argument('-s', '--script', help='get all script file from the site', action='store_true')
	parser.add_argument('-f', '--file', help='get file from the site', action='store_true')
	parser.add_argument('-o', '--path', help='path when u save the file', type=str)
	parser.add_argument('-p', '--post', help='post data to the site', type=str)
	parser.add_argument('-g', '--get', help='get data from the site', type=str)
	parser.add_argument('-d', '--download', help='download file from the site', type=str)
	parser.add_argument('url', help='url of the site url shoul start with http:// or https://', type=str)
	args = parser.parse_args()
	return args
	
def Qget():
	argument = parse()
	search = searching(argument.url)


if __name__ == '__main__':
	Qget()