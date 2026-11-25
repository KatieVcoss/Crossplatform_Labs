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

class Button_(Button):
    def __init__(self, parent, text, fg, bg, width, height, column, row, padx=5, pady=5):
        Button.__init__(self, parent, text=text, fg=fg, bg=bg,
                        width=width, height=height)
        self.grid(column=column, row=row, padx=padx, pady=pady)

    def commandB(self, fun):
        self['command'] = fun

# Класс интерфейса
class Task5UI:
    def __init__(self):
        self._win = Win("Задание 5: Бегущая строка", 600, 300, 300, 200, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(1, weight=1)

        # Текст бегущей строки
        self._message = "Соблюдайте режим сна — это залог здоровья и продуктивности! "
        self._running = False
        self._x_pos = 0
        self._text_id = None
        self._after_id = None

        self._build_ui()

    def _build_ui(self):
        # Создание панели с кнопками управления
        btn_frame = Frame(self._win, bg="#f0f0f0", padx=10, pady=10)
        btn_frame.grid(row=0, column=0, sticky="ew")

        self._btn_start = Button_(btn_frame, "Старт", "white", "#4CAF50", 10, 1, 0, 0)
        self._btn_start.commandB(self._start)

        self._btn_stop = Button_(btn_frame, "Стоп", "white", "#f44336", 10, 1, 1, 0)
        self._btn_stop.commandB(self._stop)

        # Создание внешнего холста
        self._cw = 580
        self._ch = 150
        self._canvas = Canvas_(self._win, self._cw, self._ch, "white")
        self._canvas.show(0, 1, 1, 1, 10, 10)

        # Параметры внутренней рамки для обрезки текста
        self._frame_left = 20
        self._frame_top = 40
        self._frame_right = self._cw - 20
        self._frame_bottom = self._ch - 40
        self._frame_w = self._frame_right - self._frame_left
        self._frame_h = self._frame_bottom - self._frame_top

        # Отрисовка рамки на внешнем холсте
        self._canvas.create_rectangle(self._frame_left, self._frame_top,
                                       self._frame_right, self._frame_bottom,
                                       outline="black", width=2, fill="white")

        # Создание вложенного холста для автоматической обрезки выходящего текста
        self._inner = Canvas(self._canvas, width=self._frame_w, height=self._frame_h,
                             bg="white", highlightthickness=0, bd=0)
        self._canvas.create_window(self._frame_left + self._frame_w // 2,
                                    self._frame_top + self._frame_h // 2,
                                    window=self._inner)

    # Метод запуска анимации бегущей строки
    def _start(self):
        if not self._running:
            self._running = True
            if self._text_id is None:
                self._text_id = self._inner.create_text(self._inner.winfo_width(),
                                                         self._inner.winfo_height() // 2,
                                                         text=self._message,
                                                         font=("Arial", 14, "bold"),
                                                         fill="blue", anchor="w")
                self._x_pos = self._inner.winfo_width()
            self._animate()

    # Метод остановки анимации
    def _stop(self):
        self._running = False
        if self._after_id is not None:
            self._win.after_cancel(self._after_id)
            self._after_id = None

    # Метод циклического перемещения текста
    def _animate(self):
        if not self._running:
            return
        self._x_pos -= 2
        # Возврат текста за правую границу при полном выходе за левую
        if self._x_pos < -self._inner.bbox(self._text_id)[2]:
            self._x_pos = self._inner.winfo_width()
        self._inner.coords(self._text_id, self._x_pos, self._inner.winfo_height() // 2)
        self._after_id = self._win.after(30, self._animate)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task5UI()
    app.run()