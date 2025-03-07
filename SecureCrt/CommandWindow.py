from typing import Any

class CommandWindow:
    """
    CommandWindow 对象提供对 SecureCRT 命令窗口的访问。
    
    通过 CommandWindow 对象可以控制命令窗口的可见状态、文本内容，
    以及发送命令等操作。
    
    SecureCRT 的 CommandWindow 对象通过顶级对象的 CommandWindow 属性访问。
    """
    def __init__(self, crt):
        """
        初始化 CommandWindow 对象
        
        Args:
            crt: SecureCRT 对象
        """
        self.crt = crt
    
    @property
    def SendCharactersImmediately(self) -> bool:
        """
        返回或设置一个布尔值，指示命令窗口输入是否应立即发送。
        
        当设置为 True 时，输入命令窗口的字符将立即发送到远程系统，
        而不需要通过 Send 方法显式发送。
        
        示例：
            # 启用立即发送字符
            crt.CommandWindow.SendCharactersImmediately = True
            
            # 查询当前立即发送设置
            immediate_send = crt.CommandWindow.SendCharactersImmediately
        
        Returns:
            bool: True 表示立即发送，False 表示需要显式调用 Send 方法
        """
        return self.crt.CommandWindow.SendCharactersImmediately
    
    @SendCharactersImmediately.setter
    def SendCharactersImmediately(self, value: bool) -> None:
        """
        设置命令窗口输入是否应立即发送。
        
        Args:
            value (bool): True 表示立即发送，False 表示需要显式调用 Send 方法
        """
        self.crt.CommandWindow.SendCharactersImmediately = value
    
    @property
    def SendToAllSessions(self) -> bool:
        """
        返回或设置一个布尔值，指示命令窗口文本是否应发送到所有会话。
        
        当设置为 True 时，从命令窗口发送的命令将被发送到所有打开的会话，
        而不仅仅是当前活动会话。此功能在需要同时管理多个会话时非常有用。
        
        示例：
            # 启用向所有会话发送命令
            crt.CommandWindow.SendToAllSessions = True
            
            # 查询当前向所有会话发送的设置
            send_all = crt.CommandWindow.SendToAllSessions
        
        Returns:
            bool: True 表示发送到所有会话，False 表示只发送到当前会话
        """
        return self.crt.CommandWindow.SendToAllSessions
    
    @SendToAllSessions.setter
    def SendToAllSessions(self, value: bool) -> None:
        """
        设置命令窗口文本是否应发送到所有会话。
        
        Args:
            value (bool): True 表示发送到所有会话，False 表示只发送到当前会话
        """
        self.crt.CommandWindow.SendToAllSessions = value
    
    @property
    def Text(self) -> str:
        """
        返回或设置命令窗口中的文本。
        
        这是一个可读写的字符串属性。可以通过使用回车换行符（\\r\\n）向命令窗口添加多行文本。
        读取此属性将返回命令窗口中当前的文本内容。
        
        示例：
            # 在命令窗口中填入多行命令
            crt.CommandWindow.Text = "ls -l\\r\\npwd\\r\\nwhoami"
            
            # 获取命令窗口中当前的文本
            current_text = crt.CommandWindow.Text
            
            # 在命令窗口中填入带有控制字符的命令
            crt.CommandWindow.Text = "\\x1b:q"  # ESC 后跟 :q
        
        Returns:
            str: 命令窗口中的文本内容
        """
        return self.crt.CommandWindow.Text
    
    @Text.setter
    def Text(self, value: str) -> None:
        """
        设置命令窗口中的文本。
        
        Args:
            value (str): 要设置的文本内容，可以包含多行（使用\\r\\n分隔）
        """
        self.crt.CommandWindow.Text = value
    
    @property
    def Visible(self) -> bool:
        """
        返回或设置一个布尔值，指示命令窗口是否可见。
        
        这是一个可读写的布尔属性。通过设置此属性，可以控制命令窗口的显示状态。
        读取此属性将返回命令窗口当前的可见状态。
        
        示例：
            # 保存命令窗口当前的可见状态
            cmd_window_visible = crt.CommandWindow.Visible
            
            # 确保命令窗口可见
            crt.CommandWindow.Visible = True
            
            # 执行一些操作...
            
            # 恢复命令窗口的原始状态
            crt.CommandWindow.Visible = cmd_window_visible
        
        Returns:
            bool: True 表示命令窗口可见，False 表示不可见
        """
        return self.crt.CommandWindow.Visible
    
    @Visible.setter
    def Visible(self, value: bool) -> None:
        """
        设置命令窗口是否可见。
        
        Args:
            value (bool): True 表示命令窗口可见，False 表示不可见
        """
        self.crt.CommandWindow.Visible = value
    
    def Send(self) -> None:
        """
        将当前命令窗口中的文本发送到远程机器。
        
        此方法会将命令窗口中当前的文本内容发送到远程系统，就像用户手动按下 Enter 键一样。
        如果 SendToAllSessions 属性设置为 True，将会向所有打开的会话发送命令。
        
        示例：
            # 设置命令窗口文本并发送
            crt.CommandWindow.Text = "ls -la"
            crt.CommandWindow.Send()
            
            # 或者先设置多行命令，然后一次性发送
            crt.CommandWindow.Text = "cd /tmp\\r\\nls -la\\r\\npwd"
            crt.CommandWindow.Send()
        """
        self.crt.CommandWindow.Send()
