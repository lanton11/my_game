from tkinter import *

game_width = 400
game_height = 400
snake_item = 10

tk = Tk()
tk.title("Игра змейка на Python")
tk.resizable(0,0)
tk.wm_attributes("-topmost",-1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
