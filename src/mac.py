import subprocess

def start_cmd_mac(file):
    global pid
    
    # si = subprocess.STARTUPINFO()
    # si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    # pro = subprocess.Popen(['cmd', '/c', 'cd','mac','&', 'sh', file], startupinfo=si)
    pro = subprocess.Popen(['cd','mac','&', 'sh', file])
    pid = pro.pid
    