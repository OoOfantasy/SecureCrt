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
        # 测试FileTransfer属性
        # 获取下载文件夹路径
        download_folder = _crt.FileTransfer.DownloadFolder
        _crt.Dialog.MessageBox(f"下载文件夹路径: {download_folder}", "FileTransfer测试", [64, 0, 0])
        
        # 测试ZmodemUploadAscii属性
        original_ascii_mode = _crt.FileTransfer.ZmodemUploadAscii
        _crt.Dialog.MessageBox(f"当前Zmodem上传ASCII模式: {original_ascii_mode}", 
                              "ZmodemUploadAscii测试", [64, 0, 0])
        
        # 切换ZmodemUploadAscii设置
        _crt.FileTransfer.ZmodemUploadAscii = not original_ascii_mode
        _crt.Dialog.MessageBox(f"已切换Zmodem上传ASCII模式为: {_crt.FileTransfer.ZmodemUploadAscii}", 
                              "ZmodemUploadAscii测试", [64, 0, 0])
        
        # 测试上传列表管理
        # 创建临时测试文件
        temp_file_path1 = os.path.join(download_folder, "test_upload1.txt")
        temp_file_path2 = os.path.join(download_folder, "test_upload2.txt")
        
        with open(temp_file_path1, "w") as f:
            f.write("这是测试上传文件1")
        with open(temp_file_path2, "w") as f:
            f.write("这是测试上传文件2")
        
        # 清除任何现有上传列表
        _crt.FileTransfer.ClearUploadList()
        _crt.Dialog.MessageBox("已清除上传列表", "ClearUploadList测试", [64, 0, 0])
        
        # 添加文件到上传列表
        _crt.FileTransfer.AddToUploadList(temp_file_path1)
        _crt.FileTransfer.AddToUploadList(temp_file_path2)
        _crt.Dialog.MessageBox(f"已添加文件到上传列表:\n{temp_file_path1}\n{temp_file_path2}", 
                              "AddToUploadList测试", [64, 0, 0])
        
        # 显示文件传输方法使用信息
        info_text = """
文件传输方法使用信息:

1. Xmodem传输:
   - 发送: _crt.FileTransfer.SendXmodem("完整文件路径")
   - 接收: _crt.FileTransfer.ReceiveXmodem("仅文件名")

2. Ymodem传输:
   - 发送: 先用AddToUploadList添加文件，然后调用SendYmodem()
   - 接收: _crt.FileTransfer.ReceiveYmodem()

3. Kermit传输:
   - 发送: 先用AddToUploadList添加文件，然后调用SendKermit()
   - 接收: _crt.FileTransfer.ReceiveKermit()

注意: 实际传输需要连接到支持相应协议的远程系统。
"""
        _crt.Dialog.MessageBox(info_text, "文件传输方法说明", [64, 0, 0])
        
        # 清理临时文件
        os.remove(temp_file_path1)
        os.remove(temp_file_path2)
        
        # 恢复原始设置
        _crt.FileTransfer.ZmodemUploadAscii = original_ascii_mode
        _crt.FileTransfer.ClearUploadList()
        
        _crt.Dialog.MessageBox("FileTransfer类测试完成！", "测试结束", [64, 0, 0])
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
