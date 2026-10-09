from tkinter import *

win = Tk()
win.geometry("150x150+600+150")

# Настройка сетки 3х3: центр растягивается, периметр фиксирован
win.columnconfigure(0, weight=0); win.columnconfigure(1, weight=1); win.columnconfigure(2, weight=0)
win.rowconfigure(0, weight=0); win.rowconfigure(1, weight=1); win.rowconfigure(2, weight=0)

# Функция для создания и размещения фрейма
def fr_creation(Win, row, column, sticky):
    fr = Frame(Win, borderwidth=10, relief="ridge", bg="lime", width=50, height=50)
    fr.grid(row=row, column=column, sticky=sticky)

# Размещение 8 фреймов по периметру сетки с соответствующим прижатием (sticky)
fr_creation(win, 0, 0, "nw")
fr_creation(win, 0, 2, "ne")
fr_creation(win, 2, 0, "sw")
fr_creation(win, 2, 2, "se")

fr_creation(win, 0, 1, "n")
fr_creation(win, 1, 0, "w")
fr_creation(win, 1, 2, "e")
fr_creation(win, 2, 1, "s")

win.mainloop()