import subprocess
import os
import signal

def start_cmd_mac(file):
    
    
    global process
    global pid
    
    # cmds = ['pwd', 'cd skybrush-server', 'cd .venv.', 'cd bin', 'source activate', 'python3 skybrushd']
    
    print("Server is running at localhost:5000")
    process = subprocess.Popen(["sh", "./mac/" + file])
    # process = subprocess.Popen(["pwd", "&&","cd","skybrush-server","&&","cd",".venv","&&","cd","bin","&&","source","activate","&&","python3","skybrushd","&&","pwd"])
    # process = subprocess.run(["ls", ";", "cd", "skybrush-server"])
    # process = subprocess.Popen(["cd skybrush-server;ls"])
    
    pid = process.pid
    print("pid: " + str(pid))
    end_Process = input("Press any key to end the server\n")
    # process.send_signal(signal.SIGINT)
    # process.wait()
    print("Server has closed")
    
def stop_cmd_mac():
    # process.terminate()
    # process.kill()
    os.kill(int(pid+2), signal.SIGKILL)
    print("delete pid: " + str(pid+2))
    # process.communicate()