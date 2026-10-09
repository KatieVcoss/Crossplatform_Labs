from tkinter import *

def task_3():
    win = Toplevel(root)
    win.geometry("300x150+500+100")
    # Список цветов
    colors = ["red","orange","green","blue","purple","black"]
    # Индекс хранится в списке, для его изменения внутри вложенной функции
    color_index = [0]

    button = Button(win, text="Press", font=("Arial",14))
    button.pack(expand=True,pady=30)
    #Фокус на кнопке для Enter
    button.focus_set()

    # Общий обработчик для клика и нажатия Enter
    def change_color(event):
        color_index[0] = (color_index[0]+1)%len(colors)
        button.config(fg=colors[color_index[0]])

    # Привязка функции к двум разным событиям
    button.bind("<Button-1>",change_color)
    button.bind("<Return>",change_color)

def task_3_1():
    win = Toplevel(root)
    win.title("Задание 3.1")
    win.geometry("300x150+500+100")

    messages = ["сообщение номер 1", "другое сообщение"]
    # Ссылкa на окно храниncz в списке, для её изменения внутри обработчиков
    message_win = [None]

    btn_get = Button(win, text="Получить сообщение")
    btn_next = Button(win, text="Следующее сообщение", state="disabled")

    # Общая функция открытия окна с сообщением
    def show_msg(text):
        if message_win[0] is not None:
            message_win[0].destroy()
        m = Toplevel(win)
        m.geometry("250x90+550+200")
        Label(m,text=text, justify="center").pack(expand=True)
        message_win[0] = m

    def on_get_msg(event):
        show_msg(messages[0])
        btn_get.config(state="disabled")
        btn_next.config(state="normal")

    def on_next_msg(event):
        show_msg(messages[1])
        btn_next.config(state="disabled")

    btn_get.bind("<Button-1>",on_get_msg)
    btn_get.pack(pady=10)
    btn_next.bind("<Button-1>",on_next_msg)
    btn_next.pack(pady=10)

def task_3_2():
    win = Toplevel(root)
    win.title("Задание 3.2")
    win.geometry("300x150+500+200")

    frame = Frame(win)
    frame.pack(expand=True, padx=20, pady=20)

    entry1 = Entry(frame,width=25)
    entry1.pack(pady=10)
    entry2 = Entry(frame,width=25)
    entry2.pack(pady=10)

    # Обработчик: через event.widget определяется, какое поле получило фокус
    def focus(event):
        event.widget.config(bg="white")

    def unfocus(event):
        event.widget.config(bg="grey")

    entry1.bind("<FocusIn>",focus)
    entry1.bind("<FocusOut>",unfocus)
    entry2.bind("<FocusIn>",focus)
    entry2.bind("<FocusOut>",unfocus)

    entry2.config(bg="grey")
    entry1.focus_set()

def task_3_3():
    win = Toplevel(root)
    win.title("Задание 3.3")
    win.geometry("300x250+500+200")

    frame = Frame(win)
    frame.pack(expand=True, padx=20, pady=20)

    entry1=Entry(frame, width=25)
    entry1.pack(pady=5)
    entry2=Entry(frame, width=25)
    entry2.pack(pady=5)

    def focus(event):
        event.widget.config(bg="white")

    def unfocus(event):
        event.widget.config(bg="grey")

    entry1.bind("<FocusIn>",focus)
    entry1.bind("<FocusOut>",unfocus)
    entry2.bind("<FocusIn>", focus)
    entry2.bind("<FocusOut>", unfocus)

    entry2.config(bg="grey")
    entry1.focus_set()

    Label(frame, text="Введённые значения:").pack(pady=(15,5))

    lb1 = Label(frame,text="")
    lb1.pack()
    lb2 = Label(frame,text="")
    lb2.pack()

    btn_get = Button(frame, text="Получить")
    btn_get.pack(pady=(15,5))
    btn_clear = Button(frame, text="Очистить")
    btn_clear.pack(pady=5)

    # Обработчик кнопки "Получить": считывание значений и блокировка кнопки
    def on_get(event):
        lb1.config(text=entry1.get())
        lb2.config(text=entry2.get())
        btn_get.config(state="disabled")

    # Обработчик кнопки "Очистить": очистка полей и активирование "Получить"
    def on_clear(event):
        entry1.delete(0,END)
        entry2.delete(0,END)
        lb1.config(text="")
        lb2.config(text="")
        btn_get.config(state="normal")

    btn_get.bind("<Button-1>",on_get)
    btn_get.bind("<Return>",on_get)
    btn_clear.bind("<Button-1>",on_clear)
    btn_clear.bind("<Return>",on_clear)

# Главное меню
root = Tk()
root.title("Главное меню")

btn_3 = Button(root,  text="Задание 3", command=task_3)
btn_3.pack(pady=5)
btn_3_1 = Button(root, text="Задание 3.1", command=task_3_1)
btn_3_1.pack(pady=5)
btn_3_2 = Button(root, text="Задание 3.2", command=task_3_2)
btn_3_2.pack(pady=5)
btn_3_3 = Button(root, text="Задание 3.3", command=task_3_3)
btn_3_3.pack(pady=5)

root.mainloop()