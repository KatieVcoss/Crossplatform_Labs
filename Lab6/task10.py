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
class Task10UI:
    def __init__(self):
        self._win = Win("Задание 10: Катящийся Колобок", 700, 350, 250, 150, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 680
        self._ch = 330
        self._canvas = Canvas_(self._win, self._cw, self._ch, "#FFFACD")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        # Параметры движения и размеры Колобка
        self._R = 40
        self._ground_y = 250
        self._x = 60
        self._y = self._ground_y - self._R
        self._angle = 0
        self._speed = 2

        # Отрисовка травы
        self._canvas.create_rectangle(0, self._ground_y, self._cw, self._ch,
                                       fill="#7CFC00", outline="")
        self._canvas.create_line(0, self._ground_y, self._cw, self._ground_y,
                                  fill="#228B22", width=3)

        # Параметры элементов лица для вращения
        self._features = {
            "left_eye":  {"dx": -8,  "dy": -10, "type": "oval", "size": 4, "color": "black"},
            "right_eye": {"dx":  8,  "dy": -10, "type": "oval", "size": 4, "color": "black"},
            "nose":      {"dx":  0,  "dy":   0, "type": "oval", "size": 5, "color": "orange"},
            "mouth":     {"dx":  0,  "dy":  12, "type": "arc",  "size": 14, "color": "red",
                          "start_local": 190, "extent": 160},
        }

        self._ids = {}
        self._draw()
        self._win.after(30, self._animate)

    # Метод поворота точки вокруг центра
    def _rotate(self, dx, dy, angle):
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        new_dx = dx * cos_a - dy * sin_a
        new_dy = dx * sin_a + dy * cos_a
        return new_dx, new_dy

    # Метод первичной отрисовки всех элементов
    def _draw(self):
        # Отрисовка тела Колобка
        self._ids["body"] = self._canvas.create_oval(
            self._x - self._R, self._y - self._R,
            self._x + self._R, self._y + self._R,
            fill="yellow", outline="orange", width=2)

        # Отрисовка элементов лица с учётом начального поворота
        for name, feat in self._features.items():
            dx, dy = self._rotate(feat["dx"], feat["dy"], self._angle)
            px = self._x + dx
            py = self._y + dy
            s = feat["size"]

            if feat["type"] == "oval":
                self._ids[name] = self._canvas.create_oval(
                    px - s, py - s, px + s, py + s,
                    fill=feat["color"], outline="")
            elif feat["type"] == "arc":
                start_deg = math.degrees(-self._angle) + feat["start_local"]
                self._ids[name] = self._canvas.create_arc(
                    px - s, py - s, px + s, py + s,
                    start=start_deg, extent=feat["extent"],
                    style=ARC, outline=feat["color"], width=2)

    # Метод анимации качения Колобка
    def _animate(self):
        self._x += self._speed
        self._angle += self._speed / self._R

        # Обновление координат тела
        self._canvas.coords(self._ids["body"],
                             self._x - self._R, self._y - self._R,
                             self._x + self._R, self._y + self._R)

        # Обновление координат и параметров элементов лица
        for name, feat in self._features.items():
            dx, dy = self._rotate(feat["dx"], feat["dy"], self._angle)
            px = self._x + dx
            py = self._y + dy
            s = feat["size"]

            if feat["type"] == "oval":
                self._canvas.coords(self._ids[name],
                                     px - s, py - s, px + s, py + s)
            elif feat["type"] == "arc":
                start_deg = math.degrees(-self._angle) + feat["start_local"]
                self._canvas.coords(self._ids[name],
                                     px - s, py - s, px + s, py + s)
                self._canvas.itemconfig(self._ids[name], start=start_deg)

        # Возврат Колобка в начало при выходе за правую границу
        if self._x - self._R > self._cw:
            self._x = -self._R
            self._angle = 0

        self._win.after(30, self._animate)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task10UI()
    app.run()