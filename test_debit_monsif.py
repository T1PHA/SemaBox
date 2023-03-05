import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application graphique")

# Création de quelques widgets
label = tk.Label(fenetre, text="Bienvenue sur l'application graphique de votre semabox", font=("Helvetica", 18))
label.pack()

# Création d'un cadre pour les boutons
cadre_boutons = tk.Frame(fenetre)
cadre_boutons.pack(pady=20)

# Création d'un style pour les boutons
style = ttk.Style()
style.configure('Bouton.TButton', font=('Helvetica', 12), foreground='black', background='#4CAF50', padding=10)

def lancer_tdb():
    subprocess.call(["python", "tdb.py"])

bouton_tdb = ttk.Button(cadre_boutons, text="Ouvrir tableau de bord", command=lancer_tdb, style='Bouton.TButton')
bouton_tdb.pack(side="top", padx=20, pady=10)

def run_script():
    # Run the other script
    subprocess.call(['python', 'scan.py'])

bouton_script_1 = ttk.Button(cadre_boutons, text="Lancer scan réseau", command=run_script, style='Bouton.TButton')
bouton_script_1.pack(side="left", padx=20, pady=10)

def lancer_debit():
    subprocess.call(["python", "debit.py"])

bouton_debit = ttk.Button(cadre_boutons, text="Lancer test de débit", command=lancer_debit, style='Bouton.TButton')
bouton_debit.pack(side="right", padx=20, pady=10)

def lancer_ping():
    subprocess.call(["python", "ping.py"])

bouton_ping = ttk.Button(cadre_boutons, text="Lancer ping", command=lancer_ping, style='Bouton.TButton')
bouton_ping.pack(side="right", padx=20, pady=10)

def lancer_ippublique():
    subprocess.call(["python", "ippublique_DynDNS.py"])

bouton_script_4 = ttk.Button(cadre_boutons, text="IP Publique DynDNS", command=lancer_ippublique, style='Bouton.TButton')
bouton_script_4.pack(side="right", padx=20, pady=10)

# Création d'un bouton pour quitter
bouton_quitter = ttk.Button(fenetre, text="Quitter", command=fenetre.quit, style='Bouton.TButton')
bouton_quitter.pack(pady=20)

# Lancement de la boucle d'événements Tkinter
fenetre.mainloop()
