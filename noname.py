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
###########################################################################
## Class MainDlg
###########################################################################

class MainDlg ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MCMC ADS Fetcher", pos = wx.DefaultPosition, size = wx.Size( 432,344 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.mlblToken = wx.StaticText( self, wx.ID_ANY, u"Facebook GRAPH Api Token", wx.Point( 10,10 ), wx.DefaultSize, wx.ALIGN_CENTRE )
		self.mlblToken.Wrap( -1 )
		bSizer1.Add( self.mlblToken, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.mtxtToken = wx.TextCtrl( self, wx.ID_ANY, u"EAAgzFO2gyWoBANLZA8RROlZBUNLjXlm6LNsZA7ZAXUmJFIZAEZB9RNSwHnPSDchAq7ugIn42ZAhnlfoN14GpWKDdnCVTnjSXsQ2RZBWgL3bhY8f6zAzpFLfjfSdMaW3qXI1ZB3ZBcd0byZCYG4pdieHmjZC7XkTwgPYIvSmApvOaUlIUxcLvN2E1t8k18bHCkZAYo0SIxuQQFN6pedynZB9ZAZArVu7P", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.mtxtToken, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.mbtnGetAds = wx.Button( self, wx.ID_ANY, u"Download ADS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.mbtnGetAds, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.txtOutput = wx.TextCtrl( self, wx.ID_ANY, u"Progress...", wx.DefaultPosition, wx.Size( -1,400 ), wx.TE_MULTILINE )
		self.txtOutput.Enable( False )
		
		bSizer1.Add( self.txtOutput, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MainDlgOnClose )
		self.mbtnGetAds.Bind( wx.EVT_BUTTON, self.onDownloadClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MainDlgOnClose( self, event ):
		self.Destroy()
	
	def onDownloadClick( self, event ):
		self.txtOutput.AppendText("\n[+] Downloading ADS initiated...\n")
		for i in range(0,10):
			self.txtOutput.AppendText(f"{i}%...")
			time.sleep(1)
		self.txtOutput.AppendText("\n[+]Downloads Completed !\n")
	

