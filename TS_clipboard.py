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
        # 保存原始剪贴板格式和内容
        original_format = _crt.Clipboard.Format
        original_text = _crt.Clipboard.Text
        
        # 显示当前剪贴板格式
        _crt.Dialog.MessageBox(f"当前剪贴板格式: {_crt.Clipboard.Format}", "剪贴板格式", [0, 0, 0])
        
        # 设置新的剪贴板内容
        test_text = "这是剪贴板测试文本 - Test clipboard text"
        _crt.Clipboard.Text = test_text
        
        # 验证剪贴板内容
        current_text = _crt.Clipboard.Text
        _crt.Dialog.MessageBox(f"剪贴板内容: {current_text}", "读取剪贴板", [0, 0, 0])
        
        # 测试不同的剪贴板格式
        _crt.Clipboard.Format = _crt.Clipboard.VDS_TEXT
        _crt.Dialog.MessageBox(f"已将格式更改为 VDS_TEXT: {_crt.Clipboard.Format}", "格式测试", [0, 0, 0])
        
        _crt.Clipboard.Format = _crt.Clipboard.CF_UNICODETEXT
        _crt.Dialog.MessageBox(f"已将格式更改为 CF_UNICODETEXT: {_crt.Clipboard.Format}", "格式测试", [0, 0, 0])
        
        _crt.Clipboard.Format = _crt.Clipboard.CF_TEXT
        _crt.Dialog.MessageBox(f"已将格式更改为 CF_TEXT: {_crt.Clipboard.Format}", "Windows格式", [0, 0, 0])
        
        _crt.Clipboard.Format = _crt.Clipboard.CF_OEMTEXT
        _crt.Dialog.MessageBox(f"已将格式更改为 CF_OEMTEXT: {_crt.Clipboard.Format}", "Windows格式", [0, 0, 0])
        
        # 恢复原始剪贴板格式和内容
        _crt.Clipboard.Format = original_format
        _crt.Clipboard.Text = original_text
        _crt.Dialog.MessageBox("剪贴板测试完成，原始内容已恢复", "测试完成", [64, 0, 0])
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
