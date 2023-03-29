import subprocess
import tkinter as tk

def check_internet_connection():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        
        # Si le code de retour est égal à 0, l'ordinateur est connecté à Internet
        if result.returncode == 0:
            # Obtenir la latence à partir de la sortie de la commande ping
            latency = result.stdout.decode('utf-8').split('\n')[-2].split(' ')[-2].split('/')[1]
            # Mettre à jour l'étiquette avec le message "Connecté à Internet" et la latence
            label['text'] = f'Connecté à Internet\nLatence: {latency} ms'
        else:
            # Mettre à jour l'étiquette avec le message "Non connecté à Internet"
            label['text'] = 'Non connecté à Internet'
    except Exception as e:
        # En cas d'erreur, mettre à jour l'étiquette avec le message d'erreur
        label['text'] = 'Error: ' + str(e)

# Créer la fenêtre principale
root = tk.Tk()
# Créer une étiquette vide
label = tk.Label(root, text='')
# Ajouter l'étiquette à la fenêtre principale
label.pack()

# Vérifier la connexion Internet
check_internet_connection()
# Lancer la boucle d'événements Tkinter
root.mainloop()

