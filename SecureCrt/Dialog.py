from typing import List, Union, Optional, Tuple

class Dialog:
    """
    Dialog对象提供对SecureCRT简单用户界面功能的访问。
    通过Dialog对象可以显示文件选择对话框、保存对话框、消息框和输入提示框。
    """
    
    # MessageBox 常量
    # 图标常量
    ICON_STOP = 16       # 显示错误/停止图标
    ICON_QUESTION = 32   # 显示问号图标
    ICON_WARN = 48       # 显示感叹号图标
    ICON_INFO = 64       # 显示信息图标
    
    # 按钮常量
    BUTTON_OK = 0                # 仅显示确定按钮
    BUTTON_CANCEL = 1            # 显示确定和取消按钮
    BUTTON_ABORTRETRYIGNORE = 2  # 显示中止、重试和忽略按钮
    BUTTON_YESNOCANCEL = 3       # 显示是、否和取消按钮
    BUTTON_YESNO = 4             # 显示是和否按钮
    BUTTON_RETRYCANCEL = 5       # 显示重试和取消按钮
    
    # 默认按钮常量
    DEFBUTTON1 = 0       # 第一个按钮是默认按钮
    DEFBUTTON2 = 256     # 第二个按钮是默认按钮
    DEFBUTTON3 = 512     # 第三个按钮是默认按钮
    
    # MessageBox 返回值常量
    IDOK = 1             # 确定按钮被点击
    IDCANCEL = 2         # 取消按钮被点击
    IDABORT = 3          # 中止按钮被点击
    IDRETRY = 4          # 重试按钮被点击
    IDIGNORE = 5         # 忽略按钮被点击
    IDYES = 6            # 是按钮被点击
    IDNO = 7             # 否按钮被点击
    
    def __init__(self, crt):
        """
        初始化Dialog对象
        
        Args:
            crt: SecureCRT对象
        """
        self.crt = crt

    def FileOpenDialog(self, title: str = "浏览文件", buttonLabel: str = "", 
                       defaultfilename: str = "", filter: str = "所有文件(*.*)|*.*||") -> str:
        """
        显示文件浏览对话框，让用户可以选择单个文件。所选文件必须存在。
        
        如果defaultFilename参数仅是文件名（未提供路径），则文件对话框浏览器将在当前工作目录中打开。
        如果defaultFilename参数指定了文件的绝对路径，则文件对话框浏览器将在该文件的父目录中打开。
        
        文件名过滤器格式如下：
        <过滤器名称> (*.<扩展名>)|*.<扩展名>||
        
        例如：
        "文本文件 (*.txt)|*.txt||"
        或
        "文本文件 (*.txt)|*.txt|日志文件 (*.log)|*.log||"
        
        Args:
            title (str, optional): 对话框标题。默认为"浏览文件"
            buttonLabel (str, optional): 按钮文本。默认为空字符串
            defaultfilename (str, optional): 默认文件名/路径。默认为空字符串
            filter (str, optional): 文件类型过滤器。默认为"所有文件(*.*)|*.*||"
            
        Returns:
            str: 选择的文件完整路径，如果用户取消则返回空字符串
        """
        return self.crt.Dialog.FileOpenDialog(title, buttonLabel, defaultfilename, filter)

    def FileSaveDialog(self, title: str = "保存文件", buttonLabel: str = "", 
                       defaultfilename: str = "", filter: str = "所有文件(*.*)|*.*||") -> str:
        """
        显示文件保存对话框，让用户可以选择单个文件进行保存。
        
        如果defaultFilename参数仅是文件名（未提供路径），则文件对话框浏览器将在当前工作目录中打开。
        如果defaultFilename参数指定了文件的绝对路径，则文件对话框浏览器将在该文件的父目录中打开。
        
        文件名过滤器格式如下：
        <过滤器名称> (*.<扩展名>)|*.<扩展名>||
        
        例如：
        "文本文件 (*.txt)|*.txt||"
        或
        "文本文件 (*.txt)|*.txt|日志文件 (*.log)|*.log||"
        
        Args:
            title (str, optional): 对话框标题。默认为"保存文件"
            buttonLabel (str, optional): 按钮文本。默认为空字符串
            defaultfilename (str, optional): 默认文件名/路径。默认为空字符串
            filter (str, optional): 文件类型过滤器。默认为"所有文件(*.*)|*.*||"
            
        Returns:
            str: 选择的文件完整路径，如果用户取消则返回空字符串
        """
        return self.crt.Dialog.FileSaveDialog(title, buttonLabel, defaultfilename, filter)

    def MessageBox(self, message: str, title: str = "提示", 
                   buttons: Union[List[int], int] = None) -> int:
        """
        显示消息对话框。
        
        MessageBox函数向用户显示一个消息字符串。可选的title参数设置MessageBox的标题或标题栏文本。
        通过在可选的'buttons'参数中传递数值组合，可以配置MessageBox上显示的按钮。
        默认情况下，MessageBox将显示带有"确定"按钮的消息字符串。
        
        buttons参数可以是以下值的组合：
        - 图标: ICON_STOP(16):错误, ICON_QUESTION(32):问号, ICON_WARN(48):感叹号, ICON_INFO(64):信息
        - 按钮: BUTTON_OK(0):仅确定, BUTTON_CANCEL(1):确定&取消, 
               BUTTON_ABORTRETRYIGNORE(2):中止&重试&忽略, 
               BUTTON_YESNOCANCEL(3):是&否&取消, BUTTON_YESNO(4):是&否, 
               BUTTON_RETRYCANCEL(5):重试&取消
        - 默认按钮: DEFBUTTON1(0):第一个按钮默认, DEFBUTTON2(256):第二个按钮默认, 
                   DEFBUTTON3(512):第三个按钮默认
        
        MessageBox函数返回一个数值，可用于标识点击了哪个按钮：
        - IDOK(1):确定按钮被点击
        - IDCANCEL(2):取消按钮被点击
        - IDABORT(3):中止按钮被点击
        - IDRETRY(4):重试按钮被点击
        - IDIGNORE(5):忽略按钮被点击
        - IDYES(6):是按钮被点击
        - IDNO(7):否按钮被点击
        
        Args:
            message (str): 要显示的消息文本
            title (str, optional): 对话框标题。默认为"提示"
            buttons (Union[List[int], int], optional): 按钮和图标配置。
                可以是整数或整数列表。如果是列表，会将列表中的值组合起来。
                默认为[ICON_INFO, BUTTON_OK, DEFBUTTON1]
                
        Returns:
            int: 点击的按钮对应的值
        """
        if buttons is None:
            buttons = [self.ICON_INFO, self.BUTTON_OK, self.DEFBUTTON1]
            
        if isinstance(buttons, list):
            button_value = 0
            for b in buttons:
                button_value |= b
        else:
            button_value = buttons
            
        return self.crt.Dialog.MessageBox(message, title, button_value)

    def Prompt(self, message: str, title: str = "提示", default: str = "", 
               isPassword: bool = False) -> str:
        """
        提示用户输入字符串。
        
        Prompt函数显示一个简单的对话框，其中包含消息和一个用于用户输入字符串的编辑字段。
        message参数是显示在提示对话框中的信息字符串。
        可以通过传递title字符串来设置提示对话框的标题。
        默认情况下编辑字段为空，但可以使用可选的default字符串设置编辑字段的初始内容。
        最后，如果在输入时要隐藏编辑字段中输入的文本（例如在输入密码时），
        则应将布尔值isPassword字段设置为True。
        
        如果用户点击确定，Prompt返回输入的字符串；如果用户点击取消，Prompt返回空字符串。
        
        Args:
            message (str): 提示消息文本
            title (str, optional): 对话框标题。默认为"提示"
            default (str, optional): 输入框默认值。默认为空字符串
            isPassword (bool, optional): 是否为密码输入（隐藏文本）。默认为False
            
        Returns:
            str: 用户输入的字符串，如果用户取消则返回空字符串
        """
        return self.crt.Dialog.Prompt(message, title, default, isPassword)
