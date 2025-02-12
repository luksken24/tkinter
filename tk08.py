import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps
import os
selected_files = []

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
        kausta_sisu = os.listdir(directory)
        for fail in kausta_sisu:
            file_name, file_extension = os.path.splitext(fail)
            if file_extension == ".jpg":
                text_field.insert(tk.END, fail+ "\n")
                selected_files.append(os.path.join(directory, fail))
        print(selected_files)
    else:
        dir_label.config(text="Kasuta ei valitud")

def save_image():
    save_directory = filedialog.askdirectory()
    for file in selected_files:
        img = Image.open(file)
        img = img.resize(200, 200)
        filename = os.path.basename(file)
        img.save(os.path.join(save_directory, filename))
    print("Pildid on salvestatud")


aken = tk.Tk()
aken .title("Pildi suuruse muutmine")
aken.geometry("450x400")

label = tk.Label(aken, text="Pildi suurus 200x200", font="Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height = 10, width = 50)
inputtxt.pack(pady=10)

open_Button = tk.Button(aken, text="Vali Failid", command=open_directory)
open_Button.pack(pady=10)

save_Button = tk.Button(aken, text="Salvesta pildid", command=save_image)
save_Button.pack(pady=10)

dir_label  = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()