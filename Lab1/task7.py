from tkinter import *

win = Tk()
win.geometry("250x250+600+150")

# Настройка сетки 3х3
win.columnconfigure(0, weight=0); win.columnconfigure(1, weight=1); win.columnconfigure(2, weight=0)
win.rowconfigure(0, weight=0); win.rowconfigure(1, weight=1); win.rowconfigure(2, weight=0)

# Функция создания фрейма с добавлением параметров внешних отступов (padx, pady)
def fr_creation(Win, row, column, sticky, padx=0, pady=0):
    fr = Frame(Win, borderwidth=10, relief="ridge", bg="lime", width=50, height=50)
    fr.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

# Размещение 8 фреймов по периметру с заданными отступами от краев окна
fr_creation(win, 0, 0, "nw", padx=10, pady=10)
fr_creation(win, 0, 2, "ne", padx=10, pady=10)
fr_creation(win, 2, 0, "sw", padx=10, pady=10)
fr_creation(win, 2, 2, "se", padx=10, pady=10)

fr_creation(win, 0, 1, "n", pady=10)
fr_creation(win, 1, 0, "w", padx=10)
fr_creation(win, 1, 2, "e", padx=10)
fr_creation(win, 2, 1, "s", pady=10)

# Загрузка изображения и его уменьшение в 5 раз
pic = PhotoImage(file="pic.png").subsample(5)
lbl_image = Label(win, image=pic)
# Размещение изображения в центральной растягиваемой ячейке
lbl_image.grid(row=1, column=1)

win.mainloop()