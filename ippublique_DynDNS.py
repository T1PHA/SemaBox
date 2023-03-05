import tkinter as tk
import socket
import requests
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Récupération d'informations réseau")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.recovery_button = tk.Button(self, text="Lancer la récupération", command=self.recover_info)
        self.recovery_button.pack(side="top")

    def recover_info(self):
        ip = requests.get('https://api.ipify.org').text
        hostname = socket.gethostname()
        message = f"Adresse IP publique : {ip}\nNom DNS de la machine : {hostname}"
        messagebox.showinfo("Résultat de la récupération", message)

root = tk.Tk()
app = Application(master=root)
app.mainloop()