import socket
import tkinter as tk
import requests
import subprocess
from scapy.all import *



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_hostname():
    return socket.gethostname()

def get_public_ip():
    response = requests.get('http://checkip.dyndns.org')
    return response.text.split(': ')[-1].strip()

def get_dynamic_dns():
    response = requests.get('http://checkip.dyndns.org/dynamicdns.html')
    return response.text.split('Dynamic DNS : ')[-1].split('<')[0]

#scan réseau
def get_machines():
    machines = []
    ans, unans = arping('10.60.56.0/24')
    for s, r in ans:
        machines.append(r.sprintf("%ARP.psrc%"))
    return "\n".join(machines)

root = tk.Tk()
label_titre = tk.Label(root, text=f'Bienvenue sur le tableau de bord de votre SemaOS')
label_titre.pack(side="top")

# Fonction qui met à jour le label avec la latence de ping
def check_internet_connection():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        
        if result.returncode == 0:
            latency = result.stdout.decode('latin1').split('\n')[-2].split(' = ')[-1]
            label_latency['text'] = f'Connecté à Internet\nLatency: {latency}'
        else:
            label_latency['text'] = 'Non connecté à Internet'
    except Exception as e:
        label_latency['text'] = 'Error: ' + str(e)

# texte = tk.Text(root, height=10)
# texte.pack()
# texte.configure(font=("Times New Roman", 20, "italic"))

#scan label
label_machines = tk.Label(root, text=f'Machines en ligne: {get_machines()}')
label_machines.pack(side="bottom")

label_ip = tk.Label(root, text=f'IP: {get_ip()}')
label_ip.pack()

label_hostname = tk.Label(root, text=f'Hostname: {get_hostname()}')
label_hostname.pack()

label_latency = tk.Label(root, text='')
label_latency.pack()
check_internet_connection()

label_ip = tk.Label(root, text=f'Public IP: {get_public_ip()}')
label_ip.pack()
label_dns = tk.Label(root, text=f'Dynamic DNS: {get_dynamic_dns()}')
label_dns.pack()

root.geometry("400x300")
root.mainloop()