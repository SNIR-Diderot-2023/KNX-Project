from tkinter import *
from tkinter import ttk
import serial.tools.list_ports
from PIL import ImageTk, Image  

ports = list(serial.tools.list_ports.comports())



root = Tk()
root.geometry("1000x100")
#Ouvre une nouvelle page mais l'ancienne est toujours présente 
def openNewWindow():
    
    newWindow = Toplevel(root)
    newWindow.title('Page numéro 2')
    image1 = Image.open("Diderot.png")
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("Diderot.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()
    
    
    
#fais disparaître le button d'avant donc plus rapide et efficace 
def Invisible():
   
    
    button.pack_forget()
    cb.pack_forget()
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("Diderot.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame,text='Choix pris en compte, veuillez quitter la page')
    label.pack()
  
   
#Cette classe permet d'afficher les images et de gérer leurs tailles
class ImagePrinter:
    def __init__(self, master):
        
        self.frame = Frame(master, width=600, height=600)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.25, rely=0.5)

        self.frameText = Frame(master, width=400, height=100)
        self.frameText.pack()
        self.frameText.place(anchor='center', relx=0.5, rely=0.3)

        

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("téléchargé.png"))

        self.img2 = (Image.open("Diderot.png"))
        #Taille image diderot

        self.resized_image= self.img2.resize((273,200), Image.ANTIALIAS)
        self.Diderot= ImageTk.PhotoImage(self.resized_image)

        # Create a self.Label Widget to display the text or Image
        self.label = Label(master =self.frame, image = self.img)
        self.label.pack()

        self.label2 = Label(self.frame, image=self.Diderot)
        self.label2.pack()
        self.img2.image = self.img

            
def on_select(SelectedPort,event=None):
    print('----------------------------')

 

    for i, x in enumerate(all_comboboxes):
        SelectedPort= (i, x.get())
        yo=print(SelectedPort)
        return(yo)
    


all_comboboxes = []
cb = ttk.Combobox(root, values=ports)
cb.set("Selectionne le Port")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

all_comboboxes.append(cb)
button = Button(root, text="Show all selections", command=Invisible)
button.pack()


root.mainloop()
