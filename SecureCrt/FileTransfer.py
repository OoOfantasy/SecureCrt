from typing import Optional

class FileTransfer:
    """
    FileTransfer 对象提供了通过脚本执行文件传输的方法。
    
    通过 FileTransfer 对象可以执行各种文件传输操作，包括文件上传和下载，
    以及支持 Xmodem、Ymodem 和 Kermit 等多种传输协议。
    
    SecureCRT 的 FileTransfer 对象通过顶级对象的 FileTransfer 属性访问。
    注意：FileTransfer 对象不支持使用 TN3270 模拟的会话。
    """
    def __init__(self, crt):
        """
        初始化 FileTransfer 对象
        
        Args:
            crt: SecureCRT 对象
        """
        self.crt = crt

    @property
    def DownloadFolder(self) -> str:
        """
        返回当前会话的下载文件夹路径。
        
        这是一个只读属性，返回当前会话下载文件夹的路径。
        通过 Xmodem、Ymodem 或 Kermit 下载的文件总是放置在会话的下载文件夹中。
        脚本可以使用此属性确定下载文件的位置。
        
        Returns:
            str: 当前会话的下载文件夹路径
        """
        return self.crt.FileTransfer.DownloadFolder

    @property
    def ZmodemUploadAscii(self) -> bool:
        """
        指定 Zmodem 上传使用 ASCII 模式还是二进制模式。
        
        当 ZmodemUploadAscii 设置为 True 时，上传将以 ASCII 格式进行。
        在运行将 ZmodemUploadAscii 选项设置为 True 的脚本后，
        该设置将作为会话选项保存，直到通过运行另一个将其重置为 False 的脚本
        或通过在"使用 Zmodem 发送文件"对话框中更改选项来更改它。
        
        注意：要使此选项正常工作，远程机器上的 Zmodem 安装必须能够将 ASCII 
        转换为使用本地换行符约定。
        
        Returns:
            bool: True 表示使用 ASCII 模式，False 表示使用二进制模式
        """
        return self.crt.FileTransfer.ZmodemUploadAscii

    @ZmodemUploadAscii.setter
    def ZmodemUploadAscii(self, value: bool) -> None:
        """
        设置 Zmodem 上传是否使用 ASCII 模式。
        
        Args:
            value (bool): True 表示使用 ASCII 模式，False 表示使用二进制模式
        """
        self.crt.FileTransfer.ZmodemUploadAscii = value

    def AddToUploadList(self, filepath: str) -> None:
        """
        将文件添加到 Y/Zmodem 或 Kermit 上传列表。
        
        AddToUploadList 将指定文件放置在文件列表中，这些文件将在下一次 Y/Zmodem 
        或 Kermit 上传期间上传。一旦将一个或多个文件添加到上传列表中，
        脚本可以通过向远程系统发送适当的命令来启动 Y/Zmodem 或 Kermit 上传。
        
        错误：
        如果提供给 AddToUploadList 的路径不是有效文件，则会生成脚本错误并显示以下消息：
        "FileTransfer.AddToUploadList: <filepath> does not exist."
        
        示例：
            crt.FileTransfer.AddToUploadList("c:\\temp\\File1.txt")
            crt.FileTransfer.AddToUploadList("c:\\temp\\File2.txt")
            crt.Screen.Send("rz\\n")  # 启动上传这两个文件
        
        Args:
            filepath (str): 要添加到上传列表的文件的完整路径
        """
        self.crt.FileTransfer.AddToUploadList(filepath)

    def ClearUploadList(self) -> None:
        """
        清除 Y/Zmodem 或 Kermit 上传列表。
        
        此方法清除之前通过 AddToUploadList 添加到上传队列中的所有文件。
        
        示例：
            crt.FileTransfer.ClearUploadList()
        """
        self.crt.FileTransfer.ClearUploadList()

    def ReceiveKermit(self) -> None:
        """
        启动 Kermit 下载到下载文件夹。
        
        ReceiveKermit 启动从远程主机下载一个或多个文件的 Kermit 下载。
        下载的文件始终放置在会话的下载文件夹中。注意，应在执行 ReceiveKermit 
        之前在远程系统上发送或启动 Kermit 发送命令，以便传输正常进行。
        
        错误：
        1. 如果在未连接时执行 ReceiveKermit 方法，则会生成以下脚本错误：
           "FileTransfer.ReceiveKermit: not connected"
        
        2. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.ReceiveKermit: A file transfer cannot be started while another transfer is in progress"
           
        示例：
            crt.Screen.Send("-kermit myFile.txt\\n")
            crt.Screen.WaitForString("-kermit myFile.txt\\n")
            crt.FileTransfer.ReceiveKermit()
        """
        self.crt.FileTransfer.ReceiveKermit()

    def ReceiveXmodem(self, filepath: str) -> None:
        """
        启动 Xmodem 下载到下载文件夹。
        
        ReceiveXmodem 启动文件的 Xmodem 下载，并将文件保存为会话下载文件夹中指定的文件名。
        下载的文件始终放置在会话的下载文件夹中。注意，应在执行 ReceiveXmodem 
        之前在远程系统上发送或启动 Xmodem 发送命令，以便传输正常进行。
        
        错误：
        1. 如果在未连接时执行 ReceiveXmodem 方法，则会生成以下脚本错误：
           "FileTransfer.ReceiveXmodem: not connected"
           
        2. 如果传递给 ReceiveXmodem 的文件名不是简单文件名（即，如果它是路径或包含路径分隔符），
           则会生成以下脚本错误：
           "FileTransfer.ReceiveXmodem: Invalid filename \"%s\". Argument should not include path information."
           
        3. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.ReceiveXmodem: A file transfer cannot be started while another transfer is in progress"
        
        示例：
            crt.Screen.Send("sx -X myFile.txt\\n")
            # 自定义下面的等待字符串以匹配远程 Xmodem 程序的输出。
            crt.Screen.WaitForString("Give your local XMODEM receive command now.")
            crt.FileTransfer.ReceiveXmodem("yourFile.txt")
            
        注意：当使用 WaitForString 命令（如上例所示）时，等待的字符串应该是精确的 Xmodem 输出，
        包括回车符和换行符。
            
        Args:
            filepath (str): 保存下载文件的文件名（不包含路径信息）
        """
        self.crt.FileTransfer.ReceiveXmodem(filepath)

    def ReceiveYmodem(self) -> None:
        """
        启动 Ymodem 下载到下载文件夹。
        
        ReceiveYmodem 启动从远程主机下载一个或多个文件的 Ymodem 下载。
        下载的文件始终放置在会话的下载文件夹中。注意，应在执行 ReceiveYmodem 
        之前在远程系统上发送或启动 Ymodem 发送命令，以便传输正常进行。
        
        错误：
        1. 如果在未连接时执行 ReceiveYmodem 方法，则会生成以下脚本错误：
           "FileTransfer.ReceiveYmodem: not connected"
           
        2. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.ReceiveYmodem: A file transfer cannot be started while another transfer is in progress"
        
        示例：
            crt.Screen.Send("sz -ymodem myFile.txt\\n")
            crt.Screen.WaitForString("sz -ymodem myFile.txt\\r\\n")
            crt.FileTransfer.ReceiveYmodem()
        """
        self.crt.FileTransfer.ReceiveYmodem()

    def SendKermit(self) -> None:
        """
        使用 Kermit 协议发送指定文件。
        
        SendKermit 使用 Kermit 协议发送指定文件。注意，应在执行 SendKermit 
        之前在远程系统上发送或启动适当的 Kermit 接收命令，以便传输正常开始。
        
        错误：
        1. 如果在未连接时执行 SendKermit 方法，则会生成以下脚本错误：
           "FileTransfer.SendKermit: not connected"
           
        2. 如果文件列表为空，则会生成以下脚本错误：
           "FileTransfer.SendKermit: No files were specified for transfer."
           
        3. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.SendKermit: A file transfer cannot be started while another transfer is in progress"
        
        示例：
            # 使用 Kermit 上传多个文件
            crt.FileTransfer.AddToUploadList("c:\\temp\\File1.txt")
            crt.FileTransfer.AddToUploadList("c:\\temp\\File2.txt")
            crt.FileTransfer.AddToUploadList("c:\\temp\\File3.txt")
            
            crt.Screen.Send("--kermit\\n")
            crt.FileTransfer.SendKermit()
        """
        self.crt.FileTransfer.SendKermit()

    def SendXmodem(self, filepath: str) -> None:
        """
        使用 Xmodem 协议发送指定文件。
        
        SendXmodem 使用 Xmodem 协议发送指定文件。必须指定文件的完整路径。
        注意，应在执行 SendXmodem 之前在远程系统上发送或启动适当的 Xmodem 接收命令，
        以便传输正常开始。
        
        错误：
        1. 如果在未连接时执行 SendXmodem 方法，则会生成以下脚本错误：
           "FileTransfer.SendXmodem: not connected"
           
        2. 如果提供给 SendXmodem 的路径不是有效文件，则会生成脚本错误并显示以下消息：
           "FileTransfer.SendXmodem: <filepath> does not exist."
           
        3. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.SendXmodem: A file transfer cannot be started while another transfer is in progress"
        
        示例：
            # 使用 Xmodem 上传 C:\\temp\\myFile.txt
            crt.Screen.Send("rx myFile.txt\\n")
            crt.Screen.WaitForString("ready to receive")
            crt.FileTransfer.SendXmodem("C:\\temp\\myFile.txt")
            
        Args:
            filepath (str): 要发送的文件的完整路径
        """
        self.crt.FileTransfer.SendXmodem(filepath)

    def SendYmodem(self) -> None:
        """
        使用 Ymodem 协议发送指定文件。
        
        SendYmodem 使用 Ymodem 协议发送指定文件。注意，应在执行 SendYmodem 
        之前在远程系统上发送或启动适当的 Ymodem 接收命令，以便传输正常开始。
        
        错误：
        1. 如果在未连接时执行 SendYmodem 方法，则会生成以下脚本错误：
           "FileTransfer.SendYmodem: not connected"
           
        2. 如果文件列表为空，则会生成以下脚本错误：
           "FileTransfer.SendYmodem: No files were specified for transfer."
           
        3. 如果在调用此方法时已有传输正在进行，则会生成以下脚本错误：
           "FileTransfer.SendYmodem: A file transfer cannot be started while another transfer is in progress"
        
        示例：
            # 使用 Ymodem 上传多个文件
            crt.FileTransfer.AddToUploadList("c:\\temp\\File1.txt")
            crt.FileTransfer.AddToUploadList("c:\\temp\\File2.txt")
            crt.FileTransfer.AddToUploadList("c:\\temp\\File3.txt")
            
            crt.Screen.Send("rz --ymodem\\n")
            crt.FileTransfer.SendYmodem()
        """
        self.crt.FileTransfer.SendYmodem()
