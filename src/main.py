from src.download import download_check
from src.windows import *

'''
Will hold the runtime of our program
'''
def run():
    input("Press any key to exit... \n>>> ")
    
    shutdown_cmd_windows()
    
    input("Press any key to exit... \n>>> ")
        
def start():
    is_downloaded = download_check()
    if not is_downloaded:
        start_cmd_windows(batch_file_name="install.bat")
    else:
        start_cmd_windows(batch_file_name="startup.bat")
    
    run()