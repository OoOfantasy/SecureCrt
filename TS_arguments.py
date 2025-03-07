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
        _crt.Dialog.MessageBox("Arguments: " + str(_crt.Arguments.Count))
        if _crt.Arguments.Count != 2:
            _crt.Dialog.MessageBox("This script requires hostname and port arguments")
        _crt.Dialog.MessageBox(f"Hostname: {_crt.Arguments.GetArg(0)}\nPort: {_crt.Arguments.GetArg(1)}", "Arguments")
        _crt.Dialog.MessageBox(f"Hostname: {_crt.Arguments[0]}\nPort: {_crt.Arguments[1]}", "Arguments")
        index_error = _crt.Arguments[2]
    except Exception as e:
        errcode = _crt.GetLastError()
        errmessage = _crt.GetLastErrorMessage()
        _crt.ClearLastError()
        _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage if errcode!=0 else e}", "Error Cleared", [16, 0, 0])
    return

main()
