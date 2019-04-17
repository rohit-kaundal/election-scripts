# Test file
# author: Rohit Kaundal

import pandas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from selenium import webdriver
import time
import urllib3
import requests


def fbSearchAds(srchTerm):
    token = 'EAAgzFO2gyWoBABwnTZA5MEvv0BcbXKX8ictg9yWgeJDcyTI3d8wOAgF0JBgviwGYZBPRSaddFMZATLyatLPbxYDB5WJ93m7XGDY58q0NLZAtjYhfDe2ZC2wyghFXyDBCcHZCCGIqLYj6HeZCf6GWP1v6XdhsS0gORECiDX5XnRDHava91llovjxPYNmf0yUr2VAHB9VZCZB3zeJDYnnaQEtW3'
    graphUrl = f'https://graph.facebook.com/v3.2/ads_archive?search_terms={srchTerm}&ad_type=POLITICAL_AND_ISSUE_ADS&ad_reached_countries=[\'IN\']&fields=page_id,page_name,ad_creative_link_title,ad_creative_body,ad_snapshot_url,currency,funding_entity,spend,ad_delivery_start_time,ad_delivery_stop_time&access_token={token}'

    ads = requests.get(graphUrl)

    adsJson = ads.json()
    print(adsJson)

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

def main():
    # adsFile = loadXl("ads.xlsx")
    # print(adsFile.keys())

    #initPyDrive()
    # getScreenShot('https://www.facebook.com/ads/archive/render_ad/?id=2324960561053902&access_token=EAAgzFO2gyWoBABrf9BmZBNwYLF4ov2v7LNZCDkBPZAKCp4kk1d0wknYsqFzuVuyOXLFhMBUDUbD6sQvFZBNZBfAmy7VlZClu4rUstNBClETyR9aRTq9KeezinC7uYr3LPADOMinZCdxvFjiyaj52PgQFbzPZADfWrDgRKpIZAO5avbE5xSZCPopyPu3KCKiUIAHFljKUPws9fF2GtYZAs4m39ZB9', 'test.png')

    fbSearchAds('Sanjay Tandon')

if __name__ == '__main__':
    main()
