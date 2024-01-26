import subprocess

pid = None #used to track the spinned up process 

'''
holds the start logic for windows. Each OS will be different. 
'''
def start_cmd_windows(batch_file_name):
    '''
    subprocess.Popen(['command1','command2'], new process arguments)
    DOCS: https://docs.python.org/3/library/subprocess.html
    '''

    global pid
    
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    pro = subprocess.Popen(['cmd', '/c', 'cd','windows','&',batch_file_name], startupinfo=si)
    pid = pro.pid

    print("Processes ID: "+str(pid))
    
'''
kills the process we create eariler
'''
def shutdown_cmd_windows():
    command = ['TASKKILL', '/F', '/T', '/PID', str(pid)]
    subprocess.Popen(command)
    print("killed")