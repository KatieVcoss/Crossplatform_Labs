from tkinter import*

# Создание главного окна и настройка его начальной геометрии
win=Tk()
win.geometry("120x140+600+100")

# Создание фреймов: задаем ширину, высоту, цвет и стиль рамки (raised - выпуклость)
fr_red=Frame(win,borderwidth=2,width=120,height=20,background="red",relief="raised")
fr_red.grid()

# Остальные фреймы размещаем в том же столбце, но в разных строках
fr_orange=Frame(win,borderwidth=2,width=120,height=20,background="orange",relief="raised")
fr_orange.grid(column=0,row=1,columnspan=1,rowspan=1)

fr_yellow=Frame(win,borderwidth=2,width=120,height=20,background="yellow",relief="raised")
fr_yellow.grid(column=0,row=2,columnspan=1,rowspan=1)

fr_green=Frame(win,borderwidth=2,width=120,height=20,background="lime",relief="raised")
fr_green.grid(column=0,row=3,columnspan=1,rowspan=1)

fr_lightblue=Frame(win,borderwidth=2,width=120,height=20,background="#007dff",relief="raised")
fr_lightblue.grid(column=0,row=4,columnspan=1,rowspan=1)

fr_blue=Frame(win,borderwidth=2,width=120,height=20,background="blue",relief="raised")
fr_blue.grid(column=0,row=5,columnspan=1,rowspan=1)

fr_purple=Frame(win,borderwidth=2,width=120,height=20,background="#7d00ff",relief="raised")
fr_purple.grid(column=0,row=6,columnspan=1,rowspan=1)

# Запрет изменения размеров окна по обеим осям
win.resizable(False,False)
win.mainloop()