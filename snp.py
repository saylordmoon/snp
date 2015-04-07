#!/usr/bin/env python

""" Snippet.

Usage:
  snp.py new 
  snp.py new <title>
  snp.py new <title> <content>
  snp.py all
  snp.py all <keyword>
  snp.py title <keyword>
  snp.py content <keyword>
  snp.py subject <keyword>
  snp.py id <id>
"""

from docopt import docopt
import lib

def main():
	arguments = docopt(__doc__, version='Snippet 0.01')

	if (arguments['new']):
		title   = arguments['<title>']
		content = arguments['<content>']
		if (title == None):	  title   = ''
		if (content == None): content = ''
		id = lib.new(title,content)
		if (title == ''):   lib.vim(id + '/title')
		if (content == ''): lib.vim(id + '/content')

	elif (arguments['all']):
		if (arguments['<keyword>'] == None):
			print lib.listAll()
		else:
			keyword =arguments['<keyword>']
			print lib.listAllKeyword(keyword)

	elif (arguments['title']):
		keyword =arguments['<keyword>']
		print lib.listTitle(keyword)

	elif (arguments['content']):
		keyword =arguments['<keyword>']
		print lib.listContent(keyword)

	elif (arguments['id']):
		keyword =arguments['<keyword>']
		print lib.listId(keyword)

if __name__ == '__main__':
	main()