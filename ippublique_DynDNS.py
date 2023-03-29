import tkinter as tk    # Importation de la bibliothèque Tkinter pour créer l'interface graphique
import socket           # Importation de la bibliothèque Socket pour récupérer le nom de la machine
import requests         # Importation de la bibliothèque Requests pour récupérer l'adresse IP publique
from tkinter import messagebox  # Importation de la classe messagebox de la bibliothèque Tkinter pour afficher une boîte de dialogue

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Récupération d'informations réseau")  # Définition du titre de la fenêtre
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.recovery_button = tk.Button(self, text="Lancer la récupération", command=self.recover_info)  # Création d'un bouton pour lancer la récupération d'informations
        self.recovery_button.pack(side="top")    # Ajout du bouton dans la fenêtre

    def recover_info(self):
        ip = requests.get('https://api.ipify.org').text    # Récupération de l'adresse IP publique en utilisant l'API ipify
        hostname = socket.gethostname()    # Récupération du nom de la machine
        message = f"Adresse IP publique : {ip}\nNom DNS de la machine : {hostname}"    # Création du message contenant l'adresse IP et le nom de la machine
        messagebox.showinfo("Résultat de la récupération", message)    # Affichage d'une boîte de dialogue avec le message récupéré

root = tk.Tk()  # Création de la fenêtre principale
app = Application(master=root)  # Création d'une instance de l'application
app.mainloop()  # Lancement de la boucle principale de l'application
