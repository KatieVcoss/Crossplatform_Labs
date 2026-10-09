from tkinter import *

# Создание главного окна и загрузка уменьшенного изображения
win1 = Tk()
pic = PhotoImage(file="pic.png").subsample(5)

# Метка с параметром compound="top" (изображение сверху, текст снизу)
lbl_image1 = Label(win1, image=pic, text="Ежик?", compound="top")
lbl_image1.grid(padx=10, pady=10)

# Создание двух дополнительных окон через Toplevel
win2 = Toplevel(win1)
# Использование параметра compound="bottom" (изображение снизу, текст сверху)
lbl_image2 = Label(win2, image=pic, text="Ежик?", compound="bottom")
lbl_image2.grid(padx=10, pady=10)

win3 = Toplevel(win2)
# Использование параметра compound="left" (изображение слева, текст справа)
lbl_image3 = Label(win3, image=pic, text="Ежик?", compound="left")
lbl_image3.grid(padx=10, pady=10)

# Запуск цикла обработки событий
win1.mainloop()