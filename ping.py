# import tkinter as tk
# import subprocess

# # Créer une fenêtre Tkinter
# window = tk.Tk()
# window.title("Test de latence d'Internet")

# # Créer un label pour afficher la latence de ping
# label = tk.Label(text="Calcul de la latence...")
# label.pack()

# # Fonction qui met à jour le label avec la latence de ping
# def update_latency():
#     # Utiliser la commande ping pour obtenir la latence
#     result = subprocess.run(["ping", "-c", "1", "www.google.com"], capture_output=True)
#     # Extraire la latence du résultat
#     latency = result.stdout.decode("latin1").split("\n")[-2].split(" = ")[-1].split("/")[0]
#     # Mettre à jour le label avec la latence
#     label.config(text=f"Latence : {latency} ms")
#     # Mettre à jour la fenêtre
#     window.update()
#     # Planifier une mise à jour dans 1 seconde
#     window.after(1000, update_latency)

# # Planifier la première mise à jour
# window.after(1000, update_latency)

# # Afficher la fenêtre
# window.mainloop()



import subprocess
import tkinter as tk

def check_internet_connection():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        
        if result.returncode == 0:
            latency = result.stdout.decode('latin1').split('\n')[-2].split(' = ')[-1]
            label['text'] = f'Connecté à Internet\nLatency: {latency}'
        else:
            label['text'] = 'Non connecté à Internet'
    except Exception as e:
        label['text'] = 'Error: ' + str(e)

root = tk.Tk()
label = tk.Label(root, text='')
label.pack()

check_internet_connection()
root.mainloop()