class Window:
    def __init__(self, crt):
        self.crt = crt

    @property
    def Active(self):
        return self.crt.Window.Active

    @property
    def Caption(self):
        return self.crt.Window.Caption

    @Caption.setter
    def Caption(self, value):
        self.crt.Window.Caption = value

    @property
    def State(self):
        return self.crt.Window.State

    def Activate(self):
        self.crt.Window.Activate()

    def Show(self, state):
        self.crt.Window.Show(state)
