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
class Task7UI:
    def __init__(self):
        self._win = Win("Задание 7: Олимпийские кольца", 700, 500, 250, 80, "#fafafa")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 680
        self._ch = 480
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        self._R = 65
        self._LW = 8
        self._STEP = 5
        self._DELAY = 20

        # Словарь цветов колец
        self._colors = {
            'blue': '#0085C7',
            'black': '#000000',
            'red': '#DF0024',
            'yellow': '#F4C300',
            'green': '#009F3D',
        }

        # Словарь координат центров колец
        self._centers = {
            'blue': (180, 150),
            'black': (320, 150),
            'red': (460, 150),
            'yellow': (250, 220),
            'green': (390, 220),
        }

        self._order = ['blue', 'black', 'red', 'yellow', 'green']
        self._ring_items = {}
        self._progress = {name: 0 for name in self._centers}
        self._current = 0

        self._win.after(300, self._animate)

    # Метод создания дуги кольца
    def _draw_ring(self, name):
        cx, cy = self._centers[name]
        self._ring_items[name] = self._canvas.create_arc(
            cx - self._R, cy - self._R, cx + self._R, cy + self._R,
            start=90, extent=0.1, style=ARC,
            outline=self._colors[name], width=self._LW
        )

    # Метод вычисления точек пересечения двух окружностей
    def _get_intersections(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        d = math.hypot(x2 - x1, y2 - y1)
        if d > 2 * self._R:
            return []
        a = d / 2
        h = math.sqrt(self._R ** 2 - a ** 2)
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2
        p1x = xm + h * (y2 - y1) / d
        p1y = ym - h * (x2 - x1) / d
        p2x = xm - h * (y2 - y1) / d
        p2y = ym + h * (x2 - x1) / d
        return [(p1x, p1y), (p2x, p2y)]

    # Метод отрисовки дуги поверх пересечения для эффекта зацепления
    def _patch(self, top_ring, below_ring, position):
        c_top = self._centers[top_ring]
        c_below = self._centers[below_ring]
        pts = self._get_intersections(c_top, c_below)
        if len(pts) != 2:
            return
        pts.sort(key=lambda p: p[1])
        pt = pts[0] if position == 'upper' else pts[1]
        cx, cy = c_top
        px, py = pt
        angle = math.degrees(math.atan2(-(py - cy), px - cx))
        self._canvas.create_arc(
            cx - self._R, cy - self._R, cx + self._R, cy + self._R,
            start=angle - 10, extent=17, style=ARC,
            outline=self._colors[top_ring], width=self._LW
        )

    # Метод применения эффекта переплетения ко всем кольцам
    def _draw_interlacing(self):
        self._patch('blue', 'yellow', 'upper')
        self._patch('yellow', 'blue', 'lower')
        self._patch('yellow', 'black', 'upper')
        self._patch('black', 'yellow', 'lower')
        self._patch('green', 'black', 'upper')
        self._patch('black', 'green', 'lower')
        self._patch('red', 'green', 'upper')
        self._patch('green', 'red', 'lower')

    # Метод анимации последовательной отрисовки колец
    def _animate(self):
        if self._current >= len(self._order):
            self._draw_interlacing()
            return

        name = self._order[self._current]
        if self._progress[name] == 0:
            self._draw_ring(name)

        self._progress[name] += self._STEP
        if self._progress[name] < 360:
            self._canvas.itemconfig(self._ring_items[name], extent=self._progress[name])
            self._win.after(self._DELAY, self._animate)
        else:
            self._canvas.itemconfig(self._ring_items[name], extent=359.9)
            self._current += 1
            if self._current < len(self._order):
                self._progress[self._order[self._current]] = 0
            self._win.after(250, self._animate)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task7UI()
    app.run()