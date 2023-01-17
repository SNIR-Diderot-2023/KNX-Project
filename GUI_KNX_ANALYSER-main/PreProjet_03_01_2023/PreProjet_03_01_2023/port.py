#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
# --- functions ---

def on_select(event=None):
    print('----------------------------')

    if event:
        print("event.widget:", event.widget.get())

    for i, x in enumerate(all_comboboxes):
        print("all_comboboxes[%d]: %s" % (i, x.get()))

# --- main ---

root = tk.Tk()

all_comboboxes = []

cb = ttk.Combobox(root, values=(ports))
cb.set("1")
cb.pack()
cb.bind('<<ComboboxSelected>>', on_select)

all_comboboxes.append(cb)



b = tk.Button(root, text=ports, command=on_select)
b.pack()


root.mainloop()