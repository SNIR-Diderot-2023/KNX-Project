from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from PIL import ImageTk, Image
import customtkinter
# Ecris moi les commentaires en françaos stp merci :D


def refresh_ports():
    ports = list(serial.tools.list_ports.comports())
    port_list.delete(END)
    for port in ports:
        port_list.insert(END, port)

# Avoir le port séléctionné dans la liste


def select_port():
    selection = port_list.curselection()
    if selection:
        global selected_port
        selected_port = port_list.get(selection[0])
        selection_label.configure(text="Port sélectionné : " + selected_port)

    else:
        selection_label.configure(text="Aucun port sélectionné.")

# Ouvre la deuxieme fenetre avec le port séléctionné


def openNewWindow():
    if selected_port != None:

        # Toplevel object which will
        # be treated as a new window
        newWindow = customtkinter.CTkToplevel(root)

        # sets the title of the
        # Toplevel widget
        newWindow.title("Port COM")

        # sets the geometry of toplevel

        newWindow.attributes('-fullscreen', True)
        # A frame widget to center the text
        frame = customtkinter.CTkFrame(newWindow)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.1)

        # frame widget pour le button fermer à gauche
        frame2 = customtkinter.CTkFrame(newWindow)
        frame2.pack()
        frame2.place(anchor='center', relx=0.9, rely=0.1)

        customtkinter.CTkButton(frame2,
                                text="Fermer",
                                command=newWindow.destroy).pack()

        # A Label widget to show in toplevel
        customtkinter.CTkLabel(frame,
                               text=selected_port).pack()

        trame = "00.04.76.9D.1C.BB"

        customtkinter.CTkLabel(frame,
                               text="Trame KNX : " + trame).pack()

        # A button widget which will close the toplevel window

        open_img(newWindow)

# Crée les widgets de la fenetre principale


def create_widgets():

    global select_button
    select_button = customtkinter.CTkButton(
        root, text="Sélectionner", command=select_port)
    select_button.pack()

    port_list_label = customtkinter.CTkLabel(
        root, text="Ports COM disponibles :")
    port_list_label.pack()

    global port_list
    port_list = Listbox(root)
    port_list.pack()

    global selection_label
    selection_label = customtkinter.CTkLabel(
        root, text="Aucun port sélectionné.")
    selection_label.pack()

    global confirm_button
    confirm_button = customtkinter.CTkButton(
        root, text="Confirmer", command=openNewWindow)
    confirm_button.pack()

# Gestion Image


def open_img(master):
    global img
    frame = customtkinter.CTkFrame(master, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.15, rely=0.5)

    img = ImageTk.PhotoImage(file="PreProjet_03_01_2023\Capture.png")
    panel = customtkinter.CTkLabel(frame, image=img)
    panel.pack(side="bottom", fill="both")

# Listbox pour afficher les details de la trame


def ListBoxTrame(master):
    trame_list = Listbox(master)
    trame_list.pack()


root = customtkinter.CTk()
root.title("Ports COM")

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")
root.iconbitmap("icon.ico")


create_widgets()
refresh_ports()


root.mainloop()
