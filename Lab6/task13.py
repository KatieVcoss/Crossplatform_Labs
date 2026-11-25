from tkinter import *
from tkinter import messagebox
import math

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
class Task13UI:
    def __init__(self):
        self._win = Win("Задание 13: Циклоида", 800, 400, 300, 100, "#f0f0f0")
        self._win.columnconfigure(1, weight=1)
        self._win.rowconfigure(1, weight=1)

        self._t = 0
        self._prev_px = None
        self._prev_py = None
        self._drawing = False

        # Создание элементов ввода параметра и кнопки запуска
        Label(self._win, text="Параметр a:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self._entry = Entry(self._win, font=("Arial", 12), width=10)
        self._entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self._entry.insert(0, "20")

        self._btn = Button(self._win, text="Циклоида", font=("Arial", 12), command=self._start_draw)
        self._btn.grid(row=0, column=2, padx=10, pady=10)

        self._canvas = Canvas_(self._win, 580, 320, "white")
        self._canvas.show(0, 1, 1, 1, 10, 10)

        # Отрисовка осей координат
        self._canvas.create_line(20, 280, 560, 280, fill="black", arrow="last")
        self._canvas.create_line(20, 280, 20, 20, fill="black", arrow="last")
        self._canvas.create_text(570, 280, text="X", font=("Arial", 12))
        self._canvas.create_text(20, 10, text="Y", font=("Arial", 12))

    # Метод запуска анимации построения кривой
    def _start_draw(self):
        try:
            self._a = float(self._entry.get().replace(",", "."))
            if self._a <= 0: raise ValueError
            self._canvas.delete("curve")
            self._t = 0
            self._prev_px = None
            self._prev_py = None
            self._drawing = True
            self._draw_step()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите положительное число для параметра a.")

    # Метод пошаговой отрисовки циклоиды
    def _draw_step(self):
        if not self._drawing:
            return

        # Вычисление координат по параметрическим уравнениям
        x = self._a * (self._t - math.sin(self._t))
        y = self._a * (1 - math.cos(self._t))

        # Масштабирование координат для холста
        scale = 5
        px = 20 + x * scale
        py = 280 - y * scale

        # Остановка при выходе за правую границу холста
        if px > 560:
            self._drawing = False
            return

        # Отрисовка отрезка от предыдущей точки к текущей
        if self._prev_px is not None:
            self._canvas.create_line(self._prev_px, self._prev_py, px, py, fill="blue", width=2, tags="curve")

        self._prev_px = px
        self._prev_py = py
        self._t += 0.1

        self._win.after(20, self._draw_step)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task13UI()
    app.run()