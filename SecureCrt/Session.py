from .Configuration import SessionConfiguration

class Session:
    def __init__(self, session):
        self.session = session

    @property
    def Config(self):
        """返回会话的配置"""
        return SessionConfiguration(self.session.Config)

    @property
    def Connected(self) -> bool:
        """返回当前会话是否连接"""
        return self.session.Connected

    @property
    def Label(self) -> str:
        """返回或设置会话的标签"""
        return self.session.Label

    @Label.setter
    def Label(self, value: str) -> None:
        self.session.Label = value

    @property
    def LocalAddress(self) -> str:
        """返回本地机器的IP地址"""
        return self.session.LocalAddress

    @property
    def Locked(self) -> bool:
        """返回当前会话是否锁定"""
        return self.session.Locked

    @property
    def LogFileName(self) -> str:
        """返回或设置当前日志文件的名称"""
        return self.session.LogFileName

    @LogFileName.setter
    def LogFileName(self, value: str) -> None:
        self.session.LogFileName = value

    @property
    def Logging(self) -> bool:
        """返回当前会话是否在记录日志"""
        return self.session.Logging

    @property
    def Path(self) -> str:
        """返回当前会话的路径"""
        return self.session.Path

    @property
    def RemoteAddress(self) -> str:
        """返回远程主机的IP地址"""
        return self.session.RemoteAddress

    @property
    def RemotePort(self) -> int:
        """返回远程端口号"""
        return self.session.RemotePort

    def Connect(self, strConnectInfo="", bWaitForAuthToComplete=True, bSuppressErrorPopups=False):
        """连接到会话"""
        self.session.Connect(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)

    def ConnectInTab(self, strConnectInfo="", bWaitForAuthToComplete=True, bSuppressErrorPopups=False):
        """在选项卡中连接到会话"""
        from .Tab import Tab
        tab_obj = self.session.ConnectInTab(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)
        return Tab(tab_obj)

    def Disconnect(self):
        """断开当前会话"""
        self.session.Disconnect()

    def Lock(self, bPrompt=False, strPassword="", bLockAllSessions=False, bHideOutput=False):
        """锁定当前会话"""
        self.session.Lock(bPrompt, strPassword, bLockAllSessions, bHideOutput)

    def Log(self, start, append=False, raw=False):
        """启用或禁用日志记录"""
        self.session.Log(start, append, raw)

    def LogUsingSessionOptions(self):
        """使用会话选项启用日志记录"""
        self.session.LogUsingSessionOptions()

    def Print(self, start):
        """启动或停止自动打印"""
        self.session.Print(start)

    def SetStatusText(self, text: str):
        """设置状态栏文本"""
        self.session.SetStatusText(text)

    def Unlock(self, bPrompt=False, strPassword="", bUnlockAllSessions=False):
        """解锁当前会话"""
        self.session.Unlock(bPrompt, strPassword, bUnlockAllSessions)
