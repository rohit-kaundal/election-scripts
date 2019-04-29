# Test file
# author: Rohit Kaundal

import pandas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from selenium import webdriver
import time
import requests
import datefinder
import datetime
import os


def makeDir(strDirName):
	os.makedirs(strDirName, exist_ok=True)

def getStringDate(strDate):
	strTmp = strDate
	dateExtract = list(datefinder.find_dates(strTmp))
	#print(dateExtract[0])
	try:
		resultDate = datetime.datetime.strftime(dateExtract[0], '%d %B %Y')
		return resultDate
	except:
		return "ACTIVE"


def fbSearchAds(srchTerm, strToken):
	# token = 'EAAgzFO2gyWoBABXxICh9hHZAZCmud0g7PSZCYVN9sxtqDSMHzaAGXOWR6Js1niZCyemfK7EdwG8E7aU9Ey2UKZAVyvMLnbjrHwnF8o78iCXK3yVwgCfDc5qUKfZBVnACdUS1VQV7sKD1o8eQjxPRfp011m20qLQf4gGZAPUI1dCfL46NUAonFe8KXXdScSQgaMKjQa61YXneKokOnz6LTjr'
	token = strToken
	graphUrl = f'https://graph.facebook.com/v3.2/ads_archive?search_terms={srchTerm}&ad_active_status=ALL&ad_type=POLITICAL_AND_ISSUE_ADS&ad_reached_countries=[\'IN\']&fields=page_id,page_name,ad_creative_link_title,ad_creative_body,ad_snapshot_url,currency,funding_entity,spend,ad_delivery_start_time,ad_delivery_stop_time,region_distribution&access_token={token}&limit=1000'

	print(f"[+] Getting ADS related to {srchTerm}...")
	yield f"Getting ADS related to {srchTerm}..."

	try:

		tmpJson = []
		ads = requests.get(graphUrl)

		adsJson = ads.json()
		# for ad in adsJson['data']:
		#     print(f"Ad: {ad}")

		adsData = adsJson['data']

		for row in adsData:
			# demographicDistribution = f"{row['region_distribution']}"
			demographicDistribution = ", ".join(map(lambda regdis: f"{regdis['region']}", row['region_distribution']))
			# print(demographicDistribution)
			tmpJson.append({
				'Page ID': row['page_id'],
				'Page Name': row.get('page_name', 'Not Found'),
				'AD Content': row.get('ad_creative_body', 'Not Found'),
				'AD Link': row['ad_snapshot_url'],
				'Spend Low Limit': row['spend']['lower_bound'],
				'Spend Upper Limit': row['spend']['upper_bound'],
				'Spending': f"{row['currency']} {row['spend']['lower_bound']}/- to {row['currency']} {row['spend']['upper_bound']}/- ",
				'Ad Funding Entity': row.get('funding_entity', 'SELF'),
				'Ad Start Time': row['ad_delivery_start_time'],
				'Ad Stop Time': row.get('ad_delivery_stop_time', 'ACTIVE'),
				'Region': demographicDistribution
			})

		df = pandas.DataFrame.from_dict(tmpJson)

		# df['Ad Start Time'] = pandas.to_datetime(df['Ad Start Time'], format='%Y-%m-%dT%H:%M:%S+0000')
		# df['Ad Stop Time'] = pandas.to_datetime(df['Ad Stop Time'], format='%Y-%m-%dT%H:%M:%S+0000')

		df = df.sort_values(by=['Ad Start Time'])
		df.reindex()
		df['Ad Start Time'] = df['Ad Start Time'].apply(lambda strDate: getStringDate(strDate))
		df['Ad Stop Time'] = df['Ad Stop Time'].apply(lambda strDate: getStringDate(strDate))

		writer = pandas.ExcelWriter(f"./ADS Output/{srchTerm}.xlsx", engine='xlsxwriter',
									options={'strings_to_urls': False})
		df.to_excel(writer, sheet_name='ADS')
		wbook = writer.book
		wsheet = writer.sheets['ADS']
		text_format = wbook.add_format({'text_wrap': True})
		new_format = wbook.add_format()
		new_format.set_align('center')
		new_format.set_align('vcenter')
		new_format.set_text_wrap()

		wsheet.set_column('A:A', None, None, {'hidden': True})
		wsheet.set_column('B:B', 60, new_format)
		wsheet.set_column('C:C', 60, new_format)
		wsheet.set_column('D:D', 20, new_format)
		wsheet.set_column('E:E', 25, new_format)
		wsheet.set_column('F:F', 25, new_format)
		wsheet.set_column('G:G', 25, new_format)
		wsheet.set_column('H:H', 25, new_format)
		wsheet.set_column('I:I', 25, new_format)
		wsheet.set_column('J:J', 25, new_format)
		wsheet.set_column('K:K', 25, new_format)
		wsheet.set_column('L:L', 25, new_format)


		wsheet.set_default_row(hide_unused_rows=True)

		writer.save()
		print(f"[+] Dumped file : {srchTerm}.xlsx")
		yield f"Dumped file : {srchTerm}.xlsx"
	except Exception as e:
		print(f"[!] Error occured: {e}")
		yield f"[!] Error occured: {e}"


def getScreenShot(url, scrName):
	DRIVER = r'C:\Program Files (x86)\Common Files\chromedriver_win32\chromedriver.exe'
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("user-data-dir=selenium")  # this is the directory for the cookies

	driver = webdriver.Chrome(executable_path=DRIVER, options=chrome_options)
	# driver = webdriver.Chrome(DRIVER)

	driver.get(url)
	driver.fullscreen_window()

	cookies = [{"name": "locale", "value": "en_US"}, {"name": "c_user", "value": "100001058641023"},
			   {"name": "presence", "value": "EDvF3EtimeF1555505493EuserFA21B01058641023A2EstateFDutF1555505491344CC"}]
	# print(driver.get_cookies())
	# return
	#  for c in cookies:
	#      driver.add_cookie(c)

	screenshot = driver.get_screenshot_as_file(scrName)

	driver.quit()
	print(f"[+] Screen shot captured {scrName}")


def initPyDrive():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	drive = GoogleDrive(gauth)


def loadXl(filename):
	xl = pandas.read_excel(filename, sheet_name="Advertisements")
	return xl


def progressBarTest():
	yield "Downloading Started"
	x = 10
	time.sleep(1)
	yield "Downloading under process..."
	time.sleep(1)
	yield "Downloading Complete"
	return


def main():
	# adsFile = loadXl("ads.xlsx")
	# print(adsFile.keys())

	# initPyDrive()
	# getScreenShot('https://www.facebook.com/ads/archive/render_ad/?id=2324960561053902&access_token=EAAgzFO2gyWoBABrf9BmZBNwYLF4ov2v7LNZCDkBPZAKCp4kk1d0wknYsqFzuVuyOXLFhMBUDUbD6sQvFZBNZBfAmy7VlZClu4rUstNBClETyR9aRTq9KeezinC7uYr3LPADOMinZCdxvFjiyaj52PgQFbzPZADfWrDgRKpIZAO5avbE5xSZCPopyPu3KCKiUIAHFljKUPws9fF2GtYZAs4m39ZB9', 'test.png')
	fbSearchAds('Sanjay Tandon')
	fbSearchAds('BJP Chandigarh')
	fbSearchAds('Kirron Kher')
	fbSearchAds('Satya Pal Jain')
	fbSearchAds('Indian National Congress - Chandigarh')
	fbSearchAds('Pawan Kumar Bansal')
	fbSearchAds('NSUI Chandigarh.')
	fbSearchAds('Chandigarh Youth Congress')
	fbSearchAds('Navjot Sidhu')
	fbSearchAds('Harmohan Dhawan, Former Union Minister, Govt. of India')
	fbSearchAds('Aam Aadmi Party - Chandigarh')
	fbSearchAds('Fans Of Harmohan Dhawan')
	fbSearchAds('Avinash Singh Sharma')
	fbSearchAds('Devi Sirohi')

	### Yield Test
	#
	# for progress in progressBarTest():
	#     print(f"[+]{progress}")


if __name__ == '__main__':
	main()
