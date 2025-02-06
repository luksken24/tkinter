import tkinter as tk

def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) >= 5:
        validation_label.config(text="Korras!", fg="green")
    else:
        validation_label.config(text="Sisesta vähemalt 5 märki!", fg="red")

aken = tk.Tk()
aken.title("Validaator")

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Sisesta vähemalt 5 märki!", fg="red")
validation_label.pack()

aken.mainloop()