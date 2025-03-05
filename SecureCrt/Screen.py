class Screen:
    def __init__(self, obj):
        self.obj = obj

    @property
    def CurrentColumn(self) -> int:
        """返回光标的当前列"""
        return self.obj.CurrentColumn

    @property
    def CurrentRow(self) -> int:
        """返回光标的当前行"""
        return self.obj.CurrentRow

    @property
    def Columns(self) -> int:
        """返回当前列数"""
        return self.obj.Columns

    @property
    def IgnoreEscape(self) -> bool:
        """获取或设置是否忽略转义序列"""
        return self.obj.IgnoreEscape

    @IgnoreEscape.setter
    def IgnoreEscape(self, value: bool) -> None:
        self.obj.IgnoreEscape = value

    @property
    def MatchIndex(self) -> int:
        """获取匹配的索引"""
        return self.obj.MatchIndex

    @property
    def Rows(self) -> int:
        """返回当前行数"""
        return self.obj.Rows

    @property
    def Selection(self) -> str:
        """返回当前选择"""
        return self.obj.Selection

    @property
    def Synchronous(self) -> bool:
        """获取或设置同步设置"""
        return self.obj.Synchronous

    @Synchronous.setter
    def Synchronous(self, value: bool) -> None:
        self.obj.Synchronous = value

    def Clear(self) -> None:
        """清除屏幕"""
        self.obj.Clear()

    def Get(self, row1: int, col1: int, row2: int, col2: int) -> str:
        """返回屏幕部分的字符"""
        return self.obj.Get(row1, col1, row2, col2)

    def Get2(self, row1: int, col1: int, row2: int, col2: int) -> str:
        """返回每行请求的字符"""
        return self.obj.Get2(row1, col1, row2, col2)

    def IgnoreCase(self) -> None:
        """设置全局方法以忽略大小写"""
        self.obj.IgnoreCase()

    def Print(self) -> None:
        """打印屏幕"""
        self.obj.Print()

    def ReadString(self, strings=None, timeoutSeconds=0, bCaseInsensitive=False) -> str:
        """捕获从远程接收的数据"""
        return self.obj.ReadString(strings, timeoutSeconds, bCaseInsensitive)

    def Send(self, string: str, bSendToScreenOnly=False, bEncode=True) -> None:
        """发送字符串"""
        self.obj.Send(string, bSendToScreenOnly, bEncode)

    def SendKeys(self, string: str) -> None:
        """发送按键"""
        self.obj.SendKeys(string)

    def SendSpecial(self, string: str) -> None:
        """发送内置的 SecureCRT 命令"""
        self.obj.SendSpecial(string)

    def WaitForCursor(self, timeout=0, bMilliseconds=False) -> bool:
        """等待光标位置变化"""
        return self.obj.WaitForCursor(timeout, bMilliseconds)

    def WaitForKey(self, timeout=0, bMilliseconds=False) -> bool:
        """等待按键事件"""
        return self.obj.WaitForKey(timeout, bMilliseconds)

    def WaitForString(self, string: str, timeout=0, bCaseInsensitive=False, bMilliseconds=False) -> bool:
        """等待字符串"""
        return self.obj.WaitForString(string, timeout, bCaseInsensitive, bMilliseconds)

    def WaitForStrings(self, strings, timeout=0, bCaseInsensitive=False, bMilliseconds=False) -> int:
        """等待多个字符串中的一个"""
        return self.obj.WaitForStrings(strings, timeout, bCaseInsensitive, bMilliseconds)