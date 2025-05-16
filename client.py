import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

root.geometry("180x150+1720+800")
root.title("Stuhl")

def neuerPatientAuswahlSpawner():
    neuerPatientAuswahl = tk.Toplevel()
    neuerPatientAuswahl.title("Name eingeben")
    neuerPatientAuswahl.geometry("180x110+1720+800")
    name_var = tk.StringVar()

    namenEntry = tk.Entry(neuerPatientAuswahl, textvariable=name_var)
    namenEntry.pack(pady=5)
    neuerPatientAuswahl.attributes('-topmost', True)

    def neuerPatientSpawner():
        neuerPatientAuswahl.destroy()

        neuerPatient = tk.Toplevel()
        neuerPatient.attributes("-fullscreen", True)
        neuerPatient.configure(background='green')
        neuerPatient.attributes('-topmost', True)

        patient_name = name_var.get()
        tk.Label(
            neuerPatient, text=patient_name, bg='green', fg="black",
            justify=tk.CENTER, font='Helvetica 128 bold'
        ).pack(pady=412)

        neuerPatient.bind("<Button-1>", lambda event: neuerPatient.destroy())

    submitButton = ttk.Button(neuerPatientAuswahl, text="Fertig", command=neuerPatientSpawner, style='Accent.TButton')
    submitButton.pack(pady=5)

def endkontrolleSpawner():
    endkontrolle = tk.Toplevel()
    endkontrolle.attributes("-fullscreen", True)
    endkontrolle.configure(background='yellow')
    endkontrolle.attributes('-topmost', True)
    tk.Label(
            endkontrolle, text="Endkontrolle", bg='yellow', fg="black",
            justify=tk.CENTER, font='Helvetica 128 bold'
        ).pack(pady=412)
    endkontrolle.bind("<Button-1>", lambda event: endkontrolle.destroy())


neuerPatientButtonFrame = tk.Frame()
neuerPatientButtonFrame.pack(pady=25)

neuerPatientButton = ttk.Button(
    neuerPatientButtonFrame, text="Neuer Patient gesetzt",
    command=neuerPatientAuswahlSpawner, style='Accent.TButton'
)
neuerPatientButton.pack()

endkontrolleButtonFrame = tk.Frame()
endkontrolleButtonFrame.pack()

endkontrolleButton = ttk.Button(
    endkontrolleButtonFrame, text="Endkontrolle",
    command=endkontrolleSpawner, style='Accent.TButton'
)
endkontrolleButton.pack()

root.attributes('-topmost', True)
root.mainloop()
