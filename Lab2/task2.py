from tkinter import *

#Главное окно
root = Tk()
root.withdraw()

#Информационное окно
info_win=Toplevel(root)
info_win.title("Информационное окно")
info_win.geometry("320x200+300+200")

label=Label(info_win, text="Переместите мышь во втором окне\n или щёлкните левой/правой кнопкой", justify="center")
label.pack(expand=True)

#Окно для перемещения мыши
event_win=Toplevel(root)
event_win.title("Окно для перемещения мыши")
event_win.geometry("320x200+630+200")

#обработчики событий мыши
def mouse_move(event):
    label.config(text=f"Координаты мыши в окне: x={event.x} y={event.y}")
def l_click(event):
    label.config(text=f"Нажата лкм: x={event.x} y={event.y}")
def r_click(event):
    label.config(text=f"Нажата пкм: x={event.x} y={event.y}")

#Привязка событий
event_win.bind("<Motion>",mouse_move)
event_win.bind("<Button-1>",l_click)
event_win.bind("<Button-3>",r_click)

root.mainloop()