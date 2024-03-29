from src.download import download_check
from src.windows import *
from src.mac import *
import sys
from sys import platform

'''
Will hold the runtime of our program
'''
def run():
    input("Press any key to exit... \n>>> ")
    if sys.platform == 'win32':
        shutdown_cmd_windows()
    if sys.platform == 'darwin':
        stop_cmd_mac()
    
    # input("Press any key to exit... \n>>> ")
        
def start():
    is_downloaded = download_check()
    if not is_downloaded:
        if sys.platform == 'win32':
            start_cmd_windows(batch_file_name="install.bat") 
        if sys.platform == 'darwin':
            start_cmd_mac(file = "install.sh")
            start_cmd_mac(file = "startup.sh")
    else:
        if sys.platform == 'win32':
            start_cmd_windows(batch_file_name="startup.bat")
        if  sys.platform == 'darwin':
            start_cmd_mac(file = "startup.sh")
    
    run()
