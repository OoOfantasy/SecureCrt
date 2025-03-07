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
        # 获取CommandWindow对象
        cmd_window = _crt.CommandWindow
        
        # 测试Visible属性
        original_visible = cmd_window.Visible
        _crt.Dialog.MessageBox(f"命令窗口当前可见性: {original_visible}", "测试Visible属性", [0, 0, 0])
        
        # 确保命令窗口可见以便于测试
        cmd_window.Visible = True
        
        # 测试Text属性
        cmd_window.Text = "echo '测试CommandWindow的Text属性'"
        _crt.Dialog.MessageBox(f"已设置文本: {cmd_window.Text}", "测试Text属性", [0, 0, 0])
        
        # 测试Send方法
        cmd_window.Send()
        _crt.Dialog.MessageBox("已使用Send方法发送命令", "测试Send方法", [0, 0, 0])
        
        # 测试SendCharactersImmediately属性
        original_send_immediately = cmd_window.SendCharactersImmediately
        _crt.Dialog.MessageBox(f"SendCharactersImmediately当前值: {original_send_immediately}", 
                              "测试SendCharactersImmediately属性", [0, 0, 0])
        
        # 切换SendCharactersImmediately属性
        cmd_window.SendCharactersImmediately = not original_send_immediately
        _crt.Dialog.MessageBox(f"已将SendCharactersImmediately切换为: {cmd_window.SendCharactersImmediately}", 
                              "测试SendCharactersImmediately属性", [0, 0, 0])
        
        # 测试SendToAllSessions属性
        original_send_all = cmd_window.SendToAllSessions
        _crt.Dialog.MessageBox(f"SendToAllSessions当前值: {original_send_all}", 
                              "测试SendToAllSessions属性", [0, 0, 0])
        
        # 切换SendToAllSessions属性
        cmd_window.SendToAllSessions = not original_send_all
        _crt.Dialog.MessageBox(f"已将SendToAllSessions切换为: {cmd_window.SendToAllSessions}", 
                              "测试SendToAllSessions属性", [0, 0, 0])
        
        # 恢复原始设置
        cmd_window.SendCharactersImmediately = original_send_immediately
        cmd_window.SendToAllSessions = original_send_all
        cmd_window.Visible = original_visible
        
        _crt.Dialog.MessageBox("CommandWindow类测试完成！", "测试结束", [0, 0, 0])
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
