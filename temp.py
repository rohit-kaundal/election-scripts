## Temp file to test and code snippets
## Author : Rohit Kaundal
##

import datefinder
import datetime

def getStringDate(strDate):
	strTmp = strDate
	dateExtract = list(datefinder.find_dates(strTmp))
	#print(dateExtract[0])
	try:
		resultDate = datetime.datetime.strftime(dateExtract[0], '%d %B %Y')
		return resultDate
	except:
		return ""

def main():

	print(getStringDate("2019-04-23T10:44:21+0000"))

if __name__ == '__main__':
	main()

