import tkinter as tk
from winsound import *
from playsound import playsound

playA0 = lambda: playsound('sounds\piano-mp3_A0.mp3')
playA1 = lambda: playsound('sounds\piano-mp3_A1.mp3')
whiteKeys = [("A0",playA0),("A1",playA1)]
window = tk.Tk()
window.geometry("500x500")
greeting = tk.Label(text="Tervetukia kosketinsoittimeen")
greeting.pack()
x_pos = 0
y_pos = 100
for key in whiteKeys:
    x_pos = x_pos+25
    tk.Button(window, text = key[0], command = key[1]).place(x=x_pos,y=y_pos)   



tk.mainloop()