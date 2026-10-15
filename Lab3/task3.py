import tkinter as tk

# Цвета для состояний ячеек
DEFAULT_COLOR = "black"
BRIGHT_COLOR = "#d32f2f"  # Ярко-красный (верный ответ)
DIM_COLOR = "#b0b0b0"  # Серый (неверный)


class LetterCell: #Класс ячейки таблицы с буквой
    def __init__(self, master, row, col, letter, correct_col, on_click_callback):
        self.master = master
        self.row = row
        self.col = col
        self.letter = letter
        self.correct_col = correct_col  # Индекс столбца с правильным автором
        self.on_click = on_click_callback
        self._label = None

    def build(self, grid_row, grid_col): #Создание фрейма и метки с буквой
        frame = tk.Frame(self.master, width=90, height=45, bd=1, relief="solid")
        frame.grid(row=grid_row, column=grid_col, sticky="nsew")
        frame.grid_propagate(False)  # Запрет фрейму менять размер под содержимое

        self._label = tk.Label(frame, text=self.letter, font=("Arial", 14, "bold"),
                               fg=DEFAULT_COLOR, bg="white")
        self._label.place(relx=0.5, rely=0.5, anchor="center")

        # Привязка клика к фрейму и метке
        self._label.bind("<Button-1>", lambda e: self.on_click(self.row, self.col))
        frame.bind("<Button-1>", lambda e: self.on_click(self.row, self.col))
        return frame

    def set_color(self, color): #Метод изменения цвета буквы
        if self._label:
            self._label.configure(fg=color)


class AnswerField: #Класс поля ввода для проверки ключевого слова

    def __init__(self, master, keyword):
        self.master = master
        self.keyword = keyword.upper()
        self.var = tk.StringVar()
        self._entry = None

    def build(self, x, y):
        tk.Label(self.master, text="Ответ:", font=("Arial", 12, "bold")).place(x=x, y=y)
        self._entry = tk.Entry(self.master, textvariable=self.var, font=("Arial", 12), width=20)
        self._entry.place(x=x + 70, y=y)

        # Отслеживание изменения текста в реальном времени
        self.var.trace_add("write", self._check_answer)
        return self._entry

    def _check_answer(self, *args): #Проверка введенного слова и смена цвета фона
        text = self.var.get().strip().upper()
        if not text:
            self._entry.configure(bg="SystemButtonFace")
        elif text == self.keyword:
            self._entry.configure(bg="#a5d6a7")  # Светло-зеленый
        else:
            self._entry.configure(bg="#ef9a9a")  # Светло-красный

    def clear(self): #Очистка поля и сброс цвета
        self.var.set("")
        self._entry.configure(bg="SystemButtonFace")


# Данные для таблицы
AUTHORS = ["А.С. Пушкин", "М.Ю. Лермонтов", "Н.В. Гоголь", "И.С. Тургенев", "Ф.М. Достоевский", "Л.Н. Толстой"]
# Книги и буквы для составления слова "ОБЪЕКТ"
ROWS_DATA = [
    {"title": '"Руслан и Людмила"', "letters": ["О", "М", "Н", "Х", "Б", "Д"], "correct_col": 0},
    {"title": '"Маскарад"', "letters": ["П", "Б", "В", "К", "Е", "Т"], "correct_col": 1},
    {"title": '"Вий"', "letters": ["У", "Ц", "Ъ", "А", "Р", "О"], "correct_col": 2},
    {"title": '"Ася"', "letters": ["Е", "Ж", "З", "Е", "И", "П"], "correct_col": 3},
    {"title": '"Бедные люди"', "letters": ["К", "Л", "Ф", "С", "К", "А"], "correct_col": 4},
    {"title": '"Детство"', "letters": ["Т", "Ю", "Я", "В", "М", "Т"], "correct_col": 5}
]
KEYWORD = "".join(ROWS_DATA[r]["letters"][ROWS_DATA[r]["correct_col"]] for r in range(len(ROWS_DATA)))


def main():
    root = tk.Tk()
    root.title("Задание 3: Таблица фреймов")
    root.geometry("780x550+200+100")
    root.resizable(False, False)

    table_frame = tk.Frame(root)
    table_frame.place(x=20, y=20)

    # Пустой верхний левый угол
    tk.Frame(table_frame, width=220, height=50, bd=1, relief="solid").grid(row=0, column=0, sticky="nsew")

    # Заголовки столбцов (Авторы) - центрированы
    for c, author in enumerate(AUTHORS):
        f = tk.Frame(table_frame, width=90, height=50, bd=1, relief="solid")
        f.grid(row=0, column=c + 1, sticky="nsew")
        f.grid_propagate(False)
        tk.Label(f, text=author, font=("Arial", 9, "bold"), wraplength=85, justify="center").place(relx=0.5, rely=0.5,
                                                                                                   anchor="center")

    cells_matrix = []  # Двумерный список для хранения экземпляров LetterCell

    def handle_cell_click(row, col): #Обработчик клика по ячейке
        cell = cells_matrix[row][col]
        if col == ROWS_DATA[row]["correct_col"]:
            cell.set_color(BRIGHT_COLOR)
        else:
            cell.set_color(DIM_COLOR)

    # Строки таблицы
    for r, row_data in enumerate(ROWS_DATA):
        # Заголовок строки (Книга) - по левому краю, без переносов
        title_f = tk.Frame(table_frame, width=220, height=45, bd=1, relief="solid")
        title_f.grid(row=r + 1, column=0, sticky="nsew")
        title_f.grid_propagate(False)
        tk.Label(title_f, text=row_data["title"], font=("Arial", 10), anchor="w", justify="left", wraplength=0).place(
            x=10, rely=0.5, anchor="w")

        row_cells = []
        for c, letter in enumerate(row_data["letters"]):
            cell = LetterCell(table_frame, r, c, letter, row_data["correct_col"], handle_cell_click)
            cell.build(grid_row=r + 1, grid_col=c + 1)
            row_cells.append(cell)
        cells_matrix.append(row_cells)

    # Поле ответа
    answer_field = AnswerField(root, KEYWORD)
    answer_field.build(x=40, y=450)

    # Кнопка Очистить
    def clear_all():
        answer_field.clear()
        for row_cells in cells_matrix:
            for cell in row_cells:
                cell.set_color(DEFAULT_COLOR)

    tk.Button(root, text="Очистить", font=("Arial", 11), command=clear_all).place(x=320, y=446)

    root.mainloop()


if __name__ == "__main__":
    main()