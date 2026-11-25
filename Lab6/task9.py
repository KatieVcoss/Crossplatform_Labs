from tkinter import *

# Классы-обёртки виджетов
class Win(Tk):
    def __init__(self, text, w, h, x, y, bg):
        Tk.__init__(self)
        self.title(text)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self['bg'] = bg

class Canvas_(Canvas):
    def __init__(self, parent, width, height, bg):
        Canvas.__init__(self, parent, width=width, height=height, bg=bg)

    def show(self, column, row, columnspan, rowspan, padx, pady, sticky="nsew"):
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)

# Класс интерфейса
class Task9UI:
    def __init__(self):
        self._win = Win("Задание 9: След на снегу", 400, 600, 300, 50, "#e8f4f8")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 380
        self._ch = 580
        self._canvas = Canvas_(self._win, self._cw, self._ch, "#e8f4f8")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        self._y_pos = self._ch - 30
        self._x_pos = self._cw // 2
        self._step_y = 25
        self._step_x = 30
        self._left_foot = True

        # Набор символов для правого следа
        self._right_foot_lines = [
            "0ооо.",
            "(   )",
            " )  /",
            "(__/"
        ]

        # Набор символов для левого следа (зеркальное отражение)
        self._left_foot_lines = [
            ".ооо0",
            "(   )",
            "\  (",
            " \__)"
        ]

        self._win.after(100, self._draw_foot)

    # Метод построчной отрисовки следа на холсте
    def _draw_foot(self):
        if self._y_pos < 30:
            return

        # Выбор набора символов в зависимости от текущей ноги
        lines = self._left_foot_lines if self._left_foot else self._right_foot_lines
        offset_x = -self._step_x if self._left_foot else self._step_x

        # Отрисовка каждой строки символа со смещением
        for i, line in enumerate(lines):
            self._canvas.create_text(
                self._x_pos + offset_x,
                self._y_pos + i * 15,
                text=line,
                font=("Consolas", 12, "bold"),
                fill="#4a4a4a",
                anchor="center"
            )

        self._y_pos -= self._step_y * 2
        # Переключение на другую ногу для следующего шага
        self._left_foot = not self._left_foot

        self._win.after(400, self._draw_foot)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task9UI()
    app.run()