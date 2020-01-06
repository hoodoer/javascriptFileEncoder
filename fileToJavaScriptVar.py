#!/usr/bin/python3
#
#
# Simple tool to take an arbitrary binary (DLL, exe, etc.) 
# and convert it to a JavaScript var for including in 
# XSS Session Riding Payloads 
#
# Drew Kirkpatrick
# drew.kirkpatrick@gmail.com
# @hoodoer
#



import argparse
import subprocess
import sys
import os



def generateCharEncoding(filename):
	outputEncoding = subprocess.check_output(['xxd', '-i', filename])

	return outputEncoding.decode()



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--filename", help="the file to encode (DLL, exe, php, zip, etc) as a JavaScript var")
	args = parser.parse_args()

	if len(sys.argv) < 3:
		parser.print_help()
		sys.exit()

	print ("Converting file into JavaScript friendly hex...")
	print

	
	cArray = generateCharEncoding(args.filename)


	# Change the C format to JavaScript format
	# wonky ass code alert!
	javaScriptArray = cArray.replace("0x", "\\x")
	javaScriptArray = javaScriptArray.replace(", ", "")
	javaScriptArray = javaScriptArray.replace("  ", "'")
	javaScriptArray = javaScriptArray.replace(",", "' +")

	javaScriptList = javaScriptArray.splitlines()

	# First line....
	javaScriptData = "var fileData = " + javaScriptList[1]

	# Closing line of data
	javaScriptList[len(javaScriptList)-3] += "';"

	# Loop through the rest...
	for i in range(2, len(javaScriptList)-2, 1):
		javaScriptData += "\n" + javaScriptList[i]


	print (javaScriptData)



