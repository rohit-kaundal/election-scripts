# author : Rohit Kaundal
# GUI code for the app
# Pure App and GUI init not to be touched with business logic

import wx
import MainForm as MainWindow


def main():
	app = wx.App()
	frame = MainWindow.MainDlg(parent=None)
	frame.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()
