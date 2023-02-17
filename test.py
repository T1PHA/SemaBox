import tkinter as tk
import time
import urllib.request

# URL du fichier à télécharger
url = "http://speedtest.ftp.otenet.gr/files/test100k.db"

# Taille du fichier en octets
size_in_bytes = 102400

# Liste des 5 derniers speedtest
speedtest_historyy = []

# Fonction appelée lorsque le bouton "Lancer le speedtest" est cliqué
def start_speedtest():
  speedtest_history = []
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
  
  # Ajout du résultat du speedtest à l'historique
  speedtest_history.append(speed / 1024 / 1024)

  # Limitation de l'historique à 5 éléments
  speedtest_history = speedtest_history[-5:]

  # Affichage de la vitesse de téléchargement en Mo/s dans une nouvelle fenêtre
  result_window = tk.Toplevel()
  result_window.title("Résultat du speedtest")
  result_label = tk.Label(result_window, text=f"Vitesse de téléchargement : {speed / 1024 / 1024:.2f} Mo/s")
  result_label.pack()
  speedtest_historyy.append(speedtest_history)
# Fonction appelée lorsque le bouton "Historique" est cliqué
def show_history():
  # Affichage de l'historique des speedtest dans une nouvelle fenêtre
  history_window = tk.Toplevel()
  history_window.title("Historique des speedtest")
  history_label = tk.Label(history_window, text="\n".join(f"{i+1}. {speed:.2f} Mo/s" for i, speed in enumerate(speedtest_historyy)))
  history_label.pack()

# Création de la fenêtre principale
window = tk.Tk()
window.title("Speedtest")

# Création du bouton "Lancer le speedtest"
start_button = tk.Button(window, text="Lancer le speedtest", command=start_speedtest)
start_button.pack()

# Création du bouton "Historique"
history_button = tk.Button(window, text="Historique", command=show_history)
start_button.pack()
window.mainloop()