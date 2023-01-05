from tkinter import *
from tkinter import ttk
import serial
import serial.tools.list_ports
from PIL import ImageTk, Image 


def refresh_ports():
    ports = list(serial.tools.list_ports.comports())
    port_list.delete(0, END)
    for port in ports:
        port_list.insert(END, port)

def select_port():
    selection = port_list.curselection()
    if selection:
        global selected_port 
        selected_port = port_list.get(selection[0])
        selection_label.config(text="Port sélectionné : " + selected_port)
        
    else:
        selection_label.config(text="Aucun port sélectionné.")
        print(selected_port[0:3])




def openNewWindow():
    if selected_port!=None: 
        

        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(root)
    
        # sets the title of the
        # Toplevel widget
        newWindow.title("Port COM")
    
        # sets the geometry of toplevel
        newWindow.geometry("1960x1080")
        # A frame widget to center the text
        frame = Frame(newWindow)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.1)
        
        # A Label widget to show in toplevel
        Label(frame,
            text =selected_port).pack()
        open_img(newWindow)
        
        
        
        

        
        

def create_widgets():
    
    global select_button
    select_button = Button(root, text="Sélectionner", command=select_port)
    select_button.pack()


    port_list_label = Label(root, text="Ports COM disponibles :")
    port_list_label.pack()

    global port_list
    port_list = Listbox(root)
    port_list.pack()

    global selection_label
    selection_label = Label(root, text="Aucun port sélectionné.")
    selection_label.pack()

    global confirm_button
    confirm_button = Button(root, text="Confirmer", command=openNewWindow)
    confirm_button.pack()



def open_img(master):
    global img
    frame = Frame(master, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.09, rely=0.5)
    path = r"Nouveau Projet.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(frame, image=img)
    panel.pack(side="bottom", fill="both")



root = Tk()
root.title("Ports COM")

create_widgets()
refresh_ports()


root.mainloop()

    