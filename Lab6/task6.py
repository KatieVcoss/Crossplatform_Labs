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
class Task6UI:
    def __init__(self):
        self._win = Win("Задание 6: Движение круга к точке клика", 600, 500, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 580
        self._ch = 480
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        self._R = 30
        self._cx = self._cw // 2
        self._cy = self._ch // 2
        self._target_x = self._cx
        self._target_y = self._cy
        self._moving = False

        # Создание круга на холсте
        self._circle = self._canvas.create_oval(self._cx - self._R, self._cy - self._R,
                                                  self._cx + self._R, self._cy + self._R,
                                                  fill="orange", outline="black", width=2)

        self._canvas.bind("<Button-1>", self._on_click)

    # Метод обработки клика мыши для установки цели
    def _on_click(self, event):
        self._target_x = event.x
        self._target_y = event.y
        if not self._moving:
            self._moving = True
            self._animate()

    # Метод анимации плавного перемещения круга
    def _animate(self):
        dx = self._target_x - self._cx
        dy = self._target_y - self._cy
        # Вычисление расстояния до цели
        dist = math.hypot(dx, dy)

        # Остановка анимации при достижении цели
        if dist < 2:
            self._moving = False
            return

        speed = 3
        # Нормализация вектора движения и применение скорости
        self._cx += dx / dist * speed
        self._cy += dy / dist * speed

        # Обновление координат круга на холсте
        self._canvas.coords(self._circle,
                             self._cx - self._R, self._cy - self._R,
                             self._cx + self._R, self._cy + self._R)
        self._win.after(20, self._animate)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task6UI()
    app.run()