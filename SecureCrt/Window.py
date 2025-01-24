class Window:
    def __init__(self, crt):
        self.crt = crt

    @property
    def Active(self) -> int:
        """ 是否活动窗口, 1是, 0否 """
        return self.crt.Window.Active

    @property
    def Caption(self) -> str:
        """ 返回或设置窗口标题 """
        return self.crt.Window.Caption

    @Caption.setter
    def Caption(self, value):
        self.crt.Window.Caption = value

    @property
    def State(self):
        """ 窗口状态, 0隐藏, 1正常, 2最小化, 3最大化 """
        return self.crt.Window.State

    def Activate(self):
        """ 置顶窗口 """
        self.crt.Window.Activate()

    def Show(self, state):
        """ 显示窗口, state[0隐藏, 1正常, 2最小化, 3最大化] """
        self.crt.Window.Show(state)
