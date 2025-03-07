# $language = "Python3"
# $interface = "1.0"

import os
import sys

def get_script_path():
  return os.path.split(os.path.realpath(__file__))[0]
sys.path.append(get_script_path())

from SecureCrt.CRT import CRT

def main():
    _crt = CRT(crt) #type: ignore
    try:
        # 获取当前会话对象
        session = _crt.GetScriptTab().Session
        result = []
        
        # 测试会话属性
        result.append(f"当前会话状态:")
        result.append(f"Connected: {session.Connected}")
        result.append(f"Label: {session.Label}")
        result.append(f"Locked: {session.Locked}")
        result.append(f"Logging: {session.Logging}")
        result.append(f"Path: {session.Path}")
        
        # 如果已连接，测试连接相关属性
        if session.Connected:
            try:
                result.append(f"LocalAddress: {session.LocalAddress}")
                result.append(f"RemoteAddress: {session.RemoteAddress}")
                result.append(f"RemotePort: {session.RemotePort}")
            except Exception as e:
                result.append(f"获取连接地址信息错误: {str(e)}")
        
        # 测试状态栏文本设置
        session.SetStatusText("测试状态栏文本")
        result.append("已设置状态栏文本")
        
        # 测试日志文件名
        try:
            current_log = session.LogFileName
            result.append(f"当前日志文件名: {current_log}")
        except Exception as e:
            result.append(f"获取日志文件名错误: {str(e)}")
        
        # 显示测试结果
        _crt.Dialog.MessageBox("\n".join(result), "Session测试结果", [0, 0, 0])
        
        # 提供连接测试选项
        connect_test = _crt.Dialog.MessageBox("是否要测试连接功能?\n(会在新标签页中打开连接)", 
                                             "连接测试", [32 + 4, 0, 0])
        if connect_test == 6:  # 如果用户选择"是"
            # 在新标签页中连接
            host = _crt.Dialog.Prompt("请输入要连接的主机名或IP:", "ConnectInTab测试", "localhost", False)
            if host:
                try:
                    new_tab = session.ConnectInTab(f"/telnet {host}", True, True)
                    _crt.Dialog.MessageBox(f"已尝试连接到 {host}\n新标签页索引: {new_tab.Index}", "连接测试", [0, 0, 0])
                except Exception as e:
                    _crt.Dialog.MessageBox(f"连接错误: {str(e)}", "连接错误", [16, 0, 0])
        
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
