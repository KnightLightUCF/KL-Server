import subprocess

pid = None #used to track the spinned up process 

IMPORTANT_MESSAGE = '''
|============[KL-Server - v0.1]============|


Requried to install skybrush and run poetry. Leave skybrush-server in the root directory for this to work.

File structure should look like this:
Root/
     skybrush-server/
     windows/
     .gitignore
     main.py

|===========================================|
'''

'''
holds the start logic for windows. Each OS will be different. 
'''
def start_cmd_windows():
    '''
    TODO: We need to make the console prompt turn on with a python ide and then run poetry commands.

    subprocess.Popen(['command1','command2'], new process arguments)

    DOCS: https://docs.python.org/3/library/subprocess.html
    '''

    global pid
    
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    pro = subprocess.Popen(['cmd', '/c', 'cd','windows','&','startup.bat'], startupinfo=si)
    pid = pro.pid

    print("Processes ID: "+str(pid))
    

def shutdown_cmd_windows():
    command = ['TASKKILL', '/F', '/T', '/PID', str(pid)]
    subprocess.Popen(command)
    print("killed")

'''
Will hold the runtime of our program

For now it_count will be to test how long until we kill the subprocess
'''
def run():
    input("Press any key to exit... \n>>> ")
    shutdown_cmd_windows()
    input("Press any key to exit... \n>>> ")
        

if __name__ == "__main__":
    print(IMPORTANT_MESSAGE)

    start_cmd_windows()

    run()
    