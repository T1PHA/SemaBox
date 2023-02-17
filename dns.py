import requests
import tkinter as tk
from tkinter import messagebox

def get_public_ip():
    # utiliser une API pour obtenir l'adresse IP publique
    try:
        response = requests.get("https://api.ipify.org")
        return response.text
    except:
        return "Impossible de récupérer l'adresse IP publique"
  

def update_dns(ip, domain, token):
    # utiliser une API de service de DNS dynamique (comme DynDNS) pour mettre à jour l'enregistrement DNS du nom de domaine avec l'adresse IP donnée
    try:
        api_url = "https://api.dynu.com/nic/update?hostname={}&myip={}&username=mon_nom_d_utilisateur&password=mon_mot_de_passe".format(domain, ip)
        headers = {"Authorization": "Bearer " + token}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return "Mise à jour réussie"
        else:
            return "Erreur lors de la mise à jour : {}".format(response.text)
    except:
        return "Erreur lors de la mise à jour"

def update_button_clicked():
    ip = get_public_ip()
    domain = domain_entry.get()
    token = token_entry.get()
    result = update_dns(ip, domain, token)
    messagebox.showinfo("Résultat", result)

# créer une fenêtre graphique
window = tk.Tk()
window.title("Mise à jour DNS dynamique")

# ajouter des champs de saisie pour le nom de domaine et le jeton d'authentification
tk.Label(window, text="Nom de domaine :").grid(row=0, column=0)
domain_entry = tk.Entry(window)
domain_entry.grid(row=0, column=1)

tk.Label(window, text="Jeton d'authentification :").grid(row=1, column=0)
token_entry = tk.Entry(window)
token_entry.grid(row=1, column=1)

# ajouter un bouton de mise à jour
update_button = tk.Button(window, text="Mettre à jour", command=update_button_clicked)
update_button.grid(row=2, column=1)

# afficher la fenêtre
window.mainloop()