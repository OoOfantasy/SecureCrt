from typing import Any

class Arguments:
    """
    Arguments 对象允许脚本访问通过一个或多个 SecureCRT /ARG 命令行选项传递给脚本的参数。
    
    SecureCRT 的 /ARG 命令行选项允许您编写通用脚本，其中脚本使用的特定值（如主机名或端口）
    通过 SecureCRT 命令行传递给脚本。脚本参数作为参数传递给每个 /ARG <参数> 选项。
    
    示例：
    SecureCRT.exe /ARG myhostname /ARG 5555
    
    然后在脚本中可以通过 crt.Arguments 对象访问这些参数：
    hostname = crt.Arguments.GetArg(0)  # 或 crt.Arguments[0]
    port = crt.Arguments.GetArg(1)      # 或 crt.Arguments[1]
    """
    def __init__(self, crt):
        self.crt = crt

    @property
    def Count(self) -> int:
        """
        返回使用 SecureCRT 的 /ARG 命令行选项传递给 SecureCRT 的参数数量。
        
        这是一个只读数值属性。
        如果 SecureCRT 启动时没有 /ARG 命令行选项，则 crt.Arguments.Count 属性设置为 0。
        
        使用示例：
        if crt.Arguments.Count < 2:
            crt.Dialog.MessageBox("此脚本需要至少两个参数")
            return
            
        Returns:
            int: 传递给 SecureCRT 的参数数量
        """
        return self.crt.Arguments.Count

    def GetArg(self, number: int) -> str:
        """
        返回与传递给 SecureCRT 的每个 /ARG 命令行选项关联的参数数据。
        
        GetArg 方法返回传递给 SecureCRT 的数据。通过调用 GetArg(0) 检索传递给 SecureCRT 的第一个参数。
        最后一个参数通过传递 crt.Arguments.Count 减 1 来检索。
        
        注意：GetArg 方法是 Arguments 对象上的默认方法，因此如果未命名，将隐式调用它。
        这意味着以下两个语句是等效的：
        
        MsgBox crt.Arguments.GetArg(0)
        MsgBox crt.Arguments(0)
        
        Python 中，可以使用索引语法访问参数：crt.Arguments[0]
        
        使用示例：
        hostname = crt.Arguments.GetArg(0)
        port = crt.Arguments.GetArg(1)
        
        Args:
            number (int): 参数的索引，从 0 开始
            
        Returns:
            str: 与指定索引关联的参数数据
            
        Raises:
            IndexError: 如果索引超出参数数量范围
        """
        return self.crt.Arguments.GetArg(number)

    def __getitem__(self, index: int) -> str:
        """
        允许使用索引符号访问参数，如 crt.Arguments[0]。
        
        这是一个 Python 特有的方法，提供更符合 Python 习惯的访问语法。
        
        Args:
            index (int): 参数的索引，从 0 开始
            
        Returns:
            str: 与指定索引关联的参数数据
            
        Raises:
            IndexError: 如果索引超出参数数量范围
        """
        return self.GetArg(index)
