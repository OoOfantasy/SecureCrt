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
        # 获取窗口对象
        window = _crt.Window
        
        # 保存原始窗口标题
        original_caption = window.Caption
        
        # 显示当前窗口信息
        _crt.Dialog.MessageBox(
            f"窗口信息:\n"
            f"- 活动状态: {'活动' if window.Active else '非活动'}\n"
            f"- 当前标题: {window.Caption}\n"
            f"- 窗口状态: {window.State} ({['隐藏', '可见', '最小化', '最大化'][window.State] if window.State <= 3 else '未知'})",
            "Window 类测试", 
            [0, 0, 0]
        )
        
        # 修改窗口标题
        window.Caption = "Window 类测试中 - " + original_caption
        
        # 激活窗口
        window.Activate()
        
        # 确认修改完成
        _crt.Dialog.MessageBox(
            "窗口已激活，标题已更改",
            "Window 类测试", 
            [0, 0, 0]
        )
        
        # 测试窗口状态切换
        _crt.Dialog.MessageBox("即将最小化窗口", "Window 类测试", [0, 0, 0])
        window.Show(2)  # 最小化
        _crt.Sleep(2000)  # 等待2秒
        
        _crt.Dialog.MessageBox("即将恢复窗口", "Window 类测试", [0, 0, 0])
        window.Show(1)  # 恢复正常显示
        
        # 恢复原始窗口标题
        window.Caption = original_caption
        
        # 测试完成
        _crt.Dialog.MessageBox(
            "Window 类测试完成，窗口标题已恢复",
            "测试完成", 
            [0, 0, 0]
        )
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
