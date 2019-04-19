# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import time
import datetime
import test as bg
import os
import subprocess


###########################################################################
## Class MainDlg
###########################################################################

class MainDlg(wx.Dialog):

	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=wx.ID_ANY,
						   title=u"MCMC ADS Fetcher Tool v1.0 - Election Comission Chandigarh", pos=wx.DefaultPosition,
						   size=wx.Size(432, 344), style=wx.DEFAULT_DIALOG_STYLE)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.mlblToken = wx.StaticText(self, wx.ID_ANY, u"Facebook GRAPH Api Token", wx.Point(10, 10), wx.DefaultSize,
									   wx.ALIGN_CENTRE)
		self.mlblToken.Wrap(-1)
		bSizer1.Add(self.mlblToken, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.mtxtToken = wx.TextCtrl(self, wx.ID_ANY,
									 u"EAAgzFO2gyWoBANLZA8RROlZBUNLjXlm6LNsZA7ZAXUmJFIZAEZB9RNSwHnPSDchAq7ugIn42ZAhnlfoN14GpWKDdnCVTnjSXsQ2RZBWgL3bhY8f6zAzpFLfjfSdMaW3qXI1ZB3ZBcd0byZCYG4pdieHmjZC7XkTwgPYIvSmApvOaUlIUxcLvN2E1t8k18bHCkZAYo0SIxuQQFN6pedynZB9ZAZArVu7P",
									 wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer1.Add(self.mtxtToken, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.mbtnGetAds = wx.Button(self, wx.ID_ANY, u"Download ADS", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer1.Add(self.mbtnGetAds, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.txtOutput = wx.TextCtrl(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.Size(-1, 400),
									 wx.TE_MULTILINE)
		self.txtOutput.SetEditable(False)
		self.txtOutput.Enable(True)

		bSizer1.Add(self.txtOutput, 1, wx.ALL | wx.EXPAND, 5)
		self.lblCopyRights = wx.StaticText(self, wx.ID_ANY,
										   u"Copyrights (C) 2019 Rohit Kaundal (MCMC). All rights reserved.",
										   wx.DefaultPosition, wx.DefaultSize, 0)
		self.lblCopyRights.Wrap(-1)
		bSizer1.Add(self.lblCopyRights, 0, wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_CLOSE, self.MainDlgOnClose)
		self.mbtnGetAds.Bind(wx.EVT_BUTTON, self.onDownloadClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def MainDlgOnClose(self, event):
		self.Destroy()

	def onDownloadClick(self, event):
		self.mbtnGetAds.Disable()
		self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Downloading ADS initiated...\n")
		self.startDownloading()
		strLog = self.txtOutput.GetValue()
		with open('MCMCAds.log', 'a') as f:
			f.write(strLog)

		self.mbtnGetAds.Enable()

	def startDownloading(self):
		mToken = self.mtxtToken.GetValue()

		for strProgress in bg.fbSearchAds('Sanjay Tandon', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('BJP Chandigarh', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Kirron Kher', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Satya Pal Jain', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Indian National Congress - Chandigarh', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Pawan Kumar Bansal', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('NSUI Chandigarh.', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Chandigarh Youth Congress', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Navjot Sidhu', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Harmohan Dhawan, Former Union Minister, Govt. of India', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Aam Aadmi Party - Chandigarh', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Fans Of Harmohan Dhawan', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Avinash Singh Sharma', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Devi Sirohi', mToken):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")


		wx.MessageBox("Download Complete !")
		strCurrentPath = os.path.abspath(".\ADS Output")
		subprocess.Popen(f'explorer "{strCurrentPath}"')
		self.mtxtToken.SetFocus()

