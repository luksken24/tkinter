import tkinter as tk
from PIL import Image, ImageTk

def kuva_pilt(aken, failinimi, laius, korgus):
    pilt = Image.open(failinimi)
    pilt = pilt.crop((0, 0, laius, korgus))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    aken = tk.Tk()
    aken.title("Mario Ülesanded")
    aken.geometry("400x400")
    aken.resizable(True, False)

    label = tk.Label(aken, text="Cuk Murris", font =("Arial",16,"bold"), fg="blue").pack()
    kuva_pilt(aken, "norris.jpg", 200, 200)
 # Text näide
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12, "bold"))
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)
    failisisu = loe_fail("text.txt")
    tekst.insert(tk.INSERT, failisisu)



    aken.mainloop()

if __name__ == "__main__":
    main()