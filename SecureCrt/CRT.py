from .Dialog import Dialog
from .Session import Session
from .Screen import Screen
from .Tab import Tab
from .Window import Window
from .Configuration import SessionConfiguration, GlobalConfiguration
from .CommandWindow import CommandWindow
from .Clipboard import Clipboard
from .Arguments import Arguments
from .FileTransfer import FileTransfer

class CRT:
    def __init__(self, crt):
        self.crt = crt

    @property
    def Config(self):
        return GlobalConfiguration(self.crt.Config)

    @property
    def ActivePrinter(self):
        return self.crt.ActivePrinter
  
    @ActivePrinter.setter
    def ActivePrinter(self, value: str):
        self.crt.ActivePrinter = value

    @property
    def Arguments(self):
        return Arguments(self.crt.Arguments)

    @property
    def Clipboard(self):
        return Clipboard(self.crt)

    @property
    def Dialog(self):
        return Dialog(self.crt)

    @property
    def FileTransfer(self):
        return FileTransfer(self.crt)

    @property
    def Screen(self):
        return Screen(self.crt.Screen)

    @property
    def ScriptFullName(self):
        return self.crt.ScriptFullName

    @property
    def Session(self):
        return Session(self.crt.Session)

    @property
    def Version(self):
        return self.crt.Version

    @property
    def Window(self):
        return Window(self.crt)

    @property
    def CommandWindow(self):
        return CommandWindow(self.crt)

    def ClearLastError(self):
        return self.crt.ClearLastError()

    def GetActiveTab(self):
        tab_obj = self.crt.GetActiveTab()
        return Tab(tab_obj)

    def GetLastError(self):
        return self.crt.GetLastError()

    def GetLastErrorMessage(self):
        return self.crt.GetLastErrorMessage()

    def GetScriptTab(self):
        tab_obj = self.crt.GetScriptTab()
        return Tab(tab_obj)

    def GetTab(self, index: int):
        tab_obj = self.crt.GetTab(index)
        return Tab(tab_obj)

    def GetTabCount(self):
        return self.crt.GetTabCount()

    def OpenSessionConfiguration(self, SessionPath: str = "Default"):
        return SessionConfiguration(self.crt.OpenSessionConfiguration(SessionPath))

    def Quit(self):
        return self.crt.Quit()
  
    def Sleep(self, milliseconds: int):
        return self.crt.Sleep(milliseconds)