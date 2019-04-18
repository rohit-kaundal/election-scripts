# author : Rohit Kaundal
# GUI code for the app

import wx

def main():
    app = wx.App()
    frame = wx.Frame(parent=None, title='TCC Rocks')
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
