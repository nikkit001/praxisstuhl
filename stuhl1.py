import tkinter as tk
from tkinter import ttk
import socket

stuhl = "stuhl1"

root = tk.Tk()

root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")
root.geometry("200x200")
root.title("Stuhl 1")

def gelb():
    gelb = tk.Toplevel()
    gelb.attributes("-fullscreen", True)
    gelb.configure(background='yellow')
    def destroy():
        gelb.destroy()
    gelb.bind("<Button-1>", lambda event: destroy())

panelButtonFrame = tk.Frame()
panelButtonFrame.pack(pady=20)
panelButton = ttk.Button(panelButtonFrame, text='Stuhlübersicht', style='Accent.TButton')
panelButton.pack()

gelbButtonFrame = tk.Frame()
gelbButtonFrame.pack(pady=5)
gelbButton = ttk.Button(gelbButtonFrame, text="gelb", command=gelb)
gelbButton.pack()

rotButtonFrame = tk.Frame()
rotButtonFrame.pack(pady=5)
rotButton = ttk.Button(rotButtonFrame, text="rot")
rotButton.pack()

root.attributes('-topmost', True)
root.mainloop()