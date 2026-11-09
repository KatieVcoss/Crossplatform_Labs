from tkinter import *
from tkinter import messagebox

# Классы-обертки виджетов
class Win(Tk):
    def __init__(self, text, w, h, x, y, bg):
        Tk.__init__(self)
        self.title(text)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self['bg'] = bg

class Canvas_(Canvas):
    def __init__(self, parent, width, height, bg):
        Canvas.__init__(self, parent, width=width, height=height, bg=bg)
        self.canv = self  # сам объект является холстом

    def show(self, column, row, columnspan, rowspan, padx, pady, sticky="nsew"):
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)

class Label_(Label):
    def __init__(self, parent, text, font, bg, column, row, columnspan=1, rowspan=1, sticky="w"):
        Label.__init__(self, parent, text=text, font=font, bg=bg)
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan, sticky=sticky)

class Entry_(Entry):
    def __init__(self, parent, width, font, fg, relief, justify, column, row):
        Entry.__init__(self, parent, width=width, font=font, fg=fg,
                       relief=relief, justify=justify)
        self.grid(column=column, row=row)
        self.var = StringVar()
        self['textvariable'] = self.var

class Button_(Button):
    def __init__(self, parent, text, fg, bg, width, height, column, row, padx=5, pady=5):
        Button.__init__(self, parent, text=text, fg=fg, bg=bg,
                        width=width, height=height)
        self.grid(column=column, row=row, padx=padx, pady=pady)

    def commandB(self, fun):
        self['command'] = fun

# Класс бизнес-логики
class FunctionLogic:
    @staticmethod
    def calculate(x):
        #Кусочно-заданная функция: f(x) = x^4-16 при |x|>=2, x^3/(2x+1) при -2<=x<=2
        if abs(x) >= 2:
            return x**4 - 16
        elif -2 <= x <= 2:
            if abs(2*x + 1) < 1e-9:
                return None  # точка разрыва x = -0.5
            return (x**3) / (2*x + 1)
        return None

# Класс тестирования
class TestRunner:
    @staticmethod
    def run(test_cases, func):
        results = []
        for i, (args, expected) in enumerate(test_cases, 1):
            try:
                res = func(*args)
                if expected is None:
                    status = "PASS" if res is None else "FAIL"
                else:
                    status = "PASS" if abs(res - expected) < 0.001 else "FAIL"
                results.append(f"Тест {i}: {status} (ожид. {expected}, пол. {res})")
            except Exception as e:
                results.append(f"Тест {i}: ERROR ({e})")
        messagebox.showinfo("Результаты тестирования", "\n".join(results))

# Класс интерфейса
class Task1UI:
    def __init__(self):
        self._win = Win("Задание 1: Значения функции на холсте", 700, 550, 300, 100, "#f5f5f5")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(1, weight=1)
        self._build_ui()

    def _build_ui(self):
        # Панель ввода
        ctrl = Frame(self._win, bg="#f5f5f5", padx=10, pady=10)
        ctrl.grid(row=0, column=0, sticky="ew")

        Label_(ctrl, "a:", ("Arial", 12, "bold"), "#f5f5f5", 0, 0)
        self._e_a = Entry_(ctrl, 6, ("Arial", 12), "black", "solid", "center", 1, 0)
        self._e_a.var.set("-3")

        Label_(ctrl, "b:", ("Arial", 12, "bold"), "#f5f5f5", 2, 0)
        self._e_b = Entry_(ctrl, 6, ("Arial", 12), "black", "solid", "center", 3, 0)
        self._e_b.var.set("3")

        Label_(ctrl, "h:", ("Arial", 12, "bold"), "#f5f5f5", 4, 0)
        self._e_h = Entry_(ctrl, 6, ("Arial", 12), "black", "solid", "center", 5, 0)
        self._e_h.var.set("0.5")

        self._btn_calc = Button_(ctrl, "Рассчитать", "white", "#2196F3", 12, 1, 6, 0)
        self._btn_calc.commandB(self._calculate)

        self._btn_test = Button_(ctrl, "Тесты", "white", "#4CAF50", 8, 1, 7, 0)
        self._btn_test.commandB(self._run_tests)

        # Холст и скроллбар
        self._canvas = Canvas_(self._win, 500, 400, "white")
        self._canvas.show(0, 1, 1, 1, 10, 10)

        self._scroll = Scrollbar(self._win, orient="vertical", command=self._canvas.yview)
        self._scroll.grid(row=1, column=1, sticky="ns", pady=10)
        self._canvas.configure(yscrollcommand=self._scroll.set)

    def _calculate(self):
        try:
            a = float(self._e_a.var.get().replace(",", "."))
            b = float(self._e_b.var.get().replace(",", "."))
            h = float(self._e_h.var.get().replace(",", "."))
            if h <= 0:
                raise ValueError("Шаг должен быть > 0")
            if a > b:
                raise ValueError("a должно быть <= b")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", f"Некорректные данные: {e}")
            return

        self._canvas.delete("all")
        y_pos = 15
        # Заголовок таблицы
        self._canvas.create_text(10, y_pos, anchor="nw",
                                  text=f"{'x':<12}{'f(x)':<12}{'':<12}| {'x':<12}{'f(x)':<12}{'':<12}| {'x':<12}{'f(x)':<12}",
                                  font=("Arial", 10, "bold"), fill="blue")
        y_pos += 20
        self._canvas.create_line(10, y_pos, 700, y_pos, fill="blue")
        y_pos += 15

        # Сбор всех значений
        values = []
        x = a
        while x <= b + 1e-9:
            val = FunctionLogic.calculate(x)
            values.append((x, val))
            x += h

        # Вывод по три значения в ряд
        row_idx = 0
        col_idx = 0
        for x_val, f_val in values:
            x_off = 10 + col_idx * 230
            if f_val is None:
                text = f"x={x_val:<6.2f} | undef"
            else:
                text = f"x={x_val:<6.2f} | {f_val:<8.2f}"
            self._canvas.create_text(x_off, y_pos + row_idx * 22, anchor="nw",
                                      text=text, font=("Arial", 10))
            col_idx += 1
            if col_idx == 3:
                col_idx = 0
                row_idx += 1

        total_height = y_pos + (row_idx + 1) * 22 + 20
        self._canvas.configure(scrollregion=(0, 0, 720, total_height))

    def _run_tests(self):
        tests = [
            ((-3,), 65.0),      # (-3)^4 - 16 = 81 - 16 = 65
            ((0,), 0.0),        # 0^3/(0+1) = 0
            ((3,), 65.0),       # 3^4 - 16 = 65
            ((-0.5,), None),    # точка разрыва
            ((1,), 1/3)         # 1^3/(2+1) = 1/3
        ]
        TestRunner.run(tests, FunctionLogic.calculate)

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task1UI()
    app.run()