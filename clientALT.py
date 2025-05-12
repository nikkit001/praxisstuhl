import tkinter as tk
from tkinter import ttk

stuhl = "stuhl1"

root = tk.Tk()

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.geometry("150x80")
root.title("Stuhl")


def gelbAuswahl():
    gelbAuswahl = tk.Toplevel()
    gelbAuswahl.geometry("130x100")
    gelbAuswahl.attributes('-topmost', True)

    def gelbNormal():
        gelbAuswahl.destroy()
        gelb = tk.Toplevel()
        gelb.attributes("-fullscreen", True)
        gelb.configure(background='yellow')
        def destroy():
            gelb.destroy()
        gelb.bind("<Button-1>", lambda event: gelb.destroy())

    def gelbLais():
        gelbAuswahl.destroy()
        gelb = tk.Toplevel()
        gelb.attributes("-fullscreen", True)
        gelb.configure(background='yellow')
        tk.Label(gelb, text='Lais', bg='yellow', fg="black", justify=tk.CENTER, font='Helvetica 128 bold').pack(pady=412)
        def destroy():
            gelb.destroy()
        gelb.bind("<Button-1>", lambda event: gelb.destroy())

    def gelbPfeffer():
        gelbAuswahl.destroy()
        gelb = tk.Toplevel()
        gelb.attributes("-fullscreen", True)
        gelb.configure(background='yellow')
        tk.Label(gelb, text='Pfeffer', bg='yellow', fg="black", justify=tk.CENTER, font='Helvetica 128 bold').pack(pady=412)
        def destroy():
            gelb.destroy()
        gelb.bind("<Button-1>", lambda event: gelb.destroy())

    leerButton = ttk.Button(gelbAuswahl, text="Leer", command=gelbNormal, style='Accent.TButton')
    leerButton.pack()

    laisButton = ttk.Button(gelbAuswahl, text="Lais", command=gelbLais)
    laisButton.pack()

    pfefferButton = ttk.Button(gelbAuswahl, text="Pfeffer", command=gelbPfeffer)
    pfefferButton.pack()


gelbButtonFrame = tk.Frame()
gelbButtonFrame.pack(pady=25)
gelbButton = ttk.Button(gelbButtonFrame, text="gelb", command=gelbAuswahl, style='Accent.TButton')
gelbButton.pack()


root.attributes('-topmost', True)
root.mainloop()