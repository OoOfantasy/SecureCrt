class SessionConfiguration:
    def __init__(self, obj):
        self.obj = obj
    
    def ConnectInTab(self):
        from .Tab import Tab
        return Tab(self.obj.ConnectInTab())

    def GetOption(self, OptionName: str):
        return self.obj.GetOption(OptionName)

    def Save(self, SessionPath: str = ""):
        self.obj.Save(SessionPath)

    def SetOption(self, OptionName: str, Value: str):
        self.obj.SetOption(OptionName, Value)