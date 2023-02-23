import socket
import tkinter as tk
import requests
import subprocess
from scapy.all import *
import urllib.request
import nmap

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
# appel de la fonction pour afficher la liste des noms de machines


root = tk.Tk()
label_titre = tk.Label(root, text=f'Bienvenue sur le tableau de bord de votre SemaOS')
label_titre.pack(side="top")

# Fonction qui met à jour le label avec la latence de ping
def check_internet_connection():
    try:
        # essayer de se connecter à un site web connu
        urllib.request.urlopen("http://www.google.com")
        label = tk.Label(root, text="Votre machine est connectée à Internet.")
    except:
        label = tk.Label(root, text="Votre machine n'est pas connectée à Internet.")
    label.pack()

# appel de la fonction pour vérifier la connexion Internet


# texte = tk.Text(root, height=10)
# texte.pack()
# texte.configure(font=("Times New Roman", 20, "italic"))


# ajouter d'autres fonctionnalités à votre tableau de bord ici

# lancement de la boucle principale Tkinter

label_ip = tk.Label(root, text=f'IP: {get_ip()}')
label_ip.pack()

label_hostname = tk.Label(root, text=f'Hostname: {get_hostname()}')
label_hostname.pack()
check_internet_connection()
label_latency = tk.Label(root, text='')
label_latency.pack()

label_ip = tk.Label(root, text=f'Public IP: {get_public_ip()}')
label_ip.pack()
label_dns = tk.Label(root, text=f'Dynamic DNS: {get_dynamic_dns()}')
label_dns.pack()

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

  result_label = tk.Label(root, text=f"Vitesse de téléchargement : {speed / 1024 / 1024:.2f} Mo/s")
  result_label.pack()

start_speedtest()

#scan label
host = socket.gethostname()

# obtenir la liste des noms de machines dans le réseau local
ip_list = []
for ip in socket.gethostbyname_ex(host)[2]:
    if not ip.startswith("127."):
        ip_list.append(ip)

# créer une chaîne de caractères avec les noms de machines séparés par des sauts de ligne
machines_str = ip_list

# afficher la liste des machines dans un label
label = tk.Label(root, text=f'Machines détectées dans le réseau: {machines_str}')
label.pack()

root.geometry("400x300")
root.mainloop()
