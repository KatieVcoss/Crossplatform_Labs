from tkinter import *
from tkinter import messagebox
import math

# Классы-обертки виджетов
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

class Label_(Label):
    def __init__(self, parent, text, font, bg, column, row, columnspan=1, rowspan=1, sticky="w"):
        Label.__init__(self, parent, text=text, font=font, bg=bg)
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan, sticky=sticky)

class Button_(Button):
    def __init__(self, parent, text, fg, bg, width, height, column, row, padx=5, pady=5):
        Button.__init__(self, parent, text=text, fg=fg, bg=bg,
                        width=width, height=height)
        self.grid(column=column, row=row, padx=padx, pady=pady)

    def commandB(self, fun):
        self['command'] = fun

# Класс бизнес-логики
class GraphLogic:
    @staticmethod
    def calculate(x):
        #f(x) = sqrt(|x|) * (x-2)^2 / ((x+1)*(x-4)^3)
        if abs(x + 1) < 1e-9 or abs(x - 4) < 1e-9:
            return None
        try:
            num = math.sqrt(abs(x)) * (x - 2)**2
            den = (x + 1) * (x - 4)**3
            return num / den
        except (ValueError, ZeroDivisionError):
            return None

# Класс интерфейса
class Task2UI:
    def __init__(self):
        self._win = Win("Построение эскиза графика", 700, 600, 250, 80, "#fafafa")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(2, weight=1)
        self._build_ui()

    def _build_ui(self):
        # Описание функции
        desc = ("Функция: f(x) = √|x| · (x-2)² / ((x+1)·(x-4)³)\n"
                "Вертикальные асимптоты: x = -1, x = 4\n"
                "Область определения: x ∈ ℝ \\ {-1; 4}")
        Label_(self._win, desc, ("Arial", 11), "#fafafa", 0, 0, sticky="w")

        # Кнопка
        self._btn = Button_(self._win, "Построить график", "white", "#2196F3",
                            18, 1, 0, 1, padx=10, pady=5)
        self._btn.commandB(self._draw_graph)

        # Холст
        self._canvas = Canvas_(self._win, 650, 450, "white")
        self._canvas.show(0, 2, 1, 1, 10, 10)

        # Отрисовка системы координат сразу
        self._win.after(100, self._draw_axes)

    def _draw_axes(self):
        self._canvas.delete("all")
        w = self._canvas.winfo_width()
        h = self._canvas.winfo_height()
        cx, cy = w // 2, h // 2
        self._scale = 35

        # Оси со стрелками
        self._canvas.create_line(0, cy, w - 5, cy, fill="black", arrow="last", width=2)
        self._canvas.create_line(cx, h - 5, cx, 5, fill="black", arrow="last", width=2)

        # Подписи осей
        self._canvas.create_text(w - 15, cy - 15, text="X", font=("Arial", 11, "bold"))
        self._canvas.create_text(cx + 15, 15, text="Y", font=("Arial", 11, "bold"))

        # Начало координат
        self._canvas.create_text(cx - 15, cy + 15, text="O", font=("Arial", 10))

        # Единичные отрезки
        for i in range(-8, 9):
            if i == 0:
                continue
            px = cx + i * self._scale
            self._canvas.create_line(px, cy - 3, px, cy + 3, fill="black")
            self._canvas.create_text(px, cy + 15, text=str(i), font=("Arial", 8))

        for i in range(-5, 6):
            if i == 0:
                continue
            py = cy - i * self._scale
            self._canvas.create_line(cx - 3, py, cx + 3, py, fill="black")
            self._canvas.create_text(cx - 15, py, text=str(i), font=("Arial", 8))

    def _draw_graph(self):
        self._draw_axes()
        w = self._canvas.winfo_width()
        h = self._canvas.winfo_height()
        cx, cy = w // 2, h // 2

        # Асимптоты пунктиром
        for x_asym in [-1, 4]:
            px = cx + x_asym * self._scale
            self._canvas.create_line(px, 0, px, h, fill="red", dash=(5, 3), width=1)
            self._canvas.create_text(px + 5, 15, text=f"x={x_asym}",
                                      fill="red", anchor="nw", font=("Arial", 9, "bold"))

        # Название функции
        self._canvas.create_text(10, 10, text="f(x) = √|x|·(x-2)² / ((x+1)·(x-4)³)",
                                  anchor="nw", font=("Arial", 11, "italic"), fill="blue")

        # Построение графика с адаптивным шагом вблизи асимптот
        points = []
        x_min, x_max = -10, 10

        x = x_min
        while x <= x_max:
            y = GraphLogic.calculate(x)
            if y is not None and abs(y) < 30:
                px = cx + x * self._scale
                py = cy - y * self._scale
                points.append((px, py))
            else:
                if len(points) > 1:
                    self._canvas.create_line(points, fill="green", width=2)
                points = []

            # Адаптивный шаг: уменьшение вблизи асимптот
            if abs(x - (-1)) < 0.5 or abs(x - 4) < 0.5:
                x += 0.01
            else:
                x += 0.05

        if len(points) > 1:
            self._canvas.create_line(points, fill="green", width=2)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task2UI()
    app.run()