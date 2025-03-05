class FileTransfer:
    def __init__(self, crt):
        self.file_transfer = crt.FileTransfer

    @property
    def DownloadFolder(self) -> str:
        """返回当前会话的下载文件夹路径"""
        return self.file_transfer.DownloadFolder

    @property
    def ZmodemUploadAscii(self) -> bool:
        """返回或设置Zmodem上传的ASCII模式"""
        return self.file_transfer.ZmodemUploadAscii

    @ZmodemUploadAscii.setter
    def ZmodemUploadAscii(self, value: bool) -> None:
        self.file_transfer.ZmodemUploadAscii = value

    def AddToUploadList(self, filepath: str) -> None:
        """将文件添加到Y/Zmodem或Kermit上传列表"""
        self.file_transfer.AddToUploadList(filepath)

    def ClearUploadList(self) -> None:
        """清除Y/Zmodem或Kermit上传列表"""
        self.file_transfer.ClearUploadList()

    def ReceiveKermit(self) -> None:
        """启动Kermit下载"""
        self.file_transfer.ReceiveKermit()

    def ReceiveXmodem(self, filepath: str) -> None:
        """启动Xmodem下载"""
        self.file_transfer.ReceiveXmodem(filepath)

    def ReceiveYmodem(self) -> None:
        """启动Ymodem下载"""
        self.file_transfer.ReceiveYmodem()

    def SendKermit(self) -> None:
        """使用Kermit协议发送指定文件"""
        self.file_transfer.SendKermit()

    def SendXmodem(self, filepath: str) -> None:
        """使用Xmodem协议发送指定文件"""
        self.file_transfer.SendXmodem(filepath)

    def SendYmodem(self) -> None:
        """使用Ymodem协议发送指定文件"""
        self.file_transfer.SendYmodem()
