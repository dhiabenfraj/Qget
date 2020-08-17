#!/usr/bin/env python3

''' made by xreaad '''
''' Copyright © xreaad '''

from bs4 import BeautifulSoup
import requests

def GetPic(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')
	pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') and page['href'] != '#']
	pages = list(dict.fromkeys(pages))
	images = []
	for page in pages:
		_url = url + page
		re = requests.get(_url).text
		soup = BeautifulSoup(re, 'html.parser')
		_images = [img.get('src') for img in soup.findAll('img') if not img.get('src').startswith('http')]
		images.extend(_images)
	images = list(dict.fromkeys(images))
	return images


def GetPage(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')
	pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') and page['href'] != '#']	
	pages = list(dict.fromkeys(pages))
	all_pages = []
	for page in pages:
		_url = url + page
		re = requests.get(_url).text
		soup = BeautifulSoup(re, 'html.parser')
		_pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') if page['href'] != '#']
		print(_pages)
		all_pages.extend(_pages)
	pages = list(dict.fromkeys(all_pages))
	print(pages)
	return pages


def GetStyle(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')
	pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') and page['href'] != '#']
	pages = list(dict.fromkeys(pages))
	styles = []
	for page in pages:
		url = url + page
		re = requests.get(url).text
		soup = BeautifulSoup(re, 'html.parser')
		for page in pages:
			pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') if page['href'] != '#' if not page['href'] in pages]
			_styles = [link["href"] for link in soup.findAll("link") if "stylesheet" in link.get("rel", []) if not link['href'].startswith('http')]
			styles.extend(_styles)
	styles = list(dict.fromkeys(styles))
	return styles


def GetScript(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')
	pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') and page['href'] != '#']
	pages = list(dict(fromkeys(pages)))
	scripts = []
	for page in pages:
		url = url + page
		re = requests.get(url).text
		soup = BeautifulSoup(re, 'html.parser')
		for page in pages:
			pages = [page['href'] for page in soup.find_all('a') if not page['href'].startswith('http') if page['href'].endswith('.html') if page['href'] != '#' if not page['href'] in pages]
			_scripts = [script['src'] for script in soup.findAll('script') if 'src' in script.attrs if not script['src'].startswith('http') if not script['src'].startswith('//')]
			scripts.extend(_scripts)
	scripts = list(dict.fromkeys(scripts))
	return scripts



def PageItem(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')

	onestyles = [link["href"] for link in soup.findAll("link") if "stylesheet" in link.get("rel", []) if not link['href'].startswith('http')]
	onescripts = [script['src'] for script in soup.findAll('script') if 'src' in script.attrs if not script['src'].startswith('http') if not script['src'].startswith('//')]
	oneimages = [img.get('src') for img in soup.findAll('img') if not img.get('src').startswith('http')]

	# remove diplicated 
	onestyles = list(dict.fromkeys(onestyles))
	onescripts = list(dict.fromkeys(onescripts))
	oneimages = list(dict.fromkeys(oneimages))

	return onestyles, onescripts, oneimages


def AllLinks(url):
	sitelinks = []
	links = []

	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')

	html = [page['href'] for page in soup.find_all('a')]
	css = [style['href'] for style in soup.find_all('link')]
	js = [script['src'] for script in soup.find_all('script') if 'src' in script.attrs]
	img = [img['src'] for img in soup.find_all('img')]

	sitelinks.extend(html)
	sitelinks.extend(css)
	sitelinks.extend(js)
	sitelinks.extend(img)

	sitelinks = list(dict.fromkeys(sitelinks))

	if url.endswith('/'):
		url = url
	else:
		url = url + '/'

	for link in sitelinks:
		if link.startswith('http'):
			links.append(link)
		else:
			link = url + link
			links.append(link)
	
	return links

def PageLinks(url):
	re = requests.get(url)
	soup = BeautifulSoup(re.content, 'html.parser')
	pages = []
	for link in soup.find_all('a'):
		if not link['href'].startswith('http'):
			pages.append(link['href'])
	for link in pages:
		_url = url + link
		re = requests.get(_url)
		soup = BeautifulSoup(re.content, 'html.parser')
		for a in soup.find_all('a'):
			if not a['href'].startswith('http'):
				pages.append(a['href'])

