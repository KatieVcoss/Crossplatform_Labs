from tkinter import *
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
class Task8UI:
    def __init__(self):
        self._win = Win("Задание 8: Спираль", 600, 600, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 580
        self._ch = 580
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        self._cx = self._cw // 2
        self._cy = self._ch // 2
        self._max_r = min(self._cx, self._cy) - 10

        # Этап 1: создание объекта незамкнутой окружности (дуги)
        self._arc_extent = 0
        self._arc_max = 330
        self._arc_id = self._canvas.create_arc(
            self._cx - self._max_r, self._cy - self._max_r,
            self._cx + self._max_r, self._cy + self._max_r,
            start=0, extent=0, style=ARC,
            outline="#1565C0", width=3
        )

        # Этап 2: параметры для отрисовки спирали
        self._t = 0
        self._prev_x = None
        self._prev_y = None
        self._k = 0.13

        self._win.after(100, self._draw_arc)

    # Метод анимации отрисовки незамкнутой окружности
    def _draw_arc(self):
        if self._arc_extent < self._arc_max:
            self._arc_extent += 3
            if self._arc_extent > self._arc_max:
                self._arc_extent = self._arc_max
            self._canvas.itemconfig(self._arc_id, extent=self._arc_extent)
            self._win.after(20, self._draw_arc)
        else:
            self._init_spiral()

    # Метод инициализации начальной точки спирали от конца дуги
    def _init_spiral(self):
        start_angle_rad = math.radians(self._arc_max)
        x0 = self._cx + self._max_r * math.cos(start_angle_rad)
        y0 = self._cy - self._max_r * math.sin(start_angle_rad)

        self._prev_x = x0
        self._prev_y = y0
        self._t = self._arc_max

        self._win.after(50, self._draw_spiral)

    # Метод анимации отрисовки спирали к центру холста
    def _draw_spiral(self):
        r = self._max_r - self._k * (self._t - self._arc_max)

        # Остановка при достижении центра
        if r <= 0:
            return

        angle_rad = math.radians(self._t)
        x = self._cx + r * math.cos(angle_rad)
        y = self._cy - r * math.sin(angle_rad)

        # Отрисовка отрезка от предыдущей точки к текущей
        self._canvas.create_line(self._prev_x, self._prev_y, x, y,
                                  fill="#1565C0", width=3)

        self._prev_x = x
        self._prev_y = y
        self._t += 2

        self._win.after(20, self._draw_spiral)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task8UI()
    app.run()