import socket
import threading
import tkinter as tk
from scapy.all import ARP, Ether, srp

class PortScanner:
    root = tk.Tk()
    def __init__(self, master):
        self.master = master
        self.master.title("Port Scanner")

        # Ajout d'un champ d'entrée pour l'adresse IP
        self.ip_label = tk.Label(self.master, text="IP Address:")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(self.master)
        self.ip_entry.pack()

        # Ajout d'un champ d'entrée pour la plage de ports à scanner
        self.port_range_label = tk.Label(self.master, text="Port Range:")
        self.port_range_label.pack()
        self.port_range_entry = tk.Entry(self.master)
        self.port_range_entry.insert(tk.END, "1-1000")
        self.port_range_entry.pack()

        # Ajout d'un bouton pour lancer le scan
        self.scan_button = tk.Button(self.master, text="Scan", command=self.scan_ports)
        self.scan_button.pack()

        # Ajout d'un champ de texte pour afficher les résultats
        self.result_text = tk.Text(self.master)
        self.result_text.pack()

    
    # Récupération de l'adresse IP entrée
    def scan_ports(self):
        # Récupération de l'adresse IP entrée
        ip = self.ip_entry.get()

        # Récupération de la plage de ports à scanner
        port_range = self.port_range_entry.get().split('-')
        start_port = int(port_range[0])
        end_port = int(port_range[1])

        # Scan des ports pour chaque machine du réseau
        for port in range(start_port, end_port+1):
            # Utilisation de threads pour accélérer le scan
            thread = threading.Thread(target=self.scan_port, args=(ip, port))
            thread.start()
            
    host = socket.gethostname()
    
    # obtenir la liste des noms de machines dans le réseau local
    arp = ARP(pdst="192.168.29.0/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result_text = tk.Text(root)
    # Envoi de la requête ARP et récupération des réponses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Affichage des adresses MAC et IP des machines qui ont répondu
    for sent, received in result:
        result_text.insert(tk.END, f"MAC Address: {received.hwsrc} - IP Address: {received.psrc}\n")
    result_text.pack()

    root.geometry("500x200")
    root.mainloop()

    def scan_port(self, ip, port):
        # Tentative de connexion à un port sur une machine
        try:
            # Création d'un objet socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()

            # Si la connexion est réussie, le port est ouvert
            if result == 0:
                self.result_text.insert(tk.END, f"Port {port} is open\n")

        except:
            pass
            
root = tk.Tk()
scanner = PortScanner(root)
root.geometry("300x300")
root.mainloop()

