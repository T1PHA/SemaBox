import tkinter as tk
from scapy.all import *

def get_machines():
    machines = []
    ans, unans = arping('10.60.56.0/24', verbose=0)
    for s, r in ans:
        try:
            name = socket.gethostbyaddr(r.psrc)[0]
            machines.append(f'{r.sprintf(r"%Ether.src%")} - {r.sprintf(r"%ARP.psrc%")} - {name}')
        except:
            machines.append(f'{r.sprintf(r"%Ether.src%")} - {r.sprintf(r"%ARP.psrc%")}')
    return '\n'.join(machines)

root = tk.Tk()
label = tk.Label(root, text=get_machines())
label.pack()
root.mainloop()