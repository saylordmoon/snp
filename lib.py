#!/usr/bin/env python

import os
import subprocess
from datetime import datetime

DEFAULT_PREFIX = "SNP-"
DATE_FORMAT = "%Y-%m-%d_%H%M%S"

def run(cmd):
	result = ""
	try:
		result = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)    
	except subprocess.CalledProcessError as e:
		result = str(e.output)
	return result 

def directoryExists(name):
	if os.path.exists(name):
		return True
	return False

def createDirectory(name):
	run("mkdir " + name)

def createFile(name):
	run("touch " + name)

def createFileWithText(name,text):
	if not os.path.isfile(name):
		f = open(name,'w')
		f.write(text)
		f.close()
	return text

def generateDirectoryName(prefix = DEFAULT_PREFIX):
	return prefix + datetime.strftime(datetime.now(),DATE_FORMAT)

def generateDirectory():
	name = generateDirectoryName()
	if (directoryExists(name)):
		name = generateDirectoryName()
	createDirectory(name)
	return name

def generateDirectoryStructure(title='',content=''):
	id = generateDirectory()
	createFileWithText ( id + "/id" 	 	, id      )
	createFileWithText ( id + "/title" 		, title   )
	createFileWithText ( id + "/content"	, content )
	createFile ( id + "/tag"   )
	createFile ( id + "/order" )
	return id

def new(title='',content=''):
	id = generateDirectoryStructure(title,content)
	return id

def vim(file):
	if (file != ''):
		subprocess.call(['vim',file])

def getTitle(id):
	return run("cat " + id + "title")

def getContent(id):
	return run("cat " + id + "content")

def listAll():
	ids = run("ls -d */").strip().split('\n')
	snippets = []
	for id in ids:
		snippets.append({ 	'id'		: id , 
							'title'		: getTitle(id), 
							'content'	: getContent(id) })
	return snippets

def searchInDict(keyword, snippets):
	search = [];
	for snippet in snippets:
		for value in snippet.values():
			if (keyword.lower() in value.lower()):
				search.append(snippet)
	return search

def listAllKeyword(keyword):
	snippets = listAll()
	return searchInDict(keyword,snippets)

def searchInKeyInDict(keyword,key,snippets):
	search = []
	for snippet in snippets:
		if (keyword.lower() in snippet[key].lower()):
			search.append(snippet)
	return search

def listTitle(keyword):
	snippets = listAll()
	return searchInKeyInDict(keyword,'title',snippets)

def listContent(keyword):
	snippets = listAll()
	return searchInKeyInDict(keyword,'content',snippets)

def listId(keyword):
	snippets = listAll()
	return searchInKeyInDict(keyword,'id',snippets)


# subprocess.call(['vim',name + '/title'])
# subprocess.call(['vim',name + '/content'])


