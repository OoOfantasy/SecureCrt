class Clipboard:
    def __init__(self, crt):
        self.clipboard = crt.Clipboard

    @property
    def Format(self) -> str:
        """ 返回或设置剪贴板格式 """
        return self.clipboard.Format

    @Format.setter
    def Format(self, value: str) -> None:
        self.clipboard.Format = value

    @property
    def CF_OEMTEXT(self) -> str:
        """ 返回 CF_OEMTEXT 剪贴板格式字符串 """
        return self.clipboard.CF_OEMTEXT

    @property
    def CF_TEXT(self) -> str:
        """ 返回 CF_TEXT 剪贴板格式字符串 """
        return self.clipboard.CF_TEXT

    @property
    def CF_UNICODETEXT(self) -> str:
        """ 返回 CF_UNICODETEXT 剪贴板格式字符串 """
        return self.clipboard.CF_UNICODETEXT

    @property
    def DEFAULTFORMAT(self) -> str:
        """ 返回 DEFAULTFORMAT 剪贴板格式字符串 """
        return self.clipboard.DEFAULTFORMAT

    @property
    def VDS_TEXT(self) -> str:
        """ 返回 VDS_TEXT 剪贴板格式字符串 """
        return self.clipboard.VDS_TEXT

    @property
    def Text(self) -> str:
        """ 返回或设置剪贴板内容 """
        return self.clipboard.Text

    @Text.setter
    def Text(self, value: str) -> None:
        self.clipboard.Text = value
