from tkinter import *

win = Tk()
win.geometry("400x200+500+200")

# функция-обработчик события изменения размеров окна
def change_size(event):
    # Обновление заголовка
    win.title(f"Ширина окна: {event.width}  Высота окна: {event.height}")

# Привязка события к окну
win.bind("<Configure>", change_size)
win.mainloop()