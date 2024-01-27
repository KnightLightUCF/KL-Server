import subprocess

def start_cmd_mac(file):
    
    print("Server is running at localhost:5000")
    subprocess.run(["sh", "./mac/"+file], capture_output=True)
    print("Server has closed")
    