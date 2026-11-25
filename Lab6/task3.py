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

class Task3UI:
    def __init__(self):
        self._win = Win("Задание 3: Рисование линиями", 600, 500, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._canvas = Canvas_(self._win, 580, 480, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        # Координаты начальной точки рисования
        self._start_point = None

        self._canvas.bind("<Button-3>", self._set_start)
        self._canvas.bind("<Button-1>", self._draw_line)

    # Метод установки начальной точки рисования
    def _set_start(self, event):
        self._start_point = (event.x, event.y)
        # Отрисовка визуальной метки начальной точки
        self._canvas.delete("start_mark")
        self._canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3,
                                  fill="blue", tags="start_mark")

    # Метод рисования линии от предыдущей точки к текущей
    def _draw_line(self, event):
        if self._start_point is None:
            return
        x1, y1 = self._start_point
        x2, y2 = event.x, event.y
        self._canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
        # Новая точка становится стартовой
        self._start_point = (x2, y2)
        self._canvas.delete("start_mark")

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task3UI()
    app.run()