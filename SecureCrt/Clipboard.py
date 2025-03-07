from typing import Any

class Clipboard:
    """
    Clipboard 对象提供对应用程序剪贴板的访问。
    
    通过 Clipboard 对象可以读取和修改剪贴板的内容，以及设置剪贴板的格式。
    
    SecureCRT 的 Clipboard 对象通过顶级对象的 Clipboard 属性访问。
    """
    def __init__(self, crt):
        """
        初始化 Clipboard 对象
        
        Args:
            crt: SecureCRT 对象
        """
        self.crt = crt
    
    @property
    def CF_OEMTEXT(self) -> str:
        """
        返回 CF_OEMTEXT 剪贴板格式的格式字符串。
        
        此文本格式包含 OEM 字符集中的字符。每行以回车/换行(CR-LF)组合结束。
        空字符表示数据结束。
        
        注意：此格式仅在 Windows 上支持。
        
        Returns:
            str: CF_OEMTEXT 剪贴板格式的格式字符串
        """
        return self.crt.Clipboard.CF_OEMTEXT
    
    @property
    def CF_TEXT(self) -> str:
        """
        返回 CF_TEXT 剪贴板格式的格式字符串。
        
        在此文本格式中，每行以回车/换行(CR-LF)组合结束。
        空字符表示数据结束。使用此格式处理 ANSI 文本。
        
        注意：此格式仅在 Windows 上支持。
        
        Returns:
            str: CF_TEXT 剪贴板格式的格式字符串
        """
        return self.crt.Clipboard.CF_TEXT
    
    @property
    def CF_UNICODETEXT(self) -> str:
        """
        返回 CF_UNICODETEXT 剪贴板格式的格式字符串。
        
        在 Unicode 文本格式中，每行以回车/换行(CR-LF)组合结束。
        空字符表示数据结束。
        
        此格式在 Windows 和 macOS 上均受支持。
        
        Returns:
            str: CF_UNICODETEXT 剪贴板格式的格式字符串
        """
        return self.crt.Clipboard.CF_UNICODETEXT
    
    @property
    def DEFAULTFORMAT(self) -> str:
        """
        返回 DEFAULTFORMAT 剪贴板格式的格式字符串。
        
        将格式设置为此属性会将值恢复为剪贴板的全局默认格式。
        
        Returns:
            str: DEFAULTFORMAT 剪贴板格式的格式字符串
        """
        return self.crt.Clipboard.DEFAULTFORMAT
    
    @property
    def VDS_TEXT(self) -> str:
        """
        返回 VDS_TEXT 剪贴板格式的格式字符串。
        
        这是一种私有剪贴板格式，在将数据从屏幕复制到剪贴板时，
        会将某些特殊字符转换为 ASCII。转换的字符如下：
        
        - 定向引号（也称为"智能引号"）更改为 ASCII 引号
        - "全角破折号"更改为连字符
        - "半角破折号"更改为连字符
        
        此格式在 Windows 和 macOS 上均受支持。
        
        Returns:
            str: VDS_TEXT 剪贴板格式的格式字符串
        """
        return self.crt.Clipboard.VDS_TEXT
    
    @property
    def Format(self) -> str:
        """
        返回或设置剪贴板格式。
        
        Windows 上可能的格式有：CF_TEXT、CF_OEMTEXT、CF_UNICODETEXT 和 VDS_TEXT。
        macOS 上可能的格式有：CF_UNICODETEXT 和 VDS_TEXT。
        
        以下命令将值恢复为剪贴板的全局格式：
        crt.Clipboard.Format = crt.Clipboard.DEFAULTFORMAT
        
        示例：
            # 获取当前剪贴板格式
            format = crt.Clipboard.Format
            
            # 将剪贴板格式设置为 VDS_TEXT
            crt.Clipboard.Format = crt.Clipboard.VDS_TEXT
            
            # 恢复原始剪贴板格式
            crt.Clipboard.Format = format
        
        Returns:
            str: 当前剪贴板格式
        """
        return self.crt.Clipboard.Format
    
    @Format.setter
    def Format(self, value: str) -> None:
        """
        设置剪贴板格式。
        
        Args:
            value (str): 要设置的剪贴板格式。可以是 CF_TEXT、CF_OEMTEXT、
                        CF_UNICODETEXT、VDS_TEXT 或 DEFAULTFORMAT 之一。
        """
        self.crt.Clipboard.Format = value
    
    @property
    def Text(self) -> str:
        """
        返回或设置剪贴板的内容。
        
        可以用于读取剪贴板的当前内容或将新内容写入剪贴板。
        
        示例：
            # 将选定的文本放入剪贴板
            crt.Clipboard.Text = crt.Screen.Selection
            
            # 将剪贴板中的文本传输到变量中以供脚本内使用
            MyStr = crt.Clipboard.Text
            
            # 将剪贴板的内容发送到远程机器
            crt.Screen.Send(crt.Clipboard.Text)
        
        Returns:
            str: 剪贴板的当前内容
        """
        return self.crt.Clipboard.Text
    
    @Text.setter
    def Text(self, value: str) -> None:
        """
        设置剪贴板的内容。
        
        Args:
            value (str): 要写入剪贴板的文本内容
        """
        self.crt.Clipboard.Text = value
