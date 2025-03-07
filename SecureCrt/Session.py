from typing import Any, Optional, Union
from .Configuration import SessionConfiguration
from .Tab import Tab

class Session:
    """
    Session 对象提供对当前连接或会话的状态和属性的访问。
    
    通过 Session 对象可以访问连接状态、标签、日志记录、锁定状态等属性，
    以及执行连接、断开连接、锁定、解锁等操作。
    
    SecureCRT 的 Session 对象通过顶级对象的 Session 属性访问。
    """
    def __init__(self, obj):
        """
        初始化 Session 对象
        
        Args:
            obj: SecureCRT Session 对象
        """
        self.obj = obj

    @property
    def Config(self):
        """
        返回与会话关联的配置。
        
        此配置无法保存为新名称。
        
        Returns:
            SessionConfiguration: 会话配置对象
        """
        return SessionConfiguration(self.obj.Config)

    @property
    def Connected(self) -> bool:
        """
        返回一个布尔值，表示当前会话是否已连接。
        
        这是一个只读属性。
        
        Returns:
            bool: 表示会话是否已连接
        """
        return self.obj.Connected

    @property
    def Label(self) -> str:
        """
        返回或设置会话的标签。
        
        可以通过右键单击会话选项卡上的名称并选择"重命名"来重命名选项卡。
        标签更改将一直有效，直到重新使用选项卡或 SecureCRT 退出。
        
        Returns:
            str: 会话的标签
        """
        return self.obj.Label

    @Label.setter
    def Label(self, value: str) -> None:
        """
        设置会话的标签。
        
        Args:
            value (str): 新的会话标签
        """
        self.obj.Label = value

    @property
    def LocalAddress(self) -> str:
        """
        返回本地机器的 IP 地址，以字符串形式表示。
        
        这是一个只读属性。只有在会话已连接时才应访问此属性。
        在未连接时尝试访问 LocalAddress 将产生错误。
        
        Returns:
            str: 本地机器的 IP 地址
        """
        return self.obj.LocalAddress

    @property
    def Locked(self) -> bool:
        """
        返回一个布尔值，表示当前会话是否已锁定。
        
        这是一个只读属性。
        
        Returns:
            bool: 表示会话是否已锁定
        """
        return self.obj.Locked

    @property
    def LogFileName(self) -> str:
        """
        返回或设置当前日志文件的名称。
        
        如果文件名无效，将生成运行时错误。请参阅：Session.Log
        如果日志文件名包含在调用函数时已知的参数替换，则会填充这些参数。
        否则，返回原样字符串。
        
        Returns:
            str: 当前日志文件的名称
        """
        return self.obj.LogFileName

    @LogFileName.setter
    def LogFileName(self, value: str) -> None:
        """
        设置当前日志文件的名称。
        
        Args:
            value (str): 新的日志文件名
        """
        self.obj.LogFileName = value

    @property
    def Logging(self) -> bool:
        """
        返回一个布尔值，表示当前会话是否正在记录日志。
        
        这是一个只读属性。
        
        Returns:
            bool: 表示会话是否正在记录日志
        """
        return self.obj.Logging

    @property
    def Path(self) -> str:
        """
        返回当前会话在会话管理器或连接对话框中的路径，包括会话本身的名称。
        
        这是一个只读属性，返回保存的会话在会话管理器中显示的组织文件夹路径。
        如果用于此调用的会话对象未与保存的会话关联，则返回"Default"，
        表示该会话对应于临时连接，而不是保存的会话。
        
        路径分隔符是特定于操作系统的：
        - 在 Windows 上，返回的值将使用"\"作为路径分隔符
        - 在 Linux/macOS 版本的 SecureCRT 上，使用"/"作为路径分隔符
        
        例如，如果会话组织如下：
        
        Sessions
        -  Routers
          - Region 01
          - Region 02
            - Cisco Router 1
            - Cisco Router 2
            - Cisco Router 3
        
        其中 Cisco Router 3 是用于在选项卡中建立连接的保存会话，则以下脚本代码：
        
        strSessionPath = crt.GetScriptTab().Session.Path
        
        在 Windows 版本的 SecureCRT 中，将生成一个值为 "Routers\Region 02\Cisco Router 3" 的字符串变量 strSessionPath，
        在 Linux 和 macOS 上，值为 "Routers/Region 02/Cisco Router 3"。
        
        Returns:
            str: 当前会话的路径
        """
        return self.obj.Path

    @property
    def RemoteAddress(self) -> str:
        """
        返回远程主机的 IP 地址，以字符串形式表示。
        
        这是一个只读属性。只有在会话已连接时才应访问此属性。
        在未连接时尝试访问 RemoteAddress 将产生错误。
        
        注意：当会话通过 SOCKS 版本 5 代理连接时，IP 地址不可用。
        
        Returns:
            str: 远程主机的 IP 地址
        """
        return self.obj.RemoteAddress

    @property
    def RemotePort(self) -> int:
        """
        返回远程端口号。
        
        这是一个只读属性。只有在会话已连接时才应访问此属性。
        
        Returns:
            int: 远程端口号
        """
        return self.obj.RemotePort

    def Connect(self, strConnectInfo: str = "", bWaitForAuthToComplete: bool = True, 
                bSuppressErrorPopups: bool = False) -> None:
        """
        连接到会话。
        
        Connect 方法接受一个字符串参数，指定如何建立连接。
        字符串参数的格式与 SecureCRT 的命令行参数格式相匹配。
        
        如果选项卡/平铺窗口已有活动连接，Connect 方法将失败。
        如果要在另一个选项卡/平铺窗口中建立新连接，请改用 ConnectInTab 方法。
        
        Connect 方法可以接受空参数集。语句 crt.Session.Connect() 表示"连接到当前会话"。
        如果之前未建立连接，该语句将失败。如果连接已存在，则不执行任何操作，
        否则，该语句相当于按下"重新连接"按钮。
        
        示例：
        
        使用预定义的会话进行连接：
        crt.session.Connect("/s mysession")
        
        使用 Telnet 协议和默认会话参数连接到端口 2345 的 "myhost"：
        crt.session.Connect("/telnet myhost 2345")
        
        Connect 方法的 bWaitForAuthToComplete 参数（True 或 False）决定脚本是否应等待
        连接完全认证后再继续执行。例如，如果将该参数设为 True，将等待连接完全认证后才返回
        并允许脚本执行连接调用之后的错误检查。此参数仅适用于 SSH1 和 SSH2 连接。
        而传递 False 将允许在连接有机会完成之前执行错误检查。
        通常只有在想要为尝试连接的会话编写登录过程脚本时才使用 False。
        此参数的默认值为 True。
        
        Connect 方法还接受一个可选参数 bSuppressErrorPopups（True 或 False），
        指定是否禁止显示弹出消息。此参数默认为 False（不禁止）。
        
        Args:
            strConnectInfo (str, optional): 连接信息字符串。默认为空字符串
            bWaitForAuthToComplete (bool, optional): 是否等待身份验证完成。默认为 True
            bSuppressErrorPopups (bool, optional): 是否禁止错误弹出窗口。默认为 False
        """
        self.obj.Connect(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)

    def ConnectInTab(self, strConnectInfo: str = "", bWaitForAuthToComplete: bool = True, 
                     bSuppressErrorPopups: bool = False) -> Tab:
        """
        在选项卡或平铺会话窗口中连接到会话。
        
        接受与 Connect 相同的参数。此方法还返回一个 Tab 对象。
        
        ConnectInTab 方法还接受两个可选参数（True 或 False）。
        第一个参数决定脚本是否应等待连接完全认证后再继续执行。
        第一个参数仅适用于 SSH1 和 SSH2 连接。
        第二个可选参数指定调用是静默失败还是引发异常。
        
        如果第二个参数为 False 且连接尝试失败，则会引发异常并且方法返回一个空对象。
        如果第二个参数为 True 且连接尝试失败，则方法返回一个有效的 Tab 对象，
        然后可以用于检查连接状态，以确定连接尝试是否成功。
        
        ConnectInTab 不支持使用 TN3270 模拟的会话。
        
        示例：
        
        使用预定义的会话在选项卡中连接：
        tab = crt.session.ConnectInTab("/s mysession")
        
        使用 Telnet 协议和默认会话参数在选项卡中连接到端口 2345 的 "myhost"：
        tab = crt.session.ConnectInTab("/telnet myhost 2345")
        
        如果连接尝试失败则关闭选项卡：
        objNewTab = crt.Session.ConnectInTab("Host_Does_Not_Exist", bSuppressErrorPopups=True)
        crt.Dialog.MessageBox(
            "Script Tab's index: " + str(crt.GetScriptTab().Index) + "\\n" +
            "New Tab's index: " + str(objNewTab.Index))
        if objNewTab.Session.Connected != True:
            # 确保我们不是重复使用已断开连接的选项卡，
            # 我们不想关闭脚本选项卡，只想关闭由
            # ConnectInTab() 调用创建但未导致
            # 成功连接的任何新选项卡。
            if crt.GetScriptTab().Index != objNewTab.Index:
                crt.Dialog.MessageBox("Closing failed tab")
                objNewTab.Close()
        
        Args:
            strConnectInfo (str, optional): 连接信息字符串。默认为空字符串
            bWaitForAuthToComplete (bool, optional): 是否等待身份验证完成。默认为 True
            bSuppressErrorPopups (bool, optional): 是否禁止错误弹出窗口。默认为 False
            
        Returns:
            Tab: 连接创建的 Tab 对象
        """
        from .Tab import Tab
        tab_obj = self.obj.ConnectInTab(strConnectInfo, bWaitForAuthToComplete, bSuppressErrorPopups)
        return Tab(tab_obj)

    def Disconnect(self) -> None:
        """
        断开当前会话的连接。
        
        如果当前会话未连接，Disconnect 不执行任何操作。
        """
        self.obj.Disconnect()

    def Lock(self, bPrompt: bool = False, strPassword: str = "", 
             bLockAllSessions: bool = False, bHideOutput: bool = False) -> None:
        """
        锁定当前会话（或所有会话）。
        
        所有参数都是可选的。bPrompt 的默认值为 False。
        如果 bPrompt 为 True，将显示"锁定会话"对话框。
        strPassword 的默认值为空字符串 ("")。
        bLockAllSessions 和 bHideOutput 的默认值为 False。
        
        Args:
            bPrompt (bool, optional): 是否显示锁定会话对话框。默认为 False
            strPassword (str, optional): 锁定密码。默认为空字符串
            bLockAllSessions (bool, optional): 是否锁定所有会话。默认为 False
            bHideOutput (bool, optional): 是否隐藏输出。默认为 False
        """
        self.obj.Lock(bPrompt, strPassword, bLockAllSessions, bHideOutput)

    def Log(self, start: bool, append: bool = False, raw: bool = False) -> None:
        """
        启用或禁用日志记录。
        
        根据"start"参数的布尔状态启动或停止日志记录。
        在启动日志记录时，可选的布尔参数"append"和"raw"可以设置为 True，
        分别用于以追加模式打开日志文件或记录原始字符。
        append 和 raw 参数是可选的，如果未指定则为 False
        （当"start"为 False 时，append 和 raw 的值将被忽略）。
        
        Args:
            start (bool): True 表示开始记录日志，False 表示停止记录
            append (bool, optional): 是否以追加模式打开日志文件。默认为 False
            raw (bool, optional): 是否记录原始字符。默认为 False
        """
        self.obj.Log(start, append, raw)

    def LogUsingSessionOptions(self) -> None:
        """
        使用当前会话的日志选项启用日志记录。
        
        如果会话是临时会话，将使用默认会话的日志选项。
        """
        self.obj.LogUsingSessionOptions()

    def Print(self, start: bool) -> None:
        """
        启动或停止自动打印。
        
        根据布尔参数 start 启动或停止自动打印。
        
        Args:
            start (bool): True 表示开始自动打印，False 表示停止自动打印
        """
        self.obj.Print(start)

    def SetStatusText(self, text: str) -> None:
        """
        允许设置特定会话的状态栏文本。
        
        将状态栏消息设置为指定的文本字符串。
        
        Args:
            text (str): 要显示在状态栏的文本
        """
        self.obj.SetStatusText(text)

    def Unlock(self, bPrompt: bool = False, strPassword: str = "", 
               bUnlockAllSessions: bool = False) -> None:
        """
        解锁当前会话（或所有会话）。
        
        所有参数都是可选的。bPrompt 的默认值为 False。
        如果 bPrompt 为 True，将显示"解锁会话"对话框。
        strPassword 的默认值为空字符串 ("")。
        bUnlockAllSessions 的默认值为 False。
        
        Args:
            bPrompt (bool, optional): 是否显示解锁会话对话框。默认为 False
            strPassword (str, optional): 解锁密码。默认为空字符串
            bUnlockAllSessions (bool, optional): 是否解锁所有会话。默认为 False
        """
        self.obj.Unlock(bPrompt, strPassword, bUnlockAllSessions)
