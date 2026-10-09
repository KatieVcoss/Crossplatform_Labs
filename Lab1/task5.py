from tkinter import *

win = Tk()
win.geometry("250x250+600+150")

# Настройка сетки 3х3: центр растягивается, углы фиксированы
win.columnconfigure(0, weight=0);
win.columnconfigure(1, weight=1);
win.columnconfigure(2, weight=0)
win.rowconfigure(0, weight=0);
win.rowconfigure(1, weight=1);
win.rowconfigure(2, weight=0)

# Список кортежей с параметрами для каждого угла
corners = [
    (0, 0, "en", (50, 0), (50, 0), "1"),
    (0, 2, "wn", (0, 50), (50, 0), "2"),
    (2, 0, "es", (50, 0), (0, 50), "3"),
    (2, 2, "ws", (0, 50), (0, 50), "4")
]

# Цикл с распаковкой параметров для создания угловых фреймов
for row, column, sticky, padx, pady, text in corners:
    frame = Frame(win, borderwidth=10, bg="lime", width=50, height=50)
    # Размещение с привязкой к углам ячейки (sticky) и отступами
    frame.grid(row=row, column=column, sticky=sticky, padx=padx, pady=pady)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)

    lbl = Label(frame, text=text, bg="lime", font=("Arial", 20))
    lbl.grid(sticky="nsew")

win.mainloop()