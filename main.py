import subprocess

DEFAULT_IT_COUNT = 10000000 #testing can edit 

pid = None #used to track the spinned up process 

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
def run(it_count):
    i=0
    #test code to show that both processes run at the sametime
    while True: 
        if i>=it_count:
            shutdown_cmd_windows()
            break

        i+=1

    input("Press any key to exit... \n>>> ")
        

if __name__ == "__main__":
    start_cmd_windows()

    run(it_count=DEFAULT_IT_COUNT)
    