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
        # 创建一个菜单，让用户选择测试哪些功能
        menu = """
        ======== Screen类测试工具 ========
        1. 测试屏幕属性（Columns, Rows, CurrentRow, CurrentColumn）
        2. 测试Get和Get2方法
        3. 测试Send方法
        4. 测试WaitForString方法
        5. 测试ReadString方法
        6. 测试清屏操作
        7. 测试所有属性
        0. 退出
        请选择要测试的功能(0-7): """
        
        while True:
            choice = _crt.Dialog.Prompt(menu, "Screen测试", "1")
            
            if choice == "0":
                break
                
            elif choice == "1":
                # 测试屏幕属性
                message = f"屏幕尺寸: {_crt.Screen.Columns}列 x {_crt.Screen.Rows}行\n"
                message += f"当前光标位置: 行={_crt.Screen.CurrentRow}, 列={_crt.Screen.CurrentColumn}"
                _crt.Dialog.MessageBox(message, "屏幕属性测试")
                
            elif choice == "2":
                # 测试Get和Get2方法
                row1 = int(_crt.Dialog.Prompt("起始行:", "Get测试", "1"))
                col1 = int(_crt.Dialog.Prompt("起始列:", "Get测试", "1"))
                row2 = int(_crt.Dialog.Prompt("结束行:", "Get测试", str(_crt.Screen.CurrentRow)))
                col2 = int(_crt.Dialog.Prompt("结束列:", "Get测试", str(_crt.Screen.CurrentColumn)))
                
                text1 = _crt.Screen.Get(row1, col1, row2, col2)
                text2 = _crt.Screen.Get2(row1, col1, row2, col2)
                
                message = "Get方法结果:\n" + text1 + "\n\nGet2方法结果:\n" + text2
                _crt.Dialog.MessageBox(message, "Get和Get2测试")
                
            elif choice == "3":
                # 测试Send方法
                text = _crt.Dialog.Prompt("请输入要发送的文本:", "Send测试", "echo 测试Send方法")
                _crt.Screen.Send(text + "\n")
                _crt.Dialog.MessageBox("已发送文本: " + text, "Send测试")
                
            elif choice == "4":
                # 测试WaitForString方法
                text = _crt.Dialog.Prompt("请输入要等待的文本:", "WaitForString测试", "test")
                timeout = int(_crt.Dialog.Prompt("等待超时(秒):", "WaitForString测试", "5"))
                
                _crt.Dialog.MessageBox(f"将等待文本\"{text}\"出现，超时时间{timeout}秒", "WaitForString测试")
                result = _crt.Screen.WaitForString(text, timeout)
                if result:
                    _crt.Dialog.MessageBox(f"成功找到文本: {text}", "WaitForString测试")
                else:
                    _crt.Dialog.MessageBox(f"未找到文本: {text}，已超时", "WaitForString测试")
                
            elif choice == "5":
                # 测试ReadString方法
                _crt.Dialog.MessageBox("请在终端中输入任意内容，系统将读取您的输入", "ReadString测试")
                text = _crt.Screen.ReadString(["exit", "\n"], 10)
                _crt.Dialog.MessageBox(f"读取到的内容:\n{text}", "ReadString测试")
                
            elif choice == "6":
                # 测试Clear方法
                if _crt.Dialog.MessageBox("是否要清除屏幕?", "Clear测试", [1, 0, 0]) == 1:
                    _crt.Screen.Clear()
                    _crt.Dialog.MessageBox("屏幕已清除", "Clear测试")
                    
            elif choice == "7":
                # 测试所有属性
                props = [
                    f"Columns: {_crt.Screen.Columns}",
                    f"Rows: {_crt.Screen.Rows}",
                    f"CurrentRow: {_crt.Screen.CurrentRow}",
                    f"CurrentColumn: {_crt.Screen.CurrentColumn}",
                    f"IgnoreEscape: {_crt.Screen.IgnoreEscape}",
                    f"MatchIndex: {_crt.Screen.MatchIndex}",
                    f"Selection: {_crt.Screen.Selection}",
                    f"Synchronous: {_crt.Screen.Synchronous}"
                ]
                _crt.Dialog.MessageBox("\n".join(props), "Screen属性测试")
                
            else:
                _crt.Dialog.MessageBox("无效选择，请重试", "错误", [16, 0, 0])
        
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
