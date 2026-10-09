from tkinter import *

win = Tk()
win.title("Задание 4")
win.geometry("400x330+500+100")

# Панель с полями ввода координат
controls = Frame(win)
controls.pack(pady=20)

Label(controls, text="X:").grid(row=0,column=0,padx=5)
entry_x=Entry(controls, width=6)
entry_x.grid(row=0,column=1,padx=5)

Label(controls, text="Y:").grid(row=0,column=2,padx=5)
entry_y=Entry(controls, width=6)
entry_y.grid(row=0,column=3,padx=5)

btn_move = Button(controls,text="Переместить")
btn_move.grid(row=0,column=4, padx=10)

# Фрейм для размещения метки
frame = Frame(win, width=380,height=200,bg="white",relief="solid", bd=1)
frame.pack(padx=10,pady=10)
# Запрет фрейму подстраиваться под размеры дочерних виджетов
frame.pack_propagate(False)

msg_lbl = Label(frame,text="Привет!",bg="white")
msg_lbl.place(x=0,y=0)

# Обработчик перемещения метки
def move_lbl(event):
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
    except ValueError:
        return  #если введено не число — меткa на месте
    msg_lbl.place(x=x,y=y)

btn_move.bind("<Button-1>", move_lbl)
win.bind("<Return>", move_lbl)

win.mainloop()