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
import FBAdsBackend as bg
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
									 u"Fb Acess Token...",
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
		bg.makeDir("./ADS Output")

		mToken = self.mtxtToken.GetValue()

		for strProgress in bg.fbSearchAds('Sanjay Tandon', mToken, "224618077692752"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('BJP Chandigarh', mToken, "646852468671636"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Kirron Kher', mToken, "757254360959518"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Satya Pal Jain', mToken, "58924788007"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Indian National Congress - Chandigarh', mToken, "144405846101958"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Pawan Kumar Bansal', mToken, "436152543129710"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Pawan Kumar Bansal - Apna Chandigarh', mToken, "2248548095205729"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('NSUI Chandigarh.', mToken, "1656333154591788"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Chandigarh Youth Congress', mToken, "383663315386405"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Navjot Sidhu', mToken, "375345359249262"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Harmohan Dhawan, Former Union Minister, Govt. of India', mToken, "157716834420075"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Aam Aadmi Party - Chandigarh', mToken, "428452507204659"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Fans Of Harmohan Dhawan', mToken, "1941214205996225"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Avinash Singh Sharma', mToken, "380018826152835"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")

		for strProgress in bg.fbSearchAds('Devi Sirohi', mToken, "1672059219762128"):
			self.txtOutput.AppendText(
			f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {strProgress}\n")


		wx.MessageBox("Download Complete !")
		strCurrentPath = os.path.abspath(".\ADS Output")
		subprocess.Popen(f'explorer "{strCurrentPath}"')
		self.mtxtToken.SetFocus()

