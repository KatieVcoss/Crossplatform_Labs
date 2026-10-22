import tkinter as tk
from tkinter import messagebox
import random


class GuessLogic:
    def __init__(self):
        self._target = self.generate_new()

    def generate_new(self):
        self._target = random.randint(100, 999)
        return self._target

    def compare(self, user_val):
        if not (100 <= user_val <= 999):
            raise ValueError("Число должно быть в диапазоне 100...999")

        if user_val == self._target:
            return "Угадано!"
        elif user_val > self._target:
            return "Ваше число БОЛЬШЕ загаданного"
        else:
            return "Ваше число МЕНЬШЕ загаданного"


class TestRunner:
    @staticmethod
    def run(test_cases, func):
        results = []
        for i, (args, expected) in enumerate(test_cases, 1):
            try:
                res = func(*args)
                status = "PASS" if res == expected else "FAIL"
                results.append(f"Тест {i}: {status} (ожид. '{expected}', пол. '{res}')")
            except Exception as e:
                results.append(f"Тест {i}: ERROR ({e})")
        messagebox.showinfo("Результаты тестирования", "\n".join(results))


class GuessUI:
    def __init__(self, root):
        self._root = root
        self._root.title("Задание 3: Угадай число")
        self._root.geometry("500x500+300+100")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)

        self._logic = GuessLogic()
        self._build_ui()

    def _build_ui(self):
        frame = tk.Frame(self._root, padx=20, pady=20)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(1, weight=1)

        tk.Label(frame, text=f"Загадано число (100-999):", font=("Arial", 15)).grid(row=0, column=0, sticky="w",
                                                                                    pady=20)
        self._target_lbl = tk.Label(frame, text="", font=("Arial", 15, "bold"), fg="gray")
        self._target_lbl.grid(row=0, column=1, sticky="w", pady=20)

        tk.Label(frame, text="Ваше число:", font=("Arial", 15)).grid(row=1, column=0, sticky="w", pady=20)
        self._entry = tk.Entry(frame, font=("Arial", 15), width=15)
        self._entry.grid(row=1, column=1, sticky="w", pady=20)

        btn_frame = tk.Frame(self._root)
        btn_frame.grid(row=1, column=0, sticky="nsew")

        tk.Button(btn_frame, text="Сравнить", font=("Arial", 15), command=self._compare).pack(side="left", expand=True,
                                                                                              padx=10)
        tk.Button(btn_frame, text="Новая игра", font=("Arial", 15), command=self._new_game).pack(side="left",
                                                                                                 expand=True, padx=0)
        tk.Button(btn_frame, text="Тесты", font=("Arial", 15), command=self._run_tests).pack(side="left", expand=True,
                                                                                             padx=10)

        self._result_lbl = tk.Label(self._root, text="", font=("Arial", 18, "bold"))
        self._result_lbl.grid(row=2, column=0, pady=25)

    def _compare(self):
        try:
            val = int(self._entry.get())
            result = self._logic.compare(val)
            self._result_lbl.config(text=result, fg="blue")
            if "Угадано" in result:
                self._result_lbl.config(fg="green")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def _new_game(self):
        self._logic.generate_new()
        self._entry.delete(0, tk.END)
        self._result_lbl.config(text="Новое число сгенерировано!", fg="black")

    def _run_tests(self):
        # Для теста замена target на 500
        self._logic._target = 500
        tests = [
            ((500,), "Угадано!"),
            ((600,), "Ваше число БОЛЬШЕ загаданного"),
            ((400,), "Ваше число МЕНЬШЕ загаданного")
        ]
        TestRunner.run(tests, self._logic.compare)


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessUI(root)
    root.mainloop()