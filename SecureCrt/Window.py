from typing import Union

class Window:
    """
    Window 对象提供对 SecureCRT 窗口属性和方法的访问。
    
    通过 Window 对象可以控制窗口的可见状态、标题栏文本等属性，
    以及执行窗口激活和显示状态更改等操作。
    
    SecureCRT 的 Window 对象通过顶级对象的 Window 属性访问。
    """
    def __init__(self, obj):
        """
        初始化 Window 对象
        
        Args:
            crt: SecureCRT 对象
        """
        self.obj = obj

    @property
    def Active(self) -> bool:
        """
        返回一个布尔值，表示 SecureCRT 的窗口是否是活动窗口。
        
        这是一个只读属性。如果 SecureCRT 窗口是当前活动的窗口，则返回 True，
        否则返回 False。在 Linux 系统上，即使 SecureCRT 图标正在闪烁，
        也可能返回 False。
        
        Returns:
            bool: True 表示 SecureCRT 窗口是活动窗口，False 表示不是
        """
        return self.obj.Active

    @property
    def Caption(self) -> str:
        """
        返回或设置 SecureCRT 应用程序窗口的标题或标题栏文本。
        
        这是一个可读写的属性。可以通过此属性获取当前窗口标题，
        或者为窗口设置一个新的标题文本。
        
        Returns:
            str: SecureCRT 应用程序窗口的标题文本
        """
        return self.obj.Caption

    @Caption.setter
    def Caption(self, value: str) -> None:
        """
        设置 SecureCRT 应用程序窗口的标题。
        
        Args:
            value (str): 要设置的新窗口标题文本
        """
        self.obj.Caption = value

    @property
    def State(self) -> int:
        """
        返回一个数字，表示 SecureCRT 应用程序窗口的状态。
        
        这是一个只读属性。返回的状态值可能是以下几种，具体取决于 SecureCRT 窗口的状态：
        - 0：隐藏
        - 1：可见（正常）
        - 2：最小化
        - 3：最大化
        
        Returns:
            int: 表示 SecureCRT 应用程序窗口状态的数值
        """
        return self.obj.State

    def Activate(self) -> None:
        """
        将焦点赋予 SecureCRT 窗口，使窗口置于桌面顶部。
        
        在 Linux 系统上，从脚本调用 Activate() 可能会导致 SecureCRT 图标闪烁，
        而不是将 SecureCRT 置于顶部。这是该操作系统所要求的行为。
        """
        self.obj.Activate()

    def Show(self, state: int) -> None:
        """
        显示、隐藏、最小化或最大化 SecureCRT 应用程序窗口。
        
        state 参数可以是以下值之一：
        - 0：隐藏
        - 1：显示（正常）
        - 2：最小化
        - 3：最大化
        
        Args:
            state (int): 要设置的窗口状态
        """
        self.obj.Show(state)
