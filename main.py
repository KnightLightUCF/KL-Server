import subprocess

'''
holds the start logic for windows. Each OS will be different. 
'''
def start_cmd_windows():
    '''
    starts up console. /k makes the program stay online. /c would close it.
    TODO: URGENT figure out a way to kill program after it is spinned up.
    TODO: We need to make the console prompt turn on with a python ide and then run poetry commands.

    subprocess.Popen(['command1','command2'], new process arguments)

    DOCS: https://docs.python.org/3/library/subprocess.html
    '''

    pro = subprocess.Popen(['start', 'cmd', '/k', 'windows\\startup.bat'], shell=True)
    

def shutdown_cmd_windows():
    pass

'''
Will hold the runtime of our program
'''
def run():
    input("Press any key to exit... \n>>> ")
        

if __name__ == "__main__":
    start_cmd_windows()

    run()
    