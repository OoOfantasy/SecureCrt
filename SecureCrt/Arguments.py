class Arguments:
    def __init__(self, args):
        self.args = args

    @property
    def Count(self) -> int:
        """ 返回传递给 SecureCRT 的参数数量 """
        return len(self.args)

    def GetArg(self, index: int) -> str:
        """ 返回与每个 /ARG 命令行选项关联的参数数据 """
        return self.args[index]

    def __getitem__(self, index: int) -> str:
        """ 使 Arguments 对象支持索引访问 """
        return self.GetArg(index)
