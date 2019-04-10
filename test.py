# Test file
# author: Rohit Kaundal

import pandas


def loadXl(filename):
    xl = pandas.read_excel(filename, sheet_name="Advertisements")
    return xl

def main():
    adsFile = loadXl("ads.xlsx")
    print(adsFile.keys())

if __name__ == '__main__':
    main()
