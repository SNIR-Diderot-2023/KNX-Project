from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from PIL import ImageTk, Image
import customtkinter
import testPort

root = customtkinter.CTk()
root.title("Ports COM")

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")


testPort.create_widgets()
testPort.refresh_ports()


root.mainloop()
