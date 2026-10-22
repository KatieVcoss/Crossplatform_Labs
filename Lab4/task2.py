import tkinter as tk
from tkinter import messagebox


class LinearEqLogic:
    @staticmethod
    def solve(a, b): # Функция для решения уравнение ax + b = 0
        if a != 0:
            return f"x = {-b / a:.4f}"
        elif b == 0:
            return "Бесконечно много решений (0 = 0)"
        else:
            return "Решений нет"


class TestRunner:
    @staticmethod
    def run(test_cases, func):
        results = []
        for i, (args, expected) in enumerate(test_cases, 1):
            try:
                res = func(*args)
                status = "PASS" if res == expected else "FAIL"
                results.append(f"Тест {i}: {status}\nОжидалось: {expected}\nПолучено: {res}")
            except Exception as e:
                results.append(f"Тест {i}: ERROR ({e})")
        messagebox.showinfo("Результаты тестирования", "\n\n".join(results))


class LinearEqUI:
    def __init__(self, root):
        self._root = root
        self._root.title("Задание 2: Линейное уравнение")
        self._root.geometry("500x500+300+100")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self._root, padx=30, pady=30)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        tk.Label(frame, text="Коэффициент a:", font=("Arial", 15)).grid(row=0, column=0, sticky="w", pady=15)
        self._entry_a = tk.Entry(frame, font=("Arial", 15), width=15)
        self._entry_a.grid(row=0, column=1, sticky="w", pady=15)

        tk.Label(frame, text="Коэффициент b:", font=("Arial", 15)).grid(row=1, column=0, sticky="w", pady=15)
        self._entry_b = tk.Entry(frame, font=("Arial", 15), width=15)
        self._entry_b.grid(row=1, column=1, sticky="w", pady=15)

        btn_frame = tk.Frame(self._root)
        btn_frame.grid(row=1, column=0, sticky="nsew")

        tk.Button(btn_frame, text="Решить", font=("Arial", 15), command=self._solve).pack(side="left", expand=True,
                                                                                          padx=20)
        tk.Button(btn_frame, text="Тесты", font=("Arial", 15), command=self._run_tests).pack(side="left", expand=True,
                                                                                             padx=20)

        self._result_lbl = tk.Label(self._root, text="", font=("Arial", 18, "bold"), wraplength=450)
        self._result_lbl.grid(row=2, column=0, pady=30)

    def _solve(self):
        try:
            a = float(self._entry_a.get().replace(",", "."))
            b = float(self._entry_b.get().replace(",", "."))
            result = LinearEqLogic.solve(a, b)
            self._result_lbl.config(text=result, fg="blue")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа для коэффициентов.")

    def _run_tests(self):
        tests = [
            ((2, -4), "x = 2.0000"),
            ((0, 0), "Бесконечно много решений (0 = 0)"),
            ((0, 5), "Решений нет")
        ]
        TestRunner.run(tests, LinearEqLogic.solve)


if __name__ == "__main__":
    root = tk.Tk()
    app = LinearEqUI(root)
    root.mainloop()