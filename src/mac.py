import subprocess

def start_cmd_mac(file):
    
    
    global process
    
    print("Server is running at localhost:5000")
    process = subprocess.Popen(["sh", "./mac/"+file])
    print("Server has closed")
    
def stop_cmd_mac():
    process.terminate()