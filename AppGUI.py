# author : Rohit Kaundal
# GUI code for the app

import wx
import noname as MainWindow

def main():
    app = wx.App()
    frame = MainWindow.MainDlg(parent=None)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
