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

class Task4UI:
    def __init__(self):
        self._win = Win("Задание 4: Перо и линии", 600, 500, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._cw = 580
        self._ch = 480
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)
        self._canvas.focus_set()

        # Шаг перемещения пера в пикселях
        self._step = 10
        self._px = self._cw // 2
        self._py = self._ch // 2

        # Отрисовка начальной точки пера
        self._pen = self._canvas.create_oval(self._px-3, self._py-3,
                                              self._px+3, self._py+3,
                                              fill="blue", tags="pen")

        self._canvas.bind("<Key>", self._on_key)

    def _on_key(self, event):
        old_x, old_y = self._px, self._py

        if event.keysym == "Left":
            self._px -= self._step
        elif event.keysym == "Right":
            self._px += self._step
        elif event.keysym == "Up":
            self._py -= self._step
        elif event.keysym == "Down":
            self._py += self._step

        # Ограничение перемещения границами холста
        self._px = max(0, min(self._cw, self._px))
        self._py = max(0, min(self._ch, self._py))

        # Отрисовка линии от старой точки к новой
        self._canvas.create_line(old_x, old_y, self._px, self._py, fill="blue", width=2)

        # Перемещение визуальной точки пера
        self._canvas.coords(self._pen, self._px-3, self._py-3, self._px+3, self._py+3)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task4UI()
    app.run()