import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from main import go_to_friendlist, cycling_friends, run_exe

BUTTON_WIDTH = 45

root = Tk()
root.title("PokemonGo Autogifter")
root.geometry("500x400")

bg = PhotoImage(file="format_pokemongo_bg.png")
style = ttk.Style()
style.configure("TButton", background="blue", padding=6, relief="flat")
# Show image using label
canvas = tk.Canvas(root, height=200, width=500).place(relwidth=1, relheight=1)
tk.Label(canvas, image=bg).place(relwidth=1, relheight=1)


#k.Label(canvas, text="Make sure your phone is\n connected before you start\n anything!\n\n\n||-------------===-------------||\n\n"
#                    "1. Click Go to Friends.\n This is seperate just so we can\n make sure things are working.\n\n\n\n||-------------===-------------||\n\n"
 #                   "2. Click Auto Gift Activate!\n Hopefully it does it's magic!",
 #                   bg="black", fg="#652828", bd=1).grid(column=0, row=0,rowspan=100, sticky="w")

ttk.Button(text="Friends List", width=BUTTON_WIDTH, command=go_to_friendlist).place(x=110, y=175)

ttk.Button(text="(╬▔皿▔)╯|--Auto Gift Activate--|╰(艹皿艹 )", width=BUTTON_WIDTH, command=cycling_friends, style="TButton").place(x=110, y=205)
ttk.Button(text="Quit", width=BUTTON_WIDTH, command=root.destroy).place(x=110, y=350)
ttk.Button(text="Show Screen", width=BUTTON_WIDTH, command=run_exe).place(x=110, y=235)


root.mainloop()