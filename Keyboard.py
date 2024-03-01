import tkinter as tk
from winsound import *
from playsound import playsound

playC1 = lambda: playsound('sounds\piano-mp3_C1.mp3')
playD1 = lambda: playsound('sounds\piano-mp3_D1.mp3')
playE1 = lambda: playsound('sounds\piano-mp3_E1.mp3')
playDb1 = lambda: playsound('sounds\piano-mp3_Db1.mp3')
playEb1 = lambda: playsound('sounds\piano-mp3_Eb1.mp3')
whiteKeys = [("C1",playC1),("D1",playD1),("E1",playE1)]
blackKeys = [("Db1",playDb1),("Eb1",playEb1)]
window = tk.Tk()
window.geometry("500x500")
greeting = tk.Label(text="Tervetuloa kosketinsoittimeen")
greeting.pack()
x_pos = 0
y_pos = 100
for key in whiteKeys:
    x_pos = x_pos+50
    tk.Button(window, text = key[0], command = key[1], width=5,background="white").place(x=x_pos,y=y_pos)   
x_pos = 25
y_pos = 75
for key in blackKeys:
    x_pos = x_pos+50
    tk.Button(window, text = key[0], command = key[1], background="black", fg="white").place(x=x_pos,y=y_pos)   



tk.mainloop()