#!/usr/bin/env python3

''' made by xreaad '''
''' Copyright © xreaad '''

from get import *
from filemanager import *
import os
import sys
import logo
from colorama import *
from time import sleep
import requests

# colorama color
red = '\033[91m'
blue = '\033[94m'
green = '\033[92m'
purple = '\033[35m'
yellow = '\033[93m'
white = '\033[00m'

# colorama font : bold
bold = '\033[01m'

# simple intro to put some cool feedback in the feeling of user (feeling like a hacker xD)
os.system('clear')

with open('assets/intro1.txt') as intro:
	for line in intro:
		print(line, end='')
		sleep(0.05)

os.system('clear')

with open('assets/intro2.txt') as f:
	for line in f:
		print(line, end='')
		sleep(0.05)

os.system('clear')

# Logo of the tool
logo.intro()

# default input command
command = f'{bold}{red}[{green}&&{red}]{blue} Get Site Script : {yellow}' 

# function command
def fcommand(fname):
	''' arg = function name & return command inside function'''
	return f'{bold}{red}[{green}& Get Site Script &{red}]{blue} {fname} : {yellow}'

# site error
def serror():
	print(f'{red}\tThis site is not aviable !')

# derectorie error
def changedir(directorie):
	try:
		os.chdir(directorie)
	except Exception:
		print(f'{red}\tCheck tha directorie path & try again')
		main()


# default function error connection
def checkconnction(url):
	try:
		re = requests.get(url)
	except Exception:
		print(f'{red}\tCheck your connection or the url & try again !')
		main()


def editurl(url):
	""" edit the url to get the request without error """

	if url.startswith('https'):
		_url = url[8:]
		_url_list = _url.split('/')
		_url_list = list(filter(None, _url_list))
		url = 'https://' + '/'.join(_url_list) + '/'
		return url

	elif url.startswith('http'):
		_url = url[7:]
		_url_list = _url.split('/')
		_url_list = list(filter(None, _url_list))
		url = 'http://' + '/'.join(_url_list) + '/'
		return url

	else:
		print(f'{red}Check the url & try again ! should start with http or https !')
		main()

def einput():
	''' error input '''
	print(f'{red}\tInput the number of the option next time !')

def clear():
	os.system('clear')
	logo.intro()

def exit():
	''' exit from the tool'''
	os.system('clear')
	sys.exit() 
def main():
	''' main function of tool '''

	# input the option with handling the error
	while True:
		try:
			option = int(input(command))
		except ValueError:
			print(f'{red}input a value from the option !')
		else:
			break

	# call the function case of option
	if option == 0:
		exit()
	elif option == 1:
		GetAllLinks()
	elif option == 2:
		GetAllImage()
	elif option == 3:
		GetAllPage()
	elif option == 4:
		GetAllStyle()
	elif option == 5:
		DownloadImage()
	elif option == 6:
		DownloadVideo()
	elif option == 7:
		DownloadPage()
	elif option == 8:
		DownloadAllSite()
	elif option == 9:
		clear()
	else:
		einput()


def GetAllLinks():
	''' retrive all links from the site '''

	command = fcommand('Get all link')
	url = input(f'{command}{blue}\n\tSite Url :{yellow} ')
	checkconnction(url)
	
	print(f'\t{red}[{blue}1{red}]{yellow} Put The Links File Url In File .txt {green}')
	print(f'\t{red}[{blue}2{red}]{yellow} Print Them Here {green}')
	print(f'\t{red}[{blue}0{red}]{yellow} Back {green}')

	order = int(input(f'{command}'))

	while True:
		try:
			links = AllLinks(url)
		except Exception:
			serror()
			break

		if order == 1:
			directorie = input(f'{blue}\tDirectorie Path When Put The File ".txt" :{yellow} ')
			changedir(directorie)
			with open('links.txt', 'w') as f:
				for line in links:
					f.write(f'{line}\n')
				break

		elif order == 2:
			for line in links:
				print(f'{red}\t[{green}LINK{red}]{white} {line}')
			break

		else:
			main()

	main()


def GetAllImage():
	''' Get all image links from the site '''

	command = fcommand('Get All Image Links')
	url = input(f'{command}{blue}\n\tSite Url :{yellow} ')
	
	checkconnction(url)

	print(f'\t{red}[{blue}1{red}]{yellow} Put The Style File Url In File .txt {green}')
	print(f'\t{red}[{blue}2{red}]{yellow} Print Them Here {green}')
	print(f'\t{red}[{blue}0{red}]{yellow} Back {green}')

	order = int(input(f'{command}'))
	
	while True:
		images = GetPic(url)

		ListImages = []
		url = editurl(url)

		for image in images:
			image_url = url + image
			ListImages.append(image_url)

		if order == 1:
			directorie = input(f'{blue}\tDirectorie Path When Put The File ".txt" :{yellow} ')
			changedir(directorie)

			with open('ImageLinks.txt', 'w') as f:
				for line in ListImages:
					f.write(f'{line}\n')
			break

		elif order == 2:
			for line in ListImages:
				print(f'{red}  [{green}LINK{red}]{white} {line}')

			print(f'{red}  [{green}DONE{red}]{yellow}...')
			break

		elif order == 0:
			main()
		else:
			einput()
			break

	main()


def GetAllPage():
	''' retrive all Html file from the site '''

	command = fcommand('Get All HTML File')
	url = input(f'{command}{blue}\n\tSite Url :{yellow} ')
	checkconnction(url)

	print(f'\t{red}[{blue}1{red}]{yellow} Put The Links File Url In File .txt {green}')
	print(f'\t{red}[{blue}2{red}]{yellow} Print Them Here {green}')
	print(f'\t{red}[{blue}0{red}]{yellow} Back {green}')
	order = int(input(f'{command}'))
	
	while True:
		pages = GetPage(url)
		ListPages = []
		url = editurl(url)
	
		for page in pages:
			page_url = url + page
			ListPages.append(page_url)

		if order == 1:
			directorie = input(f'{blue}\tDirectorie Path When Put The File ".txt" :{yellow} ')
			changedir(directorie)
			with open('PageLinks.txt', 'w') as f:
				for line in ListPages:
					f.write(f'{line}\n')
			break
		
		elif order == 2:	
			
			for line in ListPages:
				print(f'{red}\t[{green}LINK{red}]{white} {line}')
			
			print(f'{red}\t[{green}DONE{red}]{yellow} ...')
			break
		
		elif order == 0:
			break
		
		else:
			einput()		
			break

	main()

def GetAllStyle():
	''' retrive all style file from the site '''

	command = fcommand('Get All Style File')
	url = input(f'{command}{blue}\n\tSite Url :{yellow} ')
	checkconnction(url)

	print(f'\t{red}[{blue}1{red}]{yellow} Put The Links File Url In File .txt {green}')
	print(f'\t{red}[{blue}2{red}]{yellow} Print Them Here {green}')
	print(f'\t{red}[{blue}0{red}]{yellow} Back {green}')
	order = int(input(f'{command}'))

	while True:
		pages = GetStyle(url)
		ListStyle = []
		url = editurl(url)
	
		for page in pages:
			page_url = url + page
			ListStyle.append(page_url)

		if order == 1:
			directorie = input(f'{blue}\tDirectorie Path When Put The File ".txt" :{yellow} ')
			changedir(directorie)
			with open('PageLinks.txt', 'w') as f:
				for line in ListStyle:
					f.write(f'{line}\n')
			break
		
		elif order == 2:	
			
			for line in ListStyle:
				print(f'{red}\t[{green}LINK{red}]{white} {line}')
			
			print(f'{red}\t[{green}DONE{red}]{yellow} ...')
			break
		
		elif order == 0:
			break
		
		else:
			einput()		
			break

	main()


def DownloadImage():
	command = fcommand('Download Image')
	url = input(f'{command}{blue}\n\tImage Url :{yellow} ')
	checkconnction(url)
	directorie = input(f'{blue}\tPath Of The Directorie When Save The Image :{yellow} ')
	changedir(directorie)
	re = requests.get(url).content
	image_name = url.split('/').pop()
	
	if not image_name.endswith('.jpg'):# and not image_name.endswith('.png'):
		image_name += '.jpg'

	with open(image_name, 'wb') as f:
		f.write(re)
	


def DownloadVideo():
	command = fcommand('Download Video')
	url = input(f'{command}{blue}\n\tVideo Url :{yellow} ')
	checkconnction(url)
	directorie = input(f'{blue}\tPath Of The Directorie When Save The Video :{yellow} ')
	changedir(directorie)
	re = requests.get(url).content

	video_name = url.split('/').pop()
	
	if not video_name.endswith('.mp4'):
		video_name += '.mp4'
	
	with open(video_name, 'wb') as f:
		f.write(re)
	

def DownloadPage():
	command = fcommand('Download Page')
	url = input(f'{command}{blue}\n\tPage Url :{yellow} ')
	checkconnction(url)
	
	try:
	         onestyles, onescripts, oneimages = PageItem(url)
	except Exception:
		serror()

	directorie = input(f'{blue}\tPath Of The Directorie When Save The Video :{yellow} ')
	changedir(directorie)
	alldir, allfile = Getallpath(onestyles, onescripts, oneimages)
	builddir(alldir)

	if url.endswith('/'):
		re = requests.get(url).content
		with open('indx.html', 'wb') as f:
			f.write(re)
	else:
		name = url.split('/').pop()
		re = requests.get(url).content
		with open(name, 'wb') as f:
			f.write(re)

	for item in allfile:
		url = editurl(url)
		_url = url + item
		re = requests.get(_url).content
		with open(item, 'wb') as f:
			f.write(re)

def DownloadAllSite():
        pass	 

if __name__ == '__main__':
	while True:
		main()
