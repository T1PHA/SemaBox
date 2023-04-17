import pytest
import urllib.request
import subprocess
from django.test import TestCase
from django.urls import reverse
import ping3
from .views import main
from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
import unittest
import tkinter as tk
import socket
import threading
from scapy.all import ARP, Ether, srp


@pytest.mark.parametrize("url", [
    "http://speedtest.ftp.otenet.gr/files/test100k.db"
])
def test_ping_url(url):
    try:
        urllib.request.urlopen(url)
    except:
        pytest.fail(f"Could not ping URL: {url}")

def test_nslookup():
    # exécuter la commande NSLOOKUP
    result = subprocess.run(['nslookup', 'www.google.com'], capture_output=True)

    # vérifier que la commande a réussi
    assert result.returncode == 0

    # extraire le nom du serveur et le nom de domaine de la sortie de la commande
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')
    server_name = 'semabox'
    domain_name = 'cm4.local'
    for line in lines:
        if line.startswith('Server:'):
            server_name = line.split(':')[1].strip()
        elif line.startswith('Name:'):
            domain_name = line.split(':')[1].strip()

    # vérifier que le nom du serveur et le nom de domaine ont été extraits avec succès
    assert server_name != 'semabox'
    assert domain_name != 'cm4.local'

def run_test(self):
    # Exécuter le test
    result = pytest.main(['-q', '--disable-pytest-warnings', __file__])

    # Extraire le nom du serveur DNS de la sortie de la commande
    output = subprocess.run(['nslookup', 'www.google.com'], capture_output=True).stdout.decode('utf-8')
    lines = output.split('\n')
    server_name = ''
    for line in lines:
        if line.startswith('Server:'):
            server_name = line.split(':')[1].strip()

    # Afficher le résultat du test dans l'étiquette
    if result == pytest.ExitCode.OK and server_name != '':
        self.result_label.config(text=f"Le test a réussi ! Nom du serveur DNS : {server_name}. OK", fg="green")
    else:
        self.result_label.config(text="Le test a échoué !", fg="red")




class MainTestCase(TestCase):
    def test_main(self):
        # Créer une liste de machines pour tester
        machines = [
            {'name': 'Semabox 1', 'ip': '192.168.29.132'},
            {'name': 'Semabox 2', 'ip': '192.168.29.136'},
            {'name': 'Semabox 3', 'ip': '192.168.29.135'},
        ]
        for machine in machines:
            machine['Etat'] = 'En ligne' if ping3.ping(machine['ip']) else 'Hors ligne'

        # Appel à la fonction "main" de views.py
        response = self.client.get(reverse('main'))

        # Vérifier que la réponse est valide
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

        # Vérifier que les machines sont affichées sur la page HTML
        for machine in machines:
            self.assertContains(response, machine['name'])
            self.assertContains(response, machine['ip'])
            self.assertContains(response, machine['Etat'])


class MachineRestartTestCase(TestCase):

    @patch('paramiko.SSHClient')
    def test_machine_restart(self, mock_ssh_client):
        """
        Vérifie si la machine se redémarre correctement lorsque le bouton "Redémarrer la machine" est cliqué
        """
        # Configuration de l'environnement pour le test
        c = Client()
        machines = [
            {'name': 'Semabox 1', 'ip': '192.168.29.132'},
            {'name': 'Semabox 2', 'ip': '192.168.29.136'},
            {'name': 'Semabox 3', 'ip': '192.168.29.135'},
        ]
        context = {'machines': machines}
        
        # Création d'une instance de SSHClient et simulation de l'exécution de la commande de redémarrage
        ssh_instance = MagicMock()
        ssh_instance.exec_command.return_value = (None, None, None)
        mock_ssh_client.return_value = ssh_instance
        
        # Envoi d'une requête POST pour redémarrer la machine
        response = c.post('/simple_function', {'ip': '192.168.29.132'})
        
        # Vérification de l'exécution de la commande de redémarrage sur la machine
        ssh_instance.exec_command.assert_called_once_with('sudo reboot')
        
        # Vérification de la réponse HTTP
        self.assertEqual(response.status_code, 200)

class TestDashboard(TestCase):
    def test_dashboard_display(self):
        # Créer un client HTTP
        client = Client()

        # Envoyer une requête GET à la page du tableau de bord
        response = client.get(reverse('machine_info.html'))

        # Vérifier que la réponse est un succès (200 OK)
        self.assertEqual(response.status_code, 200)

        # Vérifier que la page affiche les informations correctes
        self.assertContains(response, '<h1>Tableau de bord de Test</h1>')
        self.assertContains(response, '<p>Adresse IP de la machine distante : 192.168.29.132</p>')
        self.assertContains(response, '<p>Résultat du test de débit : MBytes/s</p>')
        self.assertContains(response, '<p>Nom de la machine : Semabox 1</p>')
        self.assertContains(response, '<p>Machine bien connectée</p>')
        self.assertContains(response, '<h2>Machines connectées :</h2>')
        self.assertContains(response, '<p> 192.168.29.136 </p>')



class TestInternetConnection(unittest.TestCase):

    def test_connection_string(self):
        # Vérifier que la fonction retourne une chaîne de caractères
        self.assertIsInstance(check_internet_connection(), str)

    def test_connection_latency(self):
        # Vérifier que la latence est un nombre décimal
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        latency = result.stdout.decode('utf-8').split('\n')[-2].split(' ')[-2].split('/')[1]
        self.assertTrue(latency.isdecimal())

    def test_connection_exception(self):
        # Vérifier que la fonction ne lève pas d'exception
        try:
            check_internet_connection()
        except:
            self.fail("La fonction a levé une exception.")

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
    return label['text']

# Créer la fenêtre principale
root = tk.Tk()
# Créer une étiquette vide
label = tk.Label(root, text='')
# Ajouter l'étiquette à la fenêtre principale
label.pack()

class ApplicationTest(unittest.TestCase):
    def test(self):
        # Vérifier que l'application se lance sans exception
        try:
            # Vérifier la connexion Internet
            check_internet_connection()
            # Lancer la boucle d'événements Tkinter
            root.mainloop()
        except:
            self.fail("L'application a levé une exception.")

if __name__ == '__main__':
    unittest.main()

class PortScanner:
    root = tk.Tk()

    def __init__(self, master):
        self.master = master
        self.master.title("Port Scanner")

        # Ajout d'un champ d'entrée pour l'adresse IP
        self.ip_label = tk.Label(self.master, text="IP Address:")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(self.master)
        self.ip_entry.pack()

        # Ajout d'un champ d'entrée pour la plage de ports à scanner
        self.port_range_label = tk.Label(self.master, text="Port Range:")
        self.port_range_label.pack()
        self.port_range_entry = tk.Entry(self.master)
        self.port_range_entry.insert(tk.END, "1-1000")
        self.port_range_entry.pack()

        # Ajout d'un bouton pour lancer le scan
        self.scan_button = tk.Button(self.master, text="Scan", command=self.scan_ports)
        self.scan_button.pack()

        # Ajout d'un champ de texte pour afficher les résultats
        self.result_text = tk.Text(self.master)
        self.result_text.pack()

        # Test 1 : Vérifier que le scan stock bien les ports dans un tableau
        def test_port_storage():
            scanner = PortScanner(tk.Tk())
            scanner.scan_ports()
            ports = scanner.ports
            assert isinstance(ports, list), "Ports should be stored in a list"
            assert len(ports) > 0, "At least one port should be stored"

        # Test 2 : Vérifier que le scan de port donne bien les ports ouverts à la fin du scan
        def test_open_ports():
            scanner = PortScanner(tk.Tk())
            scanner.scan_ports()
            ports = scanner.ports
            open_ports = [port for port in ports if port["status"] == "open"]
            assert len(open_ports) > 0, "At least one port should be open"

        # Test 3 : Vérifier qu’il soit possible de relancer un scan de port à la fin du scan
        def test_scan_again():
            scanner = PortScanner(tk.Tk())
            scanner.scan_ports()
            scanner.scan_ports()
            ports = scanner.ports
            assert len(ports) > 0, "At least one port should be stored after second scan"

    # Récupération de l'adresse IP entrée
    def scan_ports(self):
        # Récupération de l'adresse IP entrée
        ip = self.ip_entry.get()

        # Récupération de la plage de ports à scanner
        port_range = self.port_range_entry.get().split('-')
        start_port = int(port_range[0])
        end_port = int(port_range[1])

        # Scan des ports pour chaque machine du réseau
        for port in range(start_port, end_port + 1):
            # Utilisation de threads pour accélérer le scan
            thread = threading.Thread(target=self.scan_port, args=(ip, port))
            thread.start()

    host = socket.gethostname()

    # obtenir la liste des noms de machines dans le réseau local
    arp = ARP(pdst="192.168.29.0/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result_text = tk.Text(root)
    # Envoi de la requête ARP et récupération des réponses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Affichage des adresses MAC et IP des machines qui ont répondu
    for sent, received in result:
        result_text.insert(tk.END, f"MAC Address: {received.hwsrc} - IP Address: {received.psrc}\n")
    result_text.pack()

    root.geometry("500x200")
    root.mainloop()

    def scan_port(self, ip, port):
        # Tentative de connexion à un port sur une machine
        try:
            # Création d'un objet socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()

            # Si la connexion est réussie, le port est ouvert
            if result == 0:
                self.result_text.insert(tk.END, f"Port {port} is open\n")

        except:
            pass


root = tk.Tk()
scanner = PortScanner(root)
root.geometry("300x300")
root.mainloop()