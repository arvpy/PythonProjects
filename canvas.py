#  Drawing Canvas

"""  Simple drawing app
Single Key commands
R-Red, G-Green, B-Blue  C-clear"""
from tkinter import *


root = Tk()
c = Canvas(root, width=500, height=500)
c.grid(row=0, column=0)
draw_color = 'red'

def mouse_move(event):
    c.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, outline=draw_color, fill=draw_color)

c.bind('<B1-Motion>', mouse_move)
def key_press(event):
    global draw_color

    ch = event.char.upper()
    if ch == 'C':
        c.delete('all')
    if ch == 'R':
        draw_color = 'red'
    if ch == 'B':
        draw_color = 'blue'
    if ch == 'G':
        draw_color = 'green'

c.bind('<KeyPress>', key_press)



# c.create_rectangle(100, 100, 200, 600, outline='blue', fill='blue')

c.focus_set()  # Set keyboard focus to canvas
root.mainloop()
