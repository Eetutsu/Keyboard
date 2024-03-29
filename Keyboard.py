import tkinter as tk
import os
from playsound import playsound
import re

directory = 'Keyboard\sounds'
file_names = []

for filename in os.listdir(directory):
    file_names.append(filename)


pattern = r'([A-Ga-g])(b?\d+)\.mp3'


normal_notes = []
flat_notes = []

for file_name in file_names:
    match = re.match(pattern, file_name)
    if match:
        note = match.group(1) + match.group(2)
        if 'b' in note:
            flat_notes.append(note)
        else:
            normal_notes.append(note)

normal_notes = (sorted(normal_notes, key=lambda x: int("".join([i for i in x if i.isdigit()]))))
flat_notes = (sorted(flat_notes, key=lambda x: int("".join([i for i in x if i.isdigit()]))))

window = tk.Tk()
window.geometry("1650x250")
greeting = tk.Label(text="Tervetuloa kosketinsoittimeen")
greeting.pack()
x_pos = 0
y_pos = 100
for key in normal_notes:
    x_pos = x_pos+30
    tk.Button(window, text = key, command = lambda: playsound(f'Keyboard\sounds\{file_names}'), width=3,background="white").place(x=x_pos,y=y_pos)   
x_pos = 25
y_pos = 75
for key in flat_notes:
   x_pos = x_pos+30
   tk.Button(window, text = key, command = lambda: playsound(f'Keyboard\sounds\{file_names}'), width=2,background="black").place(x=x_pos,y=y_pos)      



tk.mainloop()