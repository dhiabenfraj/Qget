#! /usr/bin/env python3

from bs4 import BeautifulSoup
import os
import sys
import re
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

__author__ = 'xreaad'
__password__ = '0xreaad'

__description__ = """
	Qget is a tool based on (python oop) created by xreaad to scrapping web sites && a lot more things like 
	post && get data, download files from site, get information from site, finding elemnts of the site, etc ..
"""

__help__ = r"""{b}
	{r}	_________________________________________________
	{g}		________   {y}               __   
	{g}		\_____  \  {y}  ____   _____/  |_
	{g}		 /  / \  \ {y} / ___\_/ __ \   __\
	{g}		/   \_/.  \{y}/ /_/  >  ___/|  |  
	{g}		\_____\ \_/{y}\___  / \___  >__|  
	{g}		       \__>{y}_____/      \/{blue}created by{g} xreaad		  
	{r}	_________________________________________________ {y}

""".format(b=bold, r=red, g=green, y=yellow, blue=blue)



def start(job): # print the starting job
	print(f'{blue}[{green}+{blue}]{yellow} {job}')

def error(err): # print the error
	print(f'{blue}[{red}!{blue}]{yellow} {err}')


class searching():
	"""	searching : search for all item in the site case the order of user
		searching process : 
		- find the main files && all assets files of the site
	"""

	def __init__(self, url):
		self.url = url
		self.re = requests.get(url)
		self.soup = BeautifulSoup(self.re.text, 'html.parser')
		self.bad_type = [None, '', '#'] # list to stay away when searching


	def all_files(self):
		""" search all the items in the site && put them in lists
			&& remove duplicates from the lists of elements 
			return html_files, img_files, css_files, script_files """

		html_files = [link.get('href') for link in self.soup.find_all('a') if not link.get('href') in self.bad_type and not link.get('href').startswith('#') and not link.get('href').startswith('http')]
		img_files = [link.get('src') for link in self.soup.find_all('img') if not link.get('src') in self.bad_type and not link.get('src').startswith('#') and not link.get('src').startswith('http')]
		css_files = [link.get('href') for link in self.soup.find_all('link') if not link.get('href') in self.bad_type and not link.get('href').startswith('#') and not link.get('href').startswith('http')]
		script_files = [link.get('src') for link in self.soup.find_all('script') if not link.get('src') in self.bad_type and not link.get('src').startswith('#') and not link.get('src').startswith('http')]

		# remove duplicates from the lists of elements
		html_files = list(dict.fromkeys(html_files))
		img_files = list(dict.fromkeys(img_files))
		css_files = list(dict.fromkeys(css_files))
		script_files = list(dict.fromkeys(script_files))

		return html_files, img_files, css_files, script_files

	def user_search(self, **filtres):
		self.tag_name = filtres['tagname']
		self.class_name = filtres['classname']
		self.id_name = filtres['id']

		if self.tag_name != None:
			tags_name = [tag_name for tag_name in self.soup.find_all(self.tag_name)]
		
		if self.class_name != None:
			pass

	def find_script(self):
		pass



class filemanager():
	""" files mangement process will be here """
	def __init__(self, elements):
		self.elements = elements

	def build_directorys(self, path):
		directory = []
		for element in self.elements:
			if not element.startswith('http'):
				slicing = element.split('/')
				file_name = slicing.pop()
				directory.append('/'.join(slicing))

		# remove duplicates from the lists of elements && sorted by length
		directory = list(dict.fromkeys(directory))
		directory.sort(key=len)

		os.chdir(path)
		for _dir in directory:
			if _dir != '':
				os.makedirs(_dir)
		print(directory)

def download(url, path):
	elements = []
	searcher = searching(url)
	html_files, img_files, css_files, script_files = searcher.all_files()
	elements.extend(html_files)
	elements.extend(img_files)
	elements.extend(css_files)
	elements.extend(script_files)
	manager = filemanager(elements)
	manager.build_directorys(path)
	os.chdir(path)
	print(elements)
	for file in elements:
		url = url + file
		re = requests.get(url).content
		with open(file, 'wb') as f: # create file
			f.write(re)

def parse():
	parser = argparse.ArgumentParser(description=__description__)
	parser.add_argument('-a', '--all', help='search in all file of the site', action='store_true')
	parser.add_argument('-s', '--script', help='get all script file from the site', action='store_true')
	parser.add_argument('-f', '--file', help='get file from the site', action='store_true')
	parser.add_argument('-o', '--output', help='Save the results to text file')
	parser.add_argument('-tn', '--tag-name', help='filtre to search ', type=str)
	parser.add_argument('-cn', '--class-name', help='filtre to search ', type=str)
	parser.add_argument('-id', help='filtre to search', type=str)
	parser.add_argument('-t', '--text', help='print result without tags and heading information only the text', action='store_true')
	parser.add_argument('-p', '--post', help='post data to the site', type=str)
	parser.add_argument('-g', '--get', help='get data from the site', type=str)
	parser.add_argument('-d', '--download', help='download file from the site', type=str)
	parser.add_argument('url', help='url of the site url shoul start with http:// or https://', type=str)
	return parser.parse_args()
	

def Qget():
	args = parse()
	search = searching(args.url)
	download(args.url, args.output)


if __name__ == '__main__':
	Qget()




