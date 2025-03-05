class Tab:
    def __init__(self, obj):
        self.obj = obj

    @property
    def Caption(self) -> str:
        """ 返回/设置选项卡标题 """
        return self.obj.Caption

    @Caption.setter
    def Caption(self, value: str):
        self.obj.Caption = value
    
    @property
    def Index(self) -> int:
        """ 返回选项卡索引 """
        return self.obj.Index
    
    @property
    def Screen(self):
        """ 返回选项卡Screen对象 """
        from .Screen import Screen
        return Screen(self.obj)
    
    @property
    def Session(self):
        """ 返回选项卡Session对象 """
        from .Session import Session
        return Session(self.obj)

    def Activate(self):
        """ 置顶选项卡 """
        self.obj.Activate()

    def Clone(self):
        """ 克隆选项卡 """
        clone_obj = self.obj.Clone()
        return Tab(clone_obj)

    def Close(self):
        """ 关闭选项卡 """
        self.obj.Close()

    def ConnectSftp(self):
        """ 连接SFTP """
        sftp_obj = self.obj.ConnectSftp()
        return Tab(sftp_obj)

    def ResetCaption(self):
        """ 重置选项卡标题 """
        self.obj.ResetCaption()