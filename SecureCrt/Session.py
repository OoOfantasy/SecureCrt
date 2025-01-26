class Session:
    def __init__(self, obj):
        self.obj = obj
    
    @property
    def Config(self):
        from .SessionConfiguration import SessionConfiguration
        return SessionConfiguration(self.obj.Session.Config)
    
    @property
    def Connected(self):
        return self.obj.Session.Connected

    @property
    def Label(self):
        return self.obj.Session.Label

    @Label.setter
    def Label(self, value: str):
        self.obj.Session.Label = value

    @property
    def LocalAddress(self):
        return self.obj.Session.LocalAddress
    
    @property
    def Locked(self):
        return self.obj.Session.Locked

    @property
    def LogFileName(self):
        return self.obj.Session.LogFileName

    @LogFileName.setter
    def LogFileName(self, value: str):
        self.obj.Session.LogFileName = value

    @property
    def Logging(self):
        return self.obj.Session.Logging
    
    @property
    def Path(self):
        return self.obj.Session.Path
    
    @property
    def RemoteAddress(self):
        return self.obj.Session.RemoteAddress
    
    @property
    def RemotePort(self):
        return self.obj.Session.RemotePort

    def Connect(self, strConnectInfo: str = "", bWaitForAuthToComplete: bool = True, bSuppressErrorPopups: bool = False):
        return self.obj.Session.Connect(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)

    def ConnectInTab(self, strConnectInfo: str = "", bWaitForAuthToComplete: bool = True, bSuppressErrorPopups: bool = False):
        return self.obj.Session.ConnectInTab(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)

    def Disconnect(self):
        return self.obj.Session.Disconnect()

    def Lock(self, bPrompt: bool = False, strPassword: str = "", bLockAllSessions: bool = False, bHideOutput: bool = False):
        return self.obj.Session.Lock(bPrompt, strPassword, bLockAllSessions, bHideOutput)

    def Log(self, start: bool, append: bool = False, raw: bool = False):
        return self.obj.Session.Log(start, append, raw)

    def LogUsingSessionOptions(self):
        return self.obj.Session.LogUsingSessionOptions()

    def Print(self, start: bool):
        return self.obj.Session.Print(start)

    def SetStatusText(self, text: str):
        return self.obj.Session.SetStatusText(text)

    def Unlock(self, bPrompt: bool = False, strPassword: str = "", bUnlockAllSessions: bool = False):
        return self.obj.Session.Unlock(bPrompt, strPassword, bUnlockAllSessions)