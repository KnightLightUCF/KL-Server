# Import Module
from tkinter import *
 
 
 
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
    
def terminate_server():
    if sys.platform == 'win32':
        shutdown_cmd_windows() 
    if sys.platform == 'darwin':
        stop_cmd_mac()
 




# create root window
root = Tk()
 
# root window title and dimension
root.title("Skybrush Server Application for KnightLight")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = Label(root, text = "Server Controls")
lbl.grid()
 
# adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)
 
 
# function to display user text when 
# button is clicked
# button widget with red color text inside
start_server = Button(root, text = "Start the Server" , fg = "green", command=start)
stop_server = Button(root, text = "Stop the server" , fg = "red", command=terminate_server)

# Set Button Grid
start_server.grid(column=1, row=1)
stop_server.grid(column=2, row= 1)
 
# Execute Tkinter
root.mainloop()