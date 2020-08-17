#!/usr/bin/env python3

''' made by xreaad '''
''' Copyright © xreaad '''

import os

def Getallpath(styles, images, scripts):
	allfile = []
	alldir = []

	allfile.extend(styles)
	allfile.extend(images)
	allfile.extend(scripts)

	for path in allfile:
		direcotrie = path.split('/')
		direcotrie.pop()
		direcotrie = '/'.join(direcotrie)
		if direcotrie != '':
			alldir.append(direcotrie)
        
	allfile = list(dict.fromkeys(allfile))
	alldir = list(dict.fromkeys(alldir))

	allfile.sort(key=len)
	alldir.sort(key=len)

	return alldir, allfile

def builddir(alldir):
	for _dir in alldir:
			os.makedirs(_dir)

