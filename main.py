import tkinter as tk
import subprocess

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application graphique")

# Création de quelques widgets
label = tk.Label(fenetre, text="Bienvenue sur l'application graphique de votre semabox")
label.pack()

# Création d'un cadre pour les boutons
cadre_boutons = tk.Frame(fenetre)
cadre_boutons.pack()

def lancer_tdb():
    subprocess.call(["python", "tdb.py"])

bouton_tdb = tk.Button(cadre_boutons, text="Ouvrir tableau de bord", command=lancer_tdb)
bouton_tdb.pack(side="top")


# Création de quelques widgets
# nom = "John"
# age = 30
# message = "Nom: " + nom + "\nAge: " + str(age)
# label = tk.Label(fenetre, text=message)
# label.pack()


# Création des boutons
def run_script():
    # Run the other script
    subprocess.call(['python', 'scan.py'])

bouton_script_1 = tk.Button(cadre_boutons, text="Lancer scan réseau", command=run_script)
bouton_script_1.pack(side="left")

def lancer_debit():
    subprocess.call(["python", "debit.py"])

# def lancer_script_3():
#     subprocess.call(["python", "script3.py"])

bouton_debit = tk.Button(cadre_boutons, text="Lancer test de débit", command=lancer_debit)
bouton_debit.pack(side="right")


def lancer_ping():
    subprocess.call(["python", "ping.py"])

bouton_ping = tk.Button(cadre_boutons, text="Lancer ping", command=lancer_ping)
bouton_ping.pack(side="right")

def lancer_ippublique():
    subprocess.call(["python", "ippublique_DynDNS.py"])

bouton_script_4 = tk.Button(cadre_boutons, text="IP Publique DynDNS", command=lancer_ippublique)
bouton_script_4.pack(side="right")

# Création d'un bouton pour quitter
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

# Lancement de la boucle d'événements Tkinter
fenetre.mainloop()