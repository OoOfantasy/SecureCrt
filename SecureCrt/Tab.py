from typing import Any

class Tab:
    """
    Tab 对象提供对当前连接或会话的选项卡功能的访问。
    Tab 对象也可以用于处理平铺的会话窗口。
    
    通过 Tab 对象可以访问选项卡的属性（如标题、索引）和方法（如激活、克隆、关闭等）。
    """
    def __init__(self, obj):
        """
        初始化 Tab 对象
        
        Args:
            obj: SecureCRT Tab 对象
        """
        self.obj = obj

    @property
    def Caption(self) -> str:
        """
        返回或设置指定选项卡对象的标题。
        
        设置此属性会设置选项卡或平铺会话窗口的标题，如果选项卡或平铺会话窗口处于活动状态，
        还会设置主应用程序窗口的标题。可以通过右键单击会话选项卡上的名称并选择"重命名"来重命名选项卡。
        名称更改将一直有效，直到重新使用选项卡或 SecureCRT 退出。
        
        Returns:
            str: 选项卡的标题
        """
        return self.obj.Caption

    @Caption.setter
    def Caption(self, value: str):
        """
        设置选项卡的标题。
        
        Args:
            value (str): 新的选项卡标题
        """
        self.obj.Caption = value
    
    @property
    def Index(self) -> int:
        """
        返回对象引用的选项卡的索引。
        
        当会话以选项卡形式显示时，每个选项卡对象的索引与其在选项卡栏中的位置匹配。
        当会话平铺时，选项卡对象的索引可能与选项卡形式时的索引不匹配，但在会话保持平铺状态时索引将保持一致。
        
        Returns:
            int: 选项卡的索引
        """
        return self.obj.Index
    
    @property
    def Screen(self):
        """
        返回与选项卡对象关联的 Screen 对象的引用。
        
        Screen 对象提供对终端屏幕的访问，可以用于读取屏幕内容、发送命令等操作。
        有关其属性和方法的详细说明，请参阅 Screen 对象文档。
        
        Returns:
            Screen: 与选项卡关联的 Screen 对象
        """
        from .Screen import Screen
        return Screen(self.obj.Screen)
    
    @property
    def Session(self):
        """
        返回与选项卡对象关联的 Session 对象的引用。
        
        Session 对象提供对会话属性和方法的访问，如连接状态、路径、日志记录等。
        有关其属性和方法的详细说明，请参阅 Session 对象文档。
        
        Returns:
            Session: 与选项卡关联的 Session 对象
        """
        from .Session import Session
        return Session(self.obj.Session)

    def Activate(self):
        """
        将对象引用的选项卡或平铺会话窗口置于前台。
        
        无论选项卡是否处于活动状态，它都可以接收和发送文本。
        此方法模拟用户单击选项卡或平铺会话窗口以激活它。
        
        Returns:
            None
        """
        self.obj.Activate()

    def Clone(self):
        """
        从指定的对象选项卡引用克隆一个选项卡对象并返回其引用。
        
        克隆会话的好处是它们继承自父会话已经通过服务器身份验证。
        因此，克隆会话不需要额外的身份验证。
        
        Returns:
            Tab: 克隆的选项卡对象
        """
        clone_obj = self.obj.Clone()
        return Tab(clone_obj)

    def Close(self):
        """
        关闭对象引用的选项卡或平铺会话窗口。
        
        与对象引用的选项卡（或平铺会话窗口）相关联的任何活动连接在关闭选项卡（或平铺会话窗口）时将被终止。
        运行脚本的选项卡或平铺会话窗口不能被关闭。
        
        Returns:
            None
        """
        self.obj.Close()

    def ConnectSftp(self):
        """
        基于此选项卡创建一个 SFTP 选项卡。在平铺模式下，基于此平铺会话创建一个 SFTP 会话窗口。
        
        SFTP 会话的好处是它们继承自父会话已经通过服务器身份验证。
        因此，SFTP 会话不需要额外的身份验证。
        
        Returns:
            Tab: SFTP 选项卡对象
        """
        sftp_obj = self.obj.ConnectSftp()
        return Tab(sftp_obj)

    def ResetCaption(self):
        """
        将标题重置为调用 Caption 设置之前的状态。
        
        这个方法会将选项卡标题恢复到默认值或之前设置的状态。
        
        Returns:
            None
        """
        self.obj.ResetCaption()
