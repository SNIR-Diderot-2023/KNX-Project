import tkinter as tk
from tkinter.filedialog import *
import serial 
import serial.tools.list_ports
from tkinter import ttk
name=serial.tools.list_ports.comports()
window2 = tk.Tk()
window2.title("Mon programme2")
#Button cliqué

    
# Créer un bouton et l'ajouter à la fenêtre
button2 = tk.Button(window2, text="page 2")
button2.pack()

# Créer la fenêtre principale
window = tk.Tk()
window.title("Mon programme")
#Button cliqué
def pressed_Button():
    window.quit
    
# Créer un bouton et l'ajouter à la fenêtre
button = ttk.Button(window, text=name,command=pressed_Button)
button.pack()
button.config(command=pressed_Button)


ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p)

# Afficher la fenêtre
window.mainloop()




