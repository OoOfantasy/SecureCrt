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
    script_tab = _crt.GetScriptTab()
    log_file = script_tab.Session.LogFileName
    _crt.Dialog.MessageBox(f"Log File: {log_file}", "Log File", [64, 0, 0])
  except Exception:
    errcode = _crt.GetLastError()
    errmessage = _crt.GetLastErrorMessage()
    _crt.Dialog.MessageBox(f"Error Code: {errcode}\nError Message: {errmessage}", "Error Cleared", [16, 0, 0])
    _crt.ClearLastError()
  return

main()
