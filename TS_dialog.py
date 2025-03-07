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
        # 创建结果日志
        results = ["Dialog 类测试结果:"]
        
        # 测试 MessageBox 不同图标
        results.append("\n1. MessageBox 图标测试:")
        icons = [
            ("ICON_STOP", _crt.Dialog.ICON_STOP),
            ("ICON_QUESTION", _crt.Dialog.ICON_QUESTION),
            ("ICON_WARN", _crt.Dialog.ICON_WARN),
            ("ICON_INFO", _crt.Dialog.ICON_INFO)
        ]
        
        for name, icon in icons:
            result = _crt.Dialog.MessageBox(f"这是 {name} 图标测试", f"{name} 测试", [icon, _crt.Dialog.BUTTON_OK])
            results.append(f"  - {name} 测试结果: {result} (应为 {_crt.Dialog.IDOK})")
        
        # 测试 MessageBox 不同按钮组合
        results.append("\n2. MessageBox 按钮测试:")
        button_result = _crt.Dialog.MessageBox("请点击'是'按钮", "是/否测试", 
                                               [_crt.Dialog.ICON_QUESTION, _crt.Dialog.BUTTON_YESNO])
        results.append(f"  - BUTTON_YESNO 测试: {'成功' if button_result == _crt.Dialog.IDYES else '失败'}")
        
        # 测试 FileOpenDialog
        results.append("\n3. FileOpenDialog 测试:")
        open_file = _crt.Dialog.FileOpenDialog("打开文件测试", "选择", "", "Python文件 (*.py)|*.py||")
        results.append(f"  - 选择的文件: {open_file if open_file else '用户取消'}")
        
        # 测试 FileSaveDialog
        results.append("\n4. FileSaveDialog 测试:")
        save_file = _crt.Dialog.FileSaveDialog("保存文件测试", "保存", "test_results.txt", "文本文件 (*.txt)|*.txt||")
        results.append(f"  - 保存路径: {save_file if save_file else '用户取消'}")
        
        # 测试 Prompt
        results.append("\n5. Prompt 测试:")
        user_input = _crt.Dialog.Prompt("请输入任意文本:", "普通输入测试", "默认文本")
        results.append(f"  - 普通输入: {user_input if user_input else '用户取消'}")
        
        # 测试 Prompt (密码)
        password = _crt.Dialog.Prompt("请输入密码:", "密码输入测试", "", True)
        results.append(f"  - 密码输入: {'已输入' if password else '用户取消'} {'(长度：'+str(len(password))+')' if password else ''}")
        
        # 显示最终测试结果
        _crt.Dialog.MessageBox("\n".join(results), "Dialog测试完成", _crt.Dialog.ICON_INFO)
        
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
