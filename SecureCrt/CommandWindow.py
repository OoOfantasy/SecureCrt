class CommandWindow:
    def __init__(self, crt):
        self.command_window = crt.CommandWindow

    @property
    def SendCharactersImmediately(self) -> bool:
        """ 返回或设置一个布尔值，指示命令窗口输入是否应立即发送 """
        return self.command_window.SendCharactersImmediately

    @SendCharactersImmediately.setter
    def SendCharactersImmediately(self, value: bool) -> None:
        self.command_window.SendCharactersImmediately = value

    @property
    def SendToAllSessions(self) -> bool:
        """ 返回或设置一个布尔值，指示命令窗口文本是否应发送到所有会话 """
        return self.command_window.SendToAllSessions

    @SendToAllSessions.setter
    def SendToAllSessions(self, value: bool) -> None:
        self.command_window.SendToAllSessions = value

    @property
    def Text(self) -> str:
        """ 返回或设置命令窗口中的文本 """
        return self.command_window.Text

    @Text.setter
    def Text(self, value: str) -> None:
        self.command_window.Text = value

    @property
    def Visible(self) -> bool:
        """ 返回或设置一个布尔值，指示命令窗口是否可见 """
        return self.command_window.Visible

    @Visible.setter
    def Visible(self, value: bool) -> None:
        self.command_window.Visible = value

    def Send(self) -> None:
        """ 将命令窗口中的当前文本发送到远程机器 """
        self.command_window.Send()
