import socket
import tkinter as tk
import requests
import subprocess
from scapy.all import *
import urllib.request
from tkinter import messagebox
from scapy.all import ARP, Ether, srp

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

def get_recover_info():
        ip = requests.get('https://api.ipify.org').text
        hostname = socket.gethostname()
        frame_ip = tk.Frame(root, bd=2, relief="groove")
        frame_ip.pack(padx=10, pady=10, fill="x")

        label_ip_title = tk.Label(frame_ip, text="Adresse IP publique et nom de domaine", font=("Helvetica", 14, "bold"))
        label_ip_title.pack(pady=5)
        result_label = tk.Label(frame_ip, text=f"{ip}\n{hostname}", font=("Helvetica", 12))
        result_label.pack()

#scan réseau
# appel de la fonction pour afficher la liste des noms de machines

def check_internet_connection():
    frame_ip = tk.Frame(root, bd=2, relief="groove")
    frame_ip.pack(padx=10, pady=10, fill="x")

    label_ip_title = tk.Label(frame_ip, text="Etat de la connexion", font=("Helvetica", 14, "bold"))
    label_ip_title.pack(pady=5)
    
    try:
        # essayer de se connecter à un site web connu
        urllib.request.urlopen("http://www.google.com")
        label = tk.Label(frame_ip, text="Votre machine est connectée à Internet.", font=("Helvetica", 14, "bold"), fg='green')
    except:
        label = tk.Label(frame_ip, text="Votre machine n'est pas connectée à Internet.", font=("Helvetica", 14, "bold"), fg='red')
    label.pack()
    
    
root = tk.Tk()
label_titre = tk.Label(root, text=f'Bienvenue sur le tableau de bord de votre SemaOS', font=("Helvetica", 16))
label_titre.pack(side="top")
root.configure(bg='#E8F0F2') # Changer la couleur de fond de la fenêtre
label_titre.configure(fg='#4D4D4D') # Changer la couleur du texte
# Fonction qui met à jour le label avec la latence de ping


# appel de la fonction pour vérifier la connexion Internet


# texte = tk.Text(root, height=10)
# texte.pack()
# texte.configure(font=("Times New Roman", 20, "italic"))


# ajouter d'autres fonctionnalités à votre tableau de bord ici

# lancement de la boucle principale Tkinter

frame_ip = tk.Frame(root, bd=2, relief="groove")
frame_ip.pack(padx=10, pady=10, fill="x")

label_ip_title = tk.Label(frame_ip, text="Adresse IP", font=("Helvetica", 14, "bold"))
label_ip_title.pack(pady=5)

label_ip = tk.Label(frame_ip, text=f'{get_ip()}', font=("Helvetica", 12))
label_ip.pack(pady=5)


frame_ip = tk.Frame(root, bd=2, relief="groove")
frame_ip.pack(padx=10, pady=10, fill="x")

label_ip_title = tk.Label(frame_ip, text="Nom", font=("Helvetica", 14, "bold"))
label_ip_title.pack(pady=5)

label_hostname = tk.Label(frame_ip, text=f'{get_hostname()}', font=("Helvetica", 12))
label_hostname.pack()




check_internet_connection()



get_recover_info()



url = "http://speedtest.ftp.otenet.gr/files/test100k.db"

# Taille du fichier en octets
size_in_bytes = 102400

# Fonction appelée lorsque le bouton "Lancer le speedtest" est cliqué
def start_speedtest():
  # Mesure du temps de début du téléchargement
  start = time.perf_counter()

  # Téléchargement du fichier
  urllib.request.urlretrieve(url, "file.bin")

  # Mesure du temps de fin du téléchargement
  end = time.perf_counter()

  # Calcul de la durée du téléchargement en secondes
  duration = end - start

  # Calcul de la vitesse de téléchargement en octets par seconde
  speed = size_in_bytes / duration

  # Affichage de la vitesse de téléchargement en Mo/s dans une nouvelle fenêtre
  frame_ip = tk.Frame(root, bd=2, relief="groove")
  frame_ip.pack(padx=10, pady=10, fill="x")

  label_ip_title = tk.Label(frame_ip, text="Vitesse de téléchargement", font=("Helvetica", 14, "bold"))
  label_ip_title.pack(pady=5)
  result_label = tk.Label(frame_ip, text=f"{speed / 1024 / 1024:.2f} Mo/s", font=("Helvetica", 12))
  result_label.pack()

start_speedtest()

#scan label
host = socket.gethostname()

# obtenir la liste des noms de machines dans le réseau local


def scan_network():
    frame_ip = tk.Frame(root, bd=2, relief="groove")
    frame_ip.pack(padx=10, pady=10, fill="x")

    label_ip_title = tk.Label(frame_ip, text="Machines dans le réseau ", font=("Helvetica", 14, "bold"))
    
    
    # Création d'une requête ARP
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
    label_ip_title.pack()
# Lancement du scan à l'ouverture de la fenêtre
scan_network()


# créer une chaîne de caractères avec les noms de machines séparés par des sauts de ligne


# afficher la liste des machines dans un label


root.geometry("700x600")
root.mainloop()

