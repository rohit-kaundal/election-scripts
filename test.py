# Test file
# author: Rohit Kaundal

import pandas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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

    initPyDrive()

if __name__ == '__main__':
    main()
