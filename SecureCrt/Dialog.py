from typing import List

class Dialog:
    def __init__(self, crt):
        self.dialog = crt.Dialog

    def FileOpenDialog(self, title: str="浏览文件", buttonLabel: str="", defaultfilename: str="", filter: str="所有文件(*.*)|*.*||") -> str:
        '''
         - 文件浏览窗口
            - title: 标题
            - buttonLabel: 按钮文本
            - defaultfilename: 默认文件名/路径
            - filter: 文件类型
        - return: 文件路径
        '''
        return self.dialog.FileOpenDialog(title, buttonLabel, defaultfilename, filter)

    def FileSaveDialog(self, title: str="保存文件", buttonLabel: str="", defaultfilename: str="", filter: str="所有文件(*.*)|*.*||") -> str:
        '''
         - 文件保存窗口
            - title: 标题
            - buttonLabel: 按钮文本
            - defaultfilename: 默认文件名/路径
            - filter: 文件类型
         - return: 文件路径
        '''
        return self.dialog.FileSaveDialog(title, buttonLabel, defaultfilename, filter)

    def MessageBox(self, message: str, title: str="提示", opt: List[int]=[64, 0, 0]) -> int:
        '''
        - 消息窗口
            - message: 文本
            - title: 标题
            - opt: 选项 [图标, 按钮, 默认按钮]
                - 图标: 16:error, 32:?, 48:!, 64:info
                - 按钮: 0:确定, 1:确定&取消, 2:中止&重试&忽略, 3:是&否&取消, 4:是&否, 5:重试&取消
                - 默认按钮: 0:第一个按钮默认, 256:第二个按钮默认, 512:第三个按钮默认
        - return: 按钮编号
            - 1: '确定', 2: '取消', 3: '中止', 4: '重试', 5: '忽略', 6: '是', 7: '否'
        '''
        return self.dialog.MessageBox(message, title, opt[0] | opt[1] | opt[2])

    def Prompt(self, message: str, default: str="", title: str="提示", isPassword: bool=False) -> str:
        '''
        - 输入窗口
            - message: 文本
            - default: 输入框默认值
            - title: 标题
            - isPassword: 是否密码输入
        - return: 输入的字符串或空字符串
        '''
        return self.dialog.Prompt(message, title, default, isPassword)