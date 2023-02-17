import subprocess
import tkinter as tk

def check_internet_connection():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], stdout=subprocess.PIPE)
        
        if result.returncode == 0:
            latency = result.stdout.decode('latin1').split('\n')[-2].split(' = ')[-1]
            label['text'] = f'Connected to the Internet\nLatency: {latency}'
        else:
            label['text'] = 'Not connected to the Internet'
    except Exception as e:
        label['text'] = 'Error: ' + str(e)

root = tk.Tk()
label = tk.Label(root, text='')
label.pack()

check_internet_connection()
root.mainloop()