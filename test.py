# Test file
# author: Rohit Kaundal

import pandas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from selenium import webdriver
import time
import urllib3
import requests
import json
import datetime


def fbSearchAds(srchTerm):
    token = 'EAAgzFO2gyWoBANLZA8RROlZBUNLjXlm6LNsZA7ZAXUmJFIZAEZB9RNSwHnPSDchAq7ugIn42ZAhnlfoN14GpWKDdnCVTnjSXsQ2RZBWgL3bhY8f6zAzpFLfjfSdMaW3qXI1ZB3ZBcd0byZCYG4pdieHmjZC7XkTwgPYIvSmApvOaUlIUxcLvN2E1t8k18bHCkZAYo0SIxuQQFN6pedynZB9ZAZArVu7P'
    graphUrl = f'https://graph.facebook.com/v3.2/ads_archive?search_terms={srchTerm}&ad_active_status=ALL&ad_type=POLITICAL_AND_ISSUE_ADS&ad_reached_countries=[\'IN\']&fields=page_id,page_name,ad_creative_link_title,ad_creative_body,ad_snapshot_url,currency,funding_entity,spend,ad_delivery_start_time,ad_delivery_stop_time&access_token={token}&limit=1000'


    # print(f"[+] Getting ADS related to {srchTerm}...")
    yield f"Getting ADS related to {srchTerm}..."

    try:

        tmpJson = []
        ads = requests.get(graphUrl)

        adsJson = ads.json()
        # for ad in adsJson['data']:
        #     print(f"Ad: {ad}")

        adsData = adsJson['data']

        for row in adsData:

            tmpJson.append({
                'Page ID': row['page_id'],
                'Page Name': row.get('page_name', 'Not Found'),
                'AD Content': row.get('ad_creative_body', 'Not Found'),
                'AD Link': row['ad_snapshot_url'],
                'Spending': f"{row['currency']} {row['spend']['lower_bound']}/- to {row['currency']} {row['spend']['upper_bound']}/- ",
                'Ad Funding Entity': row.get('funding_entity', 'SELF'),
                'Ad Start Time': row['ad_delivery_start_time'],
                'Ad Stop Time': row.get('ad_delivery_stop_time', 'ACTIVE')
            })


        df = pandas.DataFrame.from_dict(tmpJson)

        writer = pandas.ExcelWriter(f"{srchTerm}.xlsx", engine='xlsxwriter', options={'strings_to_urls': False})
        df.to_excel(writer, sheet_name='ADS')
        wbook = writer.book
        wsheet = writer.sheets['ADS']
        text_format = wbook.add_format({'text_wrap': True})
        new_format = wbook.add_format()
        new_format.set_align('center')
        new_format.set_align('vcenter')
        new_format.set_text_wrap()

        wsheet.set_column('B:B', 60, new_format)
        wsheet.set_column('C:C',60 , new_format)
        wsheet.set_column('D:D',20 , new_format)
        wsheet.set_column('E:E',25 , new_format)
        wsheet.set_column('F:F',25 , new_format)
        wsheet.set_column('G:G',25 , new_format)
        wsheet.set_column('H:H',25 , new_format)
        wsheet.set_column('I:I',25 , new_format)
        # wsheet.set_default_row(20)
        writer.save()
        # print(f"[+] Dumped file : {srchTerm}.xlsx")
        yield f"Dumped file : {srchTerm}.xlsx"
    except Exception as e:
        # print(f"[!] Error occured: {e}")
        yield f"[!] Error occured: {e}"

def getScreenShot(url, scrName):
    DRIVER = r'C:\Program Files (x86)\Common Files\chromedriver_win32\chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=selenium")  # this is the directory for the cookies

    driver = webdriver.Chrome(executable_path=DRIVER,options=chrome_options)
    #driver = webdriver.Chrome(DRIVER)

    driver.get(url)
    driver.fullscreen_window()

    cookies = [{"name":"locale","value":"en_US"},{"name":"c_user","value":"100001058641023"},{"name":"presence","value":"EDvF3EtimeF1555505493EuserFA21B01058641023A2EstateFDutF1555505491344CC"}]
    #print(driver.get_cookies())
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

    #initPyDrive()
    # getScreenShot('https://www.facebook.com/ads/archive/render_ad/?id=2324960561053902&access_token=EAAgzFO2gyWoBABrf9BmZBNwYLF4ov2v7LNZCDkBPZAKCp4kk1d0wknYsqFzuVuyOXLFhMBUDUbD6sQvFZBNZBfAmy7VlZClu4rUstNBClETyR9aRTq9KeezinC7uYr3LPADOMinZCdxvFjiyaj52PgQFbzPZADfWrDgRKpIZAO5avbE5xSZCPopyPu3KCKiUIAHFljKUPws9fF2GtYZAs4m39ZB9', 'test.png')

    # fbSearchAds('Sanjay Tandon')
    # fbSearchAds('BJP Chandigarh')
    # fbSearchAds('Kirron Kher')
    # fbSearchAds('Satya Pal Jain')
    # fbSearchAds('Indian National Congress - Chandigarh')
    # fbSearchAds('Pawan Kumar Bansal')
    # fbSearchAds('NSUI Chandigarh.')
    # fbSearchAds('Chandigarh Youth Congress')
    # fbSearchAds('Navjot Sidhu')
    # fbSearchAds('Harmohan Dhawan, Former Union Minister, Govt. of India')
    # fbSearchAds('Aam Aadmi Party - Chandigarh')
    # fbSearchAds('Fans Of Harmohan Dhawan')
    # fbSearchAds('Avinash Singh Sharma')
    # fbSearchAds('Saraansh Tandon')

    ### Yield Test

    for progress in progressBarTest():
        print(f"[+]{progress}")

if __name__ == '__main__':
    main()
