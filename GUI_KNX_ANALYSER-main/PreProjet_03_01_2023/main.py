# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
import serial.tools.list_ports
import test
import tkinter.ttk as ttk

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("1960x1080")


image=test.ImagePrinter(win)


#Création des buttons des ports séries 


win.mainloop()