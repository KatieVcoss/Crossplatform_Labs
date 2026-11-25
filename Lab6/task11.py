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
class Task11UI:
    def __init__(self):
        self._win = Win("Задание 11: Секундомер", 400, 300, 300, 200, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(1, weight=1)

        self._time = 0
        self._running = False

        # Создание панели с кнопками управления
        btn_frame = Frame(self._win, bg="#f0f0f0", pady=10)
        btn_frame.grid(row=0, column=0, sticky="ew")

        self._btn_start = Button(btn_frame, text="Секундомер", font=("Arial", 12), command=self._start)
        self._btn_start.pack(side="left", expand=True, padx=20)
        self._btn_stop = Button(btn_frame, text="Стоп", font=("Arial", 12), command=self._stop)
        self._btn_stop.pack(side="left", expand=True, padx=20)

        self._canvas = Canvas_(self._win, 380, 200, "white")
        self._canvas.show(0, 1, 1, 1, 10, 10)

        self._update_display()

    # Метод запуска отсчета времени
    def _start(self):
        if not self._running:
            self._running = True
            self._tick()

    # Метод остановки отсчета
    def _stop(self):
        self._running = False

    # Метод обновления времени каждую секунду
    def _tick(self):
        if self._running:
            self._time += 1
            self._update_display()
            self._win.after(1000, self._tick)

    # Метод форматирования и отображения времени на холсте
    def _update_display(self):
        h = self._time // 3600
        m = (self._time % 3600) // 60
        s = self._time % 60
        time_str = f"{h:02d}:{m:02d}:{s:02d}"

        self._canvas.delete("time")
        self._canvas.create_text(190, 100, text=time_str, font=("Arial", 30, "bold"), fill="blue", tags="time")

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task11UI()
    app.run()