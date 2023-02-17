import tkinter as tk
import time
import urllib.request

# URL du fichier à télécharger
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
  result_window = tk.Toplevel()
  result_window.title("Résultat du speedtest")
  result_label = tk.Label(result_window, text=f"Vitesse de téléchargement : {speed / 1024 / 1024:.2f} Mo/s")
  result_label.pack()

# Création de la fenêtre principale
window = tk.Tk()
window.title("Speedtest")

# Création du bouton "Lancer le speedtest"
start_button = tk.Button(window, text="Lancer le speedtest", command=start_speedtest)
start_button.pack()

# Affichage de la fenêtre principale
window.mainloop()