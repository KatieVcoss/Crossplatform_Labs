import tkinter as tk
from tkinter import messagebox
import random


class MemoryGameLogic:
    def __init__(self): # 4 пары букв = 8 карточек
        self._pairs = ['A', 'B', 'C', 'D']
        self._cards = self._pairs * 2
        random.shuffle(self._cards)
        self._matched = [False] * len(self._cards)

    def get_card(self, index):
        return self._cards[index]

    def is_matched(self, index):
        return self._matched[index]

    def check_match(self, idx1, idx2):
        if self._cards[idx1] == self._cards[idx2]:
            self._matched[idx1] = True
            self._matched[idx2] = True
            return True
        return False

    def is_game_over(self):
        return all(self._matched)


class MemoryGameUI:
    def __init__(self, root):
        self._root = root
        self._root.title("Задание 4: Memory")
        self._root.geometry("500x500+300+100")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

        self._logic = MemoryGameLogic()
        self._flipped_cards = []
        self._buttons = []
        self._is_processing = False  # Флаг блокировки при проверке двух карт
        self._build_ui()

    def _build_ui(self):
        self._grid_frame = tk.Frame(self._root)
        self._grid_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Настройка весов для масштабирования
        for i in range(2): self._grid_frame.rowconfigure(i, weight=1)
        for i in range(4): self._grid_frame.columnconfigure(i, weight=1)

        for i in range(8):
            btn = tk.Button(self._grid_frame, text="?", font=("Arial", 24, "bold"),
                            command=lambda idx=i: self._on_card_click(idx))
            btn.grid(row=i // 4, column=i % 4, sticky="nsew", padx=5, pady=5)
            self._buttons.append(btn)

        btn_frame = tk.Frame(self._root)
        btn_frame.grid(row=1, column=0, sticky="nsew")
        tk.Button(btn_frame, text="Новая игра", font=("Arial", 12), command=self._restart).pack(expand=True, pady=10)

    def _on_card_click(self, index):
        # Исключение возможности переверачивания 3-й карточки
        if self._is_processing or len(self._flipped_cards) >= 2:
            return

        # Если карта уже угадана или уже открыта
        if self._logic.is_matched(index) or index in self._flipped_cards:
            return

        # Переворот карты
        self._buttons[index].config(text=self._logic.get_card(index), state="disabled")
        self._flipped_cards.append(index)

        # Если открыты 2 карты, проверка на совпадение
        if len(self._flipped_cards) == 2:
            self._is_processing = True
            idx1, idx2 = self._flipped_cards

            if self._logic.check_match(idx1, idx2):
                self._buttons[idx1].config(bg="#a5d6a7")  # Зеленый
                self._buttons[idx2].config(bg="#a5d6a7")
                self._flipped_cards = []
                self._is_processing = False
                if self._logic.is_game_over():
                    messagebox.showinfo("Победа", "Вы нашли все пары!")
            else:
                # Возврат карты через 1 секунду
                self._root.after(1000, self._flip_back, idx1, idx2)

    def _flip_back(self, idx1, idx2):
        self._buttons[idx1].config(text="?", state="normal")
        self._buttons[idx2].config(text="?", state="normal")
        self._flipped_cards = []
        self._is_processing = False

    def _restart(self):
        self._logic = MemoryGameLogic()
        self._flipped_cards = []
        self._is_processing = False
        for btn in self._buttons:
            btn.config(text="?", state="normal", bg="SystemButtonFace")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGameUI(root)
    root.mainloop()