import requests
import tkinter as tk

def get_public_ip():
    try:
        # Utilisez l'API de l'IP de l'i.p.chaos pour obtenir l'adresse IP publique
        response = requests.get('https://api.ipify.org')
        # Récupérez l'adresse IP de la réponse
        public_ip = response.text
        # Mettez à jour la zone de texte avec l'adresse IP publique
        ip_text.set(public_ip)
    except Exception as e:
        # Affichez un message d'erreur en cas d'échec
        ip_text.set("Erreur lors de l'obtention de l'adresse IP publique")

def get_dns_info():
    try:
        # Utilisez l'API de DynDNS pour obtenir les informations de nom de domaine
        response = requests.get('http://dyndns.org/info')
        # Récupérez le nom de domaine de la réponse
        domain = response['domain']
        # Mettez à jour la zone de texte avec le nom de domaine
        domain_text.set(domain)
    except Exception as e:
        # Affichez un message d'erreur en cas d'échec
        domain_text.set("Erreur lors de l'obtention des informations de nom de domaine")

# Créez une fenêtre graphique
window = tk.Tk()
window.title("Informations de DynDNS")

# Créez des zones de texte pour afficher l'adresse IP publique et le nom de domaine
ip_text = tk.StringVar()
domain_text = tk.StringVar()

# Créez un label pour afficher l'adresse IP publique
ip_label = tk.Label(window, textvariable=ip_text)
ip_label.pack()

# Créez un bouton pour obtenir l'adresse IP publique
get_ip_button = tk.Button(window, text="Obtenir l'adresse IP publique", command=get_public_ip)
get_ip_button.pack()

# Créez un label pour afficher le nom de domaine
domain_label = tk.Label(window, textvariable=domain_text)
domain_label.pack()

# Créez un bouton pour obtenir les informations de nom de domaine
get_info_button = tk.Button(window, text="Obtenir les informations de nom de domaine", command=get_dns_info)
get_info_button.pack()

# Démarrez la boucle d'événements
window.mainloop()