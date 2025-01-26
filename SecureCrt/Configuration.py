class Configuration:
    def __init__(self, obj):
        self.obj = obj
    
    def GetOption(self, OptionName: str):
        return self.obj.GetOption(OptionName)

    def Save(self, SessionPath: str = ""):
        self.obj.Save(SessionPath)

    def SetOption(self, OptionName: str, Value: str):
        self.obj.SetOption(OptionName, Value)

class SessionConfiguration(Configuration):
    def __init__(self, obj):
        super(SessionConfiguration, self).__init__(obj)
        self.obj = obj
     
    def ConnectInTab(self):
        from .Tab import Tab
        return Tab(self.obj.ConnectInTab())

class GlobalConfiguration(Configuration):
    def __init__(self, crt):
        super(GlobalConfiguration, self).__init__(crt)