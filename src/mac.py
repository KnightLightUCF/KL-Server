import subprocess
import os
import signal

def start_cmd_mac(file):
    
    global process
    global pid
    
    print("Server is running at localhost:5000")
    process = subprocess.Popen(["sh", "./mac/" + file])
    
    pid = process.pid
    print("pid: " + str(pid))
    end_Process = input("Press any key to end the server\n")
    
def stop_cmd_mac():
    # We add 2 because the pid is always 2 higher than what is read.
    os.kill(int(pid+2), signal.SIGKILL)
    print("Server has closed")