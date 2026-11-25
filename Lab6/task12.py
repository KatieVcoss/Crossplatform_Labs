from tkinter import *
from tkinter import messagebox

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
class Task12UI:
    def __init__(self):
        self._win = Win("Задание 12: Обратный отсчет", 800, 300, 300, 200, "#f0f0f0")
        self._win.columnconfigure(1, weight=1)
        self._win.rowconfigure(1, weight=1)

        self._time_left = 0
        self._running = False

        # Создание элементов ввода и кнопки запуска
        Label(self._win, text="Диапазон времени в секундах:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self._entry = Entry(self._win, font=("Arial", 12), width=10)
        self._entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self._entry.insert(0, "10")

        self._btn = Button(self._win, text="Обратный отсчет", font=("Arial", 12), command=self._start_countdown)
        self._btn.grid(row=0, column=2, padx=10, pady=10)

        self._canvas = Canvas_(self._win, 480, 200, "white")
        self._canvas.show(0, 1, 1, 1, 10, 10)

    # Метод запуска обратного отсчета с проверкой корректности ввода
    def _start_countdown(self):
        try:
            self._time_left = int(self._entry.get())
            if self._time_left <= 0: raise ValueError
            self._running = True
            self._canvas.delete("all")
            self._tick_down()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое положительное число секунд.")

    # Метод обновления таймера каждую секунду
    def _tick_down(self):
        if self._running and self._time_left >= 0:
            h = self._time_left // 3600
            m = (self._time_left % 3600) // 60
            s = self._time_left % 60
            time_str = f"{h:02d}:{m:02d}:{s:02d}"

            self._canvas.delete("time")
            self._canvas.create_text(240, 100, text=time_str, font=("Arial", 30, "bold"), fill="blue", tags="time")

            # Отображение сигнала по завершении отсчета
            if self._time_left == 0:
                self._running = False
                self._canvas.create_text(240, 150, text="ВРЕМЯ ВЫШЛО!", font=("Arial", 20, "bold"), fill="red", tags="signal")
                self._win.bell()
                return

            self._time_left -= 1
            self._win.after(1000, self._tick_down)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task12UI()
    app.run()