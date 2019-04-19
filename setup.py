import sys
from cx_Freeze import setup, Executable

setup(name = "MCMCAdsTool" ,
      version = "1.0" ,
      description = "FB Ads monitoring tool for MCMC Chandigarh. Designed and developed by - Rohit Kaundal" ,
      author="Rohit Kaundal",
      executables = [Executable(script="AppGUI.py", base="Win32GUI")])
