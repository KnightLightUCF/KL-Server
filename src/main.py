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
    download_check()

    start_cmd_windows()
    
    run()