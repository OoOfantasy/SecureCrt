class Screen:
    def __init__(self, obj):
        self.obj = obj
        self.CurrentColumn = 0
        self.CurrentRow = 0
        self.Columns = 0
        self.IgnoreEscape = False
        self.IgnoreCase = False
        self.MatchIndex = 0
        self.Rows = 0
        self.Selection = ""
        self.Synchronous = False

    def Clear(self):
        # ...implementation...
        pass

    def Get(self):
        # ...implementation...
        pass

    def Get2(self):
        # ...implementation...
        pass

    def Print(self):
        # ...implementation...
        pass

    def ReadString(self):
        # ...implementation...
        pass

    def Send(self):
        # ...implementation...
        pass

    def SendKeys(self):
        # ...implementation...
        pass

    def SendSpecial(self):
        # ...implementation...
        pass

    def WaitForCursor(self):
        # ...implementation...
        pass

    def WaitForKey(self):
        # ...implementation...
        pass

    def WaitForString(self):
        # ...implementation...
        pass

    def WaitForStrings(self):
        # ...implementation...
        pass