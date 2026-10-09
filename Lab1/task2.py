from tkinter import*

win = Tk()

win.geometry("310x145+400+150")
# Настройка веса столбца окна (weight=1) для горизонтального растяжения
win.columnconfigure(0,weight=1)

colors=["red","orange","yellow","lime","#007dff","blue","#7d00ff"]
labels=["красный","оранжевый","жёлтый","зелёный","голубой","синий","фиолетовый"]

for i in range(7):

    # Настройка веса строк окна для вертикального растяжения
    win.rowconfigure(i,weight=1)
    frame=Frame(win,borderwidth=1,relief="raised")

    # Размещение фрейма с заполнением всей ячейки (sticky="nsew")
    frame.grid(column=0,row=i,sticky="nsew")

    # Настройка внутреннего grid фрейма, чтобы метка могла растягиваться
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure(0,weight=1)
    lbl = Label(frame,text=labels[i], background=colors[i],relief="raised")

    # Растягивание метки на всю площадь фрейма
    lbl.grid(sticky="nsew")
win.mainloop()