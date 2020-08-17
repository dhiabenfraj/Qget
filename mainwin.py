#! /usr/bin/env python3
from getsitescript import GetSite

url = 'https://krx404.github.io/'

gs = GetSite(url)
pages, images, styles, scripts, sitelinks = gs.FindAllElement()
# print(pages, images, styles, scripts, sitelinks)

# print('\n\n', images)

files_url, directorie_paths = gs.AllDirPath(pages, images, styles, scripts)
print(files_url)
print('\n\n', directorie_paths)
# import requests
# import bs4
# text = requests.get('https://krx404.github.io').text
# soup = bs4.BeautifulSoup(text, features='html.parser')
# scripts = soup.find_all('script')
# for s in scripts:
# 	if 'src' in s.attrs:
# 		if not s['src'].startswith('http'):
# 			print(s['src'])


# print(scripts[])
# srcs = [link['src'] for link in scripts if 'src' in link.attrs]
# print(srcs)

