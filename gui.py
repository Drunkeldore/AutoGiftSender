from tkinter import *
from tkinter import ttk
from main import go_to_friendlist, cycling_friends

BUTTON_WIDTH = 45

root = Tk()
root.title("PokemonGo Autogifter")
root.geometry("500x400")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Make sure your phone is\n connected before you start\n anything!\n\n\n||-------------===-------------||\n\n"
                    "1. Click Go to Friends.\n This is seperate just so we can\n make sure things are working.\n\n\n\n||-------------===-------------||\n\n"
                    "2. Click Auto Gift Activate!\n Hopefully it does it's magic!").grid(column=0, row=0,rowspan=100, sticky="w")

ttk.Button(frm, text="Friends List", command=go_to_friendlist).grid(column=1, row=0)

ttk.Button(frm, text="(╬▔皿▔)╯|--Auto Gift Activate--|╰(艹皿艹 )", command=cycling_friends).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)


root.mainloop()