import tkinter as tk
from tkinter import messagebox


class Logic: # Класс бизнес-логики
    @staticmethod
    def check_point(a, b, x, y):
        # Проверка, лежит ли точка (x, y) на прямой y = ax + b
        return y == a * x + b


class TestRunner: # Класс тестирования
    @staticmethod
    def run(test_cases, func):
        results = []
        for i, (args, expected) in enumerate(test_cases, 1):
            try:
                res = func(*args)
                status = "PASS" if res == expected else "FAIL"
                results.append(f"Тест {i}: {status} (ожид. {expected}, пол. {res})")
            except Exception as e:
                results.append(f"Тест {i}: ERROR ({e})")
        messagebox.showinfo("Результаты тестирования", "\n".join(results))


class PointLineUI: # Класс интерфейса
    def __init__(self, root):
        self._root = root
        self._root.title("Задание 1: Точка на прямой")
        self._root.geometry("500x500+300+100")

        # Настройка масштабирования
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)

        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self._root, padx=20, pady=20)
        frame.grid(row=0, column=0, sticky="nsew")
        for i in range(4): frame.columnconfigure(i, weight=1)

        labels = ["Коэф. a:", "Коэф. b:", "Координата x:", "Координата y:"]
        self._entries = []
        for i, text in enumerate(labels):
            tk.Label(frame, text=text, font=("Arial", 15)).grid(row=i, column=0, sticky="w", pady=10)
            entry = tk.Entry(frame, font=("Arial", 15), width=25)
            entry.grid(row=i, column=1, sticky="w", pady=10)
            self._entries.append(entry)

        btn_frame = tk.Frame(self._root)
        btn_frame.grid(row=1, column=0, sticky="nsew")

        tk.Button(btn_frame, text="Проверить", font=("Arial", 15), command=self._check).pack(side="left", expand=True,
                                                                                             padx=15)
        tk.Button(btn_frame, text="Запустить тесты", font=("Arial", 15), command=self._run_tests).pack(side="left",
                                                                                                       expand=True,
                                                                                                       padx=15)

        self._result_lbl = tk.Label(self._root, text="", font=("Arial", 18, "bold"))
        self._result_lbl.grid(row=2, column=0, pady=25)

    def _get_float(self, entry, name):
        try:
            return float(entry.get().replace(",", "."))
        except ValueError:
            raise ValueError(f"Ошибка ввода в поле '{name}'. Введите число.")

    def _check(self):
        try:
            a = self._get_float(self._entries[0], "a")
            b = self._get_float(self._entries[1], "b")
            x = self._get_float(self._entries[2], "x")
            y = self._get_float(self._entries[3], "y")

            is_on_line = Logic.check_point(a, b, x, y)
            msg = "Точка ЛЕЖИТ на прямой" if is_on_line else "Точка НЕ ЛЕЖИТ на прямой"
            self._result_lbl.config(text=msg, fg="green" if is_on_line else "red")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))

    def _run_tests(self):
        # Тесты: (a, b, x, y), ожидаемый результат
        tests = [
            ((2, 3, 1, 5), True),  # y = 2*1 + 3 = 5
            ((2, 3, 1, 6), False),  # y = 2*1 + 3 = 5 != 6
            ((0, 5, 10, 5), True)  # y = 0*10 + 5 = 5
        ]
        TestRunner.run(tests, Logic.check_point)


if __name__ == "__main__":
    root = tk.Tk()
    app = PointLineUI(root)
    root.mainloop()