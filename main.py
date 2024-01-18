import os

'''
holds the start logic for windows. Each OS will be different. 
'''
def start_cmd_windows():
    '''
    starts up console. /k makes the program stay online. /c would close it.
    TODO: We need to make the console prompt turn on with a python ide and then run poetry commands.
    TODO: Make the cmd start as a subprocess under the OS so we can track it. 

    os.system("start cmd /k {commands})
    '''

    os.system("start cmd /k cd..")

'''
Will hold the runtime of our program
'''
def run():
    pass
        

if __name__ == "__main__":
    start_cmd_windows()

    run()