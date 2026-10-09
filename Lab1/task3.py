from tkinter import *

win = Tk()
win.geometry("450x145+600+150")
win.columnconfigure(0, weight=1)

colors = ["red", "orange", "yellow", "lime", "#007dff", "blue", "#7d00ff"]
labels = ["красный", "оранжевый", "жёлтый", "зелёный", "голубой", "синий", "фиолетовый"]

for i in range(7):
    if i % 2 == 0: # Для четных строк создаем растягиваемый фрейм (sticky="ew")
        fr = Frame(win, borderwidth=2, relief="raised", bg=colors[i], height=20)
        fr.grid(row=i, column=0, sticky="ew")
    else: # Для нечетных строк создаем фрейм фиксированной ширины
        fr = Frame(win, borderwidth=2, relief="raised", bg=colors[i], width=400, height=20)
        fr.grid(row=i, column=0)

    lb = Label(fr, text=labels[i], bg=colors[i])
    # Использование place() вместо grid(): метка заполняет фрейм, но не меняет его фиксированный размер
    lb.place(relx=0, rely=0, relwidth=1, relheight=1)

# Разрешено изменение ширины окна, запрещено изменение высоты
win.resizable(True, False)
win.mainloop()