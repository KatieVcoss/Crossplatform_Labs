from tkinter import *

win = Tk()
win.title("Атрибуты текстовых шрифтов")
win.geometry("300x230+100+100")

# Главное меню
Button(win, text="Семейство (family)", width=25,
       command=lambda: open_family()).pack(pady=5)
Button(win, text="Насыщенность (series)", width=25,
       command=lambda: open_series()).pack(pady=5)
Button(win, text="Начертание (shape)", width=25,
       command=lambda: open_shape()).pack(pady=5)
Button(win, text="Размер (size)", width=25,
       command=lambda: open_size()).pack(pady=5)


# Окно "Семейство шрифтов"
def open_family():
    fam_win = Toplevel(win)
    fam_win.title("Семейства шрифтов")
    fam_win.geometry("300x160+420+100")

    # Список дочерних окон для совместного закрытия
    child_windows = []

    def show_family(title, font_family):
        child = Toplevel(fam_win)
        child.title(title)
        child.geometry("380x160+550+100")
        samples = [
            ("Обычное начертание", "normal"),
            ("Курсивное начертание", "italic"),
            ("Полужирное начертание", "bold")
        ]
        for caption, weight_or_slant in samples:
            Label(child, text=f"{caption}: {font_family}",
                  font=(font_family, 13, weight_or_slant)).pack(pady=5)
        child_windows.append(child)

    Button(fam_win, text="Шрифты с засечками",
           command=lambda: show_family("Шрифты с засечками", "Times New Roman")).pack(pady=5)
    Button(fam_win, text="Шрифты без засечек",
           command=lambda: show_family("Шрифты без засечек", "Arial")).pack(pady=5)
    Button(fam_win, text='Шрифты типа "пишущая машинка"',
           command=lambda: show_family('Шрифты типа "пишущая машинка"', "Courier New")).pack(pady=5)

    # Закрытие окна и всех его потомков по Alt+q
    def close_family(event=None):
        for child in child_windows:
            child.destroy()
        fam_win.destroy()

    fam_win.bind("<Alt-q>", close_family)


#Окно "Насыщенность"
def open_series():
    series_win = Toplevel(win)
    series_win.title("Ширина и жирность шрифтов")
    series_win.geometry("300x220+420+320")

    Label(series_win, text="Введите название шрифта:").pack(pady=5)
    entry_family = Entry(series_win, width=20)
    entry_family.insert(0, "Arial")
    entry_family.pack(pady=5)

    label_medium = Label(series_win, text="Средняя")
    label_bold = Label(series_win, text="Полужирная")
    label_medium.pack(pady=10)
    label_bold.pack(pady=10)

    #Обновление шрифта
    def update_series(event=None):
        family = entry_family.get() or "Arial"
        label_medium.config(font=(family, 14, "normal"))
        label_bold.config(font=(family, 14, "bold"))

    entry_family.bind("<Return>", update_series)
    Button(series_win, text="Применить", command=update_series).pack(pady=5)
    update_series()  # начальное отображение

    # Закрытие окна на Alt+w
    series_win.bind("<Alt-w>", lambda e: series_win.destroy())


#Окно "Начертание"
def open_shape():
    shape_win = Toplevel(win)
    shape_win.title("Начертания шрифтов")
    shape_win.geometry("320x230+420+560")

    Label(shape_win, text="Прямое: Arial", font=("Arial", 14, "roman")).pack(pady=6)
    Label(shape_win, text="Курсивное: Arial", font=("Arial", 14, "italic")).pack(pady=6)
    Label(shape_win, text="Наклонное: Arial", font=("Arial", 14, "italic")).pack(pady=6)
    Label(shape_win, text="'Капитель': ARIAL", font=("Arial", 12, "normal")).pack(pady=6)

    # Закрытие окна на Alt+e
    shape_win.bind("<Alt-e>", lambda e: shape_win.destroy())


#Окно "Размер"
def open_size():
    size_win = Toplevel(win)
    size_win.title("Размер шрифтов")
    size_win.geometry("320x230+420+400")

    Label(size_win, text="Размер шрифта:").pack(pady=5)
    entry_size = Entry(size_win, width=10)
    entry_size.insert(0, "14")
    entry_size.pack(pady=5)

    Label(size_win, text="Введите строку:").pack(pady=5)
    entry_text = Entry(size_win, width=25)
    entry_text.pack(pady=5)

    result_label = Label(size_win, text="")
    result_label.pack(pady=15)

    # Обновление текста с заданным размером шрифта
    def update_text(event=None):
        try:
            size = int(entry_size.get())
        except ValueError:
            size = 14
        result_label.config(text=entry_text.get(), font=("Arial", size))

    entry_text.bind("<Return>", update_text)

    # Закрытие окна на Alt+r
    size_win.bind("<Alt-r>", lambda e: size_win.destroy())

win.mainloop()