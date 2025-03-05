class Window:
    def __init__(self, crt):
        self.crt = crt

    @property
    def Active(self) -> int:
        """ 返回 SecureCRT 应用窗口的活动状态：0 - 非活动窗口，1 - 活动窗口 """
        return self.crt.Window.Active

    @property
    def Caption(self) -> str:
        """ 返回/设置 SecureCRT 应用窗口的标题 """
        return self.crt.Window.Caption

    @Caption.setter
    def Caption(self, value: str) -> None:
        self.crt.Window.Caption = value

    @property
    def State(self) -> int:
        """ 返回 SecureCRT 应用窗口的状态：0 - 隐藏，1 - 正常，2 - 最小化，3 - 最大化 """
        return self.crt.Window.State

    def Activate(self) -> None:
        """ 激活 SecureCRT 应用窗口 """
        self.crt.Window.Activate()

    def Show(self, state: int) -> None:
        """ 设置 SecureCRT 应用窗口的状态：0 - 隐藏，1 - 正常，2 - 最小化，3 - 最大化 """
        self.crt.Window.Show(state)
