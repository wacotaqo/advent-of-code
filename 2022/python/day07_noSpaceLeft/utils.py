import os
import sys

print("Current working directory: %s" % (os.getcwd()))

IDE_VSCODE = "Visual Studio Code"
IDE_PYCHARM = "PyCharm"
IDE_UNNOWN = "No known IDE"

OS_WIN = "Windows"
OS_MAC = "MacOs"
OS_OTHER = "OtherOS"

def detect_os():
    if os.getenv('OS').find("Windows") >= 0:
        return OS_WIN
    return OS_OTHER

def detect_ide():
    if os.getenv('TERM_PROGRAM') == 'vscode':
        return IDE_VSCODE
    if os.getenv('PYCHARM_HOSTED'):
        return IDE_PYCHARM
    return IDE_UNKNOWN

#print("OS  = %s" % detect_os())
#print("IDE = %s" % detect_ide())