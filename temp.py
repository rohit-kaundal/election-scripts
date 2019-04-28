## Temp file to test and code snippets
## Author : Rohit Kaundal
##

import datefinder
import datetime
import os

def makeDir(strDirName):
	os.makedirs(strDirName, exist_ok=True)

def main():

	makeDir("./RohitTest")

if __name__ == '__main__':
	main()

