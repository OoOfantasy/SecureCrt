from typing import List, Union, Optional, Any

class Screen:
    """
    Screen对象提供对SecureCRT终端屏幕的访问。
    通过Screen对象可以读取屏幕内容、发送命令、等待特定字符串等。
    """
    def __init__(self, obj):
        self.obj = obj

    @property
    def CurrentColumn(self) -> int:
        """
        返回光标的当前列位置。
        
        列编号从1开始。如果没有打开连接，将返回错误。
        
        Returns:
            int: 当前光标列位置
        """
        return self.obj.CurrentColumn

    @property
    def CurrentRow(self) -> int:
        """
        返回光标的当前行位置。
        
        行编号从1开始。如果没有打开连接，将返回错误。
        
        Returns:
            int: 当前光标行位置
        """
        return self.obj.CurrentRow

    @property
    def Columns(self) -> int:
        """
        返回当前屏幕的列数。
        
        Returns:
            int: 屏幕列数
        """
        return self.obj.Columns

    @property
    def IgnoreEscape(self) -> bool:
        """
        获取或设置是否忽略转义序列。
        
        此属性控制ReadString()或WaitForString()是否识别转义序列。
        默认情况下，ReadString会捕获并查找转义序列。
        
        Returns:
            bool: 是否忽略转义序列
        """
        return self.obj.IgnoreEscape

    @IgnoreEscape.setter
    def IgnoreEscape(self, value: bool) -> None:
        """
        设置是否忽略转义序列。
        
        Args:
            value (bool): True表示忽略转义序列，False表示不忽略
        """
        self.obj.IgnoreEscape = value

    @property
    def MatchIndex(self) -> int:
        """
        获取ReadString或WaitForStrings方法找到的字符串在列表中的索引。
        
        只在与ReadString或WaitForStrings方法结合使用时有效。
        返回值1表示找到第一个字符串，2表示第二个字符串，依此类推。
        返回值0表示发生超时，未找到匹配项。
        
        Returns:
            int: 匹配的字符串索引
        """
        return self.obj.MatchIndex

    @property
    def Rows(self) -> int:
        """
        返回当前屏幕的行数。
        
        Returns:
            int: 屏幕行数
        """
        return self.obj.Rows

    @property
    def Selection(self) -> str:
        """
        返回当前选择的文本内容。
        
        Returns:
            str: 当前选择的文本
        """
        return self.obj.Selection

    @property
    def Synchronous(self) -> bool:
        """
        获取或设置屏幕的同步设置。
        
        如果Synchronous为False，那么在某些情况下，脚本可能会错过它期望看到的服务器发送的数据。
        默认情况下，Synchronous设置为False。
        
        Returns:
            bool: 是否同步
        """
        return self.obj.Synchronous

    @Synchronous.setter
    def Synchronous(self, value: bool) -> None:
        """
        设置屏幕的同步设置。
        
        Args:
            value (bool): 是否同步
        """
        self.obj.Synchronous = value

    def Clear(self) -> None:
        """
        清除屏幕内容。
        """
        self.obj.Clear()

    def Get(self, row1: int, col1: int, row2: int, col2: int) -> str:
        """
        返回屏幕指定矩形区域的字符串内容。
        
        Args:
            row1 (int): 左上角行坐标
            col1 (int): 左上角列坐标
            row2 (int): 右下角行坐标
            col2 (int): 右下角列坐标
        
        Returns:
            str: 指定区域的字符串内容
        """
        return self.obj.Get(row1, col1, row2, col2)

    def Get2(self, row1: int, col1: int, row2: int, col2: int) -> str:
        """
        返回屏幕指定矩形区域的字符串内容，每行以\\r\\n结束。
        
        此方法返回的每一行以\\r\\n结尾，这样可以通过查找\\r\\n序列来分割行。
        这允许不同行具有不同的长度，取决于行的内容。
        对于处理MBCS语言，应使用Get2接口。
        
        Args:
            row1 (int): 左上角行坐标
            col1 (int): 左上角列坐标
            row2 (int): 右下角行坐标
            col2 (int): 右下角列坐标
        
        Returns:
            str: 指定区域的字符串内容，每行以\\r\\n结束
        """
        return self.obj.Get2(row1, col1, row2, col2)

    def IgnoreCase(self) -> None:
        """
        设置全局忽略大小写选项。
        
        如果启用此方法，WaitForStrings、WaitForString和ReadString方法将不区分大小写，
        否则它们将区分大小写（默认情况）。
        """
        self.obj.IgnoreCase()

    def Print(self) -> None:
        """
        打印屏幕内容。
        
        如果机器上未定义打印机，将返回错误。
        """
        self.obj.Print()

    def ReadString(self, strings=None, timeoutSeconds: int = 0, bCaseInsensitive: bool = False) -> str:
        """
        捕获从远程接收的数据。
        
        ReadString类似于WaitForStrings函数，但不同之处在于ReadString捕获数据。
        默认情况下，ReadString将捕获从远程接收的所有数据，包括转义序列。
        要启用或禁用ReadString捕获的数据中包含转义序列，请将Screen.IgnoreEscape属性设置为false/true。
        
        如果提供了timeout参数，并且ReadString在未收到指定字符串的情况下达到超时期限，
        ReadString将返回一个空字符串。
        
        使用方式有三种场景：
        1. 一旦从远程有数据可用，就返回数据，一次一个字符：
           char = crt.Screen.ReadString()
           
        2. 捕获数据直到从远程检测到特定字符串：
           str = crt.Screen.ReadString("home", 10)
           
        3. 捕获数据直到从远程检测到多个字符串列表中的一个：
           str = crt.Screen.ReadString(["home", "work"], 10)
        
        Args:
            strings: 要等待的字符串或字符串列表
            timeoutSeconds (int, optional): 等待超时秒数。默认为0，表示无超时
            bCaseInsensitive (bool, optional): 是否忽略大小写。默认为False，即区分大小写
            
        Returns:
            str: 捕获的数据字符串，如果超时则返回空字符串
        """
        return self.obj.ReadString(strings, timeoutSeconds, bCaseInsensitive)

    def Send(self, string: str, bSendToScreenOnly: bool = False, bEncode: bool = True) -> None:
        """
        发送字符串到远程系统。
        
        当没有打开连接时尝试发送字符串将返回错误。
        对于使用TN3270模拟的会话，不要在字符串末尾附加回车符。
        要发送回车，请使用Screen.SendSpecial与"TN3270_RETURN"参数。
        
        Send接口可以处理MBCS语言，并且无论显示字体是否可以表示这些字符，
        只要会话的"字符编码"可以表示这些字符，它都能正常工作。
        
        Args:
            string (str): 要发送的字符串
            bSendToScreenOnly (bool, optional): 是否仅发送到屏幕，不发送到远程系统。默认为False
            bEncode (bool, optional): 当bSendToScreenOnly为True时，是否在发送到屏幕前对文本进行编码。默认为True
        """
        self.obj.Send(string, bSendToScreenOnly, bEncode)

    def SendKeys(self, string: str) -> None:
        """
        发送按键到活动窗口。
        
        SendKeys方法可以通过使用复合字符串参数一次发送多个按键。
        例如，要发送按键a、b和c，可以发送字符串参数"abc"。
        SendKeys方法还使用一些字符作为字符的修饰符，包括加号(+)、脱字符(^)、
        百分号(%)、波浪号(~)、括号、方括号和大括号。
        
        字符"+"、"^"和"%"分别执行SHIFT、CTRL和ALT的功能。
        这些可以组合起来影响一个键，如"^%c"相当于CTRL+ALT+C组合键。
        
        Args:
            string (str): 要发送的按键字符串
        """
        self.obj.SendKeys(string)

    def SendSpecial(self, string: str) -> None:
        """
        发送内置的SecureCRT命令。
        
        SendSpecial可以发送在Map Selected Key对话框中列出的任何Menu、Telnet和VT函数
        （通过在Keymap Editor中选择一个键并单击Map Selected Key...按钮访问）。
        
        当没有打开连接时尝试使用SendSpecial将导致错误。
        对于使用TN3270模拟的会话，要发送回车，请使用Screen.SendSpecial与"TN3270_RETURN"参数。
        要发送Transmit，请使用Screen.SendSpecial与"TN3270_ENTER"参数。
        
        Args:
            string (str): 描述特殊SecureCRT或协议功能的字符串
        """
        self.obj.SendSpecial(string)

    def WaitForCursor(self, timeout: int = 0, bMilliseconds: bool = False) -> bool:
        """
        等待光标位置改变。
        
        可选的timeout参数指定等待更改的秒数或毫秒数（取决于bMilliseconds参数）。
        如果检测到光标位置改变，WaitForCursor()返回True。
        如果发生超时，函数返回False。
        如果未指定超时，WaitForCursor()将不会超时。
        如果没有打开连接，将返回错误。
        
        Args:
            timeout (int, optional): 等待超时的秒数或毫秒数。默认为0，表示无超时
            bMilliseconds (bool, optional): timeout是否以毫秒为单位。默认为False，表示以秒为单位
            
        Returns:
            bool: 如果检测到光标位置改变，返回True；如果超时，返回False
        """
        return self.obj.WaitForCursor(timeout, bMilliseconds)

    def WaitForKey(self, timeout: int = 0, bMilliseconds: bool = False) -> bool:
        """
        等待按键事件。
        
        可选的timeout参数指定等待按键事件的秒数或毫秒数（取决于bMilliseconds参数）。
        如果检测到按键事件，WaitForKey()返回True。
        如果发生超时，函数返回False。
        如果未指定超时，WaitForKey()将不会超时。
        如果没有打开连接，将返回错误。
        
        Args:
            timeout (int, optional): 等待超时的秒数或毫秒数。默认为0，表示无超时
            bMilliseconds (bool, optional): timeout是否以毫秒为单位。默认为False，表示以秒为单位
            
        Returns:
            bool: 如果检测到按键事件，返回True；如果超时，返回False
        """
        return self.obj.WaitForKey(timeout, bMilliseconds)

    def WaitForString(self, string: str, timeout: int = 0, bCaseInsensitive: bool = False, bMilliseconds: bool = False) -> bool:
        """
        等待指定字符串出现在输入中。
        
        当在输入中检测到字符串时，WaitForString()返回True。
        如果发生超时，函数返回False。
        如果没有打开连接，将返回错误。
        
        不支持等待包含转义序列的字符串。
        
        Args:
            string (str): 要等待的字符串
            timeout (int, optional): 等待超时的秒数或毫秒数。默认为0，表示无超时
            bCaseInsensitive (bool, optional): 是否忽略大小写。默认为False，即区分大小写
            bMilliseconds (bool, optional): timeout是否以毫秒为单位。默认为False，表示以秒为单位
            
        Returns:
            bool: 如果找到指定字符串，返回True；如果超时，返回False
        """
        return self.obj.WaitForString(string, timeout, bCaseInsensitive, bMilliseconds)

    def WaitForStrings(self, strings: List[str], timeout: int = 0, bCaseInsensitive: bool = False, bMilliseconds: bool = False) -> int:
        """
        等待多个字符串中的一个出现在输入中。
        
        当其中一个字符串在输入中匹配时，WaitForStrings()返回找到的字符串的参数索引
        （WaitForStrings()的第一个字符串参数的索引为1）。
        如果指定了可选的timeout参数并且在找到任何字符串之前发生超时，WaitForStrings()返回0。
        如果没有timeout参数，WaitForStrings()将无限期阻塞，不会超时，也不会返回0。
        如果没有打开连接，将返回错误。
        
        WaitForString(s)接口可以处理MBCS语言，并且只依赖于会话的"字符编码"能够表示正在等待的字符，
        而不依赖于字符在屏幕上正确显示。
        
        不支持等待包含转义序列的字符串。
        
        Args:
            strings (List[str]): 要等待的字符串列表
            timeout (int, optional): 等待超时的秒数或毫秒数。默认为0，表示无超时
            bCaseInsensitive (bool, optional): 是否忽略大小写。默认为False，即区分大小写
            bMilliseconds (bool, optional): timeout是否以毫秒为单位。默认为False，表示以秒为单位
            
        Returns:
            int: 找到的字符串在列表中的索引（从1开始），如果超时则返回0
        """
        return self.obj.WaitForStrings(strings, timeout, bCaseInsensitive, bMilliseconds)
