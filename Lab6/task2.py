from tkinter import *

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

class Task2UI:
    def __init__(self):
        self._win = Win("Задание 2: Фигура Г", 600, 500, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 580
        self._ch = 480
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)
        self._canvas.focus_set()

        # Размер клетки фигуры
        self._cell = 40
        # Флаг достижения нижней границы холста
        self._at_bottom = False

        # Начальные координаты и угол поворота фигуры
        self._x = 100
        self._y = 50
        self._rotation = 0

        self._win.after(100, self._draw_shape)
        self._canvas.bind("<Key>", self._on_key)

    def _draw_shape(self):
        self._canvas.delete("shape")
        color = "orange" if not self._at_bottom else "red"

        # Отрисовка фигуры из клеток
        cells = self._get_cells()
        for (cx, cy) in cells:
            px = self._x + cx * self._cell
            py = self._y + cy * self._cell
            self._canvas.create_rectangle(px, py, px + self._cell, py + self._cell,
                                           fill=color, outline="black", width=2, tags="shape")

    # Метод получения координат клеток фигуры с учётом поворота
    def _get_cells(self):
        # Базовая форма фигуры
        base = [(0, 0), (1, 0), (2, 0), (0, 1)]

        cells = []
        for (x, y) in base:
            if self._rotation == 0:
                cells.append((x, y))
            elif self._rotation == 90:
                cells.append((y, 2 - x))
            elif self._rotation == 180:
                cells.append((2 - x, 2 - y))
            elif self._rotation == 270:
                cells.append((2 - y, x))
        return cells

    def _on_key(self, event):
        # Блокировка движения после достижения нижней границы
        if self._at_bottom and event.keysym != "Up":
            return

        step = self._cell
        old_x, old_y = self._x, self._y

        if event.keysym == "Down":
            self._y += step
        elif event.keysym == "Up":
            if not self._at_bottom:
                self._rotation = (self._rotation + 90) % 360
        elif event.keysym == "Left":
            if not self._at_bottom:
                self._x -= step
        elif event.keysym == "Right":
            if not self._at_bottom:
                self._x += step

        # Проверка выхода за границы холста
        cells = self._get_cells()
        max_x = max(c[0] for c in cells) * self._cell + self._x + self._cell
        max_y = max(c[1] for c in cells) * self._cell + self._y + self._cell

        if max_x > self._cw or max_y > self._ch or self._x < 0 or self._y < 0:
            self._x, self._y = old_x, old_y
            if event.keysym == "Up" and not self._at_bottom:
                self._rotation = (self._rotation - 90) % 360

        # Проверка достижения нижней границы холста
        if max_y >= self._ch:
            self._at_bottom = True
            self._y = self._ch - max(c[1] for c in self._get_cells()) * self._cell - self._cell

        self._draw_shape()

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task2UI()
    app.run()