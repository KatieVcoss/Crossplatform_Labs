from tkinter import *

win = Tk()
win.title("Задание 5")
win.geometry("300x260+100+100")

frame = Frame(win)
frame.pack(padx=20, pady=20)

entries = {}

# Вспомогательная функция создания поля ввода
def add_field(row, label_text, default_value):
    Label(frame, text=label_text).grid(row=row, column=0, sticky="w", pady=5)
    entry = Entry(frame, width=18, bg="lightgrey")
    entry.insert(0, default_value)
    entry.grid(row=row, column=1, pady=5)
    entries[label_text] = entry
    return entry

# Четыре поля ввода
entry_name = add_field(0, "Имя:", "")
entry_font = add_field(1, "Шрифт (family):", "Arial")
entry_style = add_field(2, "Начертание:", "normal")
entry_size = add_field(3, "Размер:", "14")

# Обработчики смены цвета фона при фокусе
def on_focus_in(event):
    event.widget.config(bg="white")

def on_focus_out(event):
    event.widget.config(bg="lightgrey")

for entry in entries.values():
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

btn_output = Button(frame, text="Вывод")
btn_change = Button(frame, text="Изменить", state="disabled")
btn_output.grid(row=4, column=0, pady=15)
btn_change.grid(row=4, column=1, pady=15)

# Ссылка на окно приветствия хранится в списке
greeting_win = [None]

# Функция сборки параметров шрифта в кортеж
def build_font():
    try:
        size = int(entry_size.get())
    except ValueError:
        size = 14
    family = entry_font.get() or "Arial"
    style = entry_style.get() or "normal"
    return (family, size, style)

# Функция показа приветствия
def show_greeting(event):
    if greeting_win[0] is not None:
        greeting_win[0].destroy()
    g = Toplevel(win)
    g.title("Приветствие")
    g.geometry("300x120+450+100")
    name = entry_name.get() or "гость"
    Label(g, text=f"Приветствую, {name}!", font=build_font(),
          justify="center").pack(expand=True, padx=10, pady=10)
    greeting_win[0] = g

# Обработчик кнопки "Вывод"
def on_output(event):
    show_greeting(event)
    btn_output.config(state="disabled")
    btn_change.config(state="normal")

# Обработчик кнопки "Изменить"
def on_change(event):
    show_greeting(event)

btn_output.bind("<Button-1>", on_output)
btn_change.bind("<Button-1>", on_change)

win.mainloop()