from tkinter import *

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

    def show(self, column, row, columnspan, rowspan, padx, pady, sticky="nsew"):
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)

# Класс интерфейса
class Task3UI:
    def __init__(self):
        self._win = Win("Задание 3: Поговорка и интерпретация", 650, 720, 300, 50, "#f0ead6")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._proverb = "У семи нянек\nдитё без глазу."
        self._interp_text = ("Мало толку, когда много людей\n"
                             "берётся за одно дело и при этом\n"
                             "каждый надеется на другого.")
        self._info_text = ("Предполагается, что пословица появилась\n"
                           "во времена Семибоярщины, когда из-за\n"
                           "раздоров среди бояр в государстве\n"
                           "наступил хаос.")

        self._cw = 600
        self._ch = 680
        self._canvas = Canvas_(self._win, self._cw, self._ch, "light blue")
        self._canvas.show(0, 0, 1, 1, 20, 20)

        self._win.after(200, self._draw_scene)

    def _draw_scene(self):
        self._canvas.delete("all")
        w = self._cw
        h = self._ch
        cx = w / 2

        # Внешняя рамка холста
        m = 20
        self._canvas.create_line(m, m, w - m, m, fill="#8B4513", width=3)
        self._canvas.create_line(w - m, m, w - m, h - m, fill="#8B4513", width=3)
        self._canvas.create_line(w - m, h - m, m, h - m, fill="#8B4513", width=3)
        self._canvas.create_line(m, h - m, m, m, fill="#8B4513", width=3)

        #  Рамка с текстом поговорки (ВСЕГДА видна)
        pf_t, pf_b, pf_l, pf_r = 50, 160, 120, w - 120
        self._canvas.create_line(pf_l, pf_t, pf_r, pf_t, fill="#2E7D32", width=2)
        self._canvas.create_line(pf_r, pf_t, pf_r, pf_b, fill="#2E7D32", width=2)
        self._canvas.create_line(pf_r, pf_b, pf_l, pf_b, fill="#2E7D32", width=2)
        self._canvas.create_line(pf_l, pf_b, pf_l, pf_t, fill="#2E7D32", width=2)

        self._canvas.create_text(cx, (pf_t + pf_b) / 2,
                                  text=self._proverb,
                                  font=("Arial", 16, "bold"), fill="#2E7D32",
                                  tags="proverb")  # всегда виден

    # Блок "Интерпретация" (виден по умолчанию)

        # Заголовок "Интерпретация"
        iy = 210
        self._canvas.create_text(cx, iy,
                                  text="Интерпретация",
                                  font=("Arial", 15, "bold", "underline"),
                                  fill="#0D47A1", tags="interp_block")
        # Двойные линии под заголовком
        self._canvas.create_line(cx - 100, iy + 18, cx + 100, iy + 18,
                                  fill="#0D47A1", width=2, tags="interp_block")
        self._canvas.create_line(cx - 100, iy + 24, cx + 100, iy + 24,
                                  fill="#0D47A1", width=2, tags="interp_block")
        # Текст интерпретации
        self._canvas.create_text(cx, iy + 90,
                                  text=self._interp_text,
                                  font=("Arial", 12, "italic"), fill="#0D47A1",
                                  tags="interp_block")

        # Рамка со сведениями о поговорке (скрыта по умолчанию)
        sf_t, sf_b, sf_l, sf_r = 190, 430, 100, w - 100
        self._canvas.create_line(sf_l, sf_t, sf_r, sf_t,
                                  fill="#0D47A1", width=2, state="hidden", tags="info_frame")
        self._canvas.create_line(sf_r, sf_t, sf_r, sf_b,
                                  fill="#0D47A1", width=2, state="hidden", tags="info_frame")
        self._canvas.create_line(sf_r, sf_b, sf_l, sf_b,
                                  fill="#0D47A1", width=2, state="hidden", tags="info_frame")
        self._canvas.create_line(sf_l, sf_b, sf_l, sf_t,
                                  fill="#0D47A1", width=2, state="hidden", tags="info_frame")

        self._canvas.create_text(cx, (sf_t + sf_b) / 2,
                                  text=self._info_text,
                                  font=("Arial", 12, "italic"), fill="#0D47A1",
                                  state="hidden", tags="info_text")

        # Элемент "Текст поговорки" (скрыт по умолчанию, для возврата)
        py = 480
        self._canvas.create_text(cx, py,
                                  text="Текст поговорки",
                                  font=("Arial", 14, "bold", "underline"),
                                  fill="#0D47A1", state="hidden", tags="btn_proverb")
        self._canvas.create_line(cx - 100, py + 18, cx + 100, py + 18,
                                  fill="#0D47A1", width=2, state="hidden", tags="btn_proverb")
        self._canvas.create_line(cx - 100, py + 24, cx + 100, py + 24,
                                  fill="#0D47A1", width=2, state="hidden", tags="btn_proverb")

        # Привязка событий
        self._canvas.tag_bind("interp_block", "<Enter>", self._show_info)
        self._canvas.tag_bind("btn_proverb", "<Enter>", self._show_interp)

    def _show_info(self, event=None):
        #Наведение на блок 'Интерпретация' → его сокрытие, показ сведений
        self._canvas.itemconfig("interp_block", state="hidden")
        self._canvas.itemconfig("info_frame", state="normal")
        self._canvas.itemconfig("info_text", state="normal")
        self._canvas.itemconfig("btn_proverb", state="normal")

    def _show_interp(self, event=None):
        #Наведение на 'Текст поговорки' → сокрытие сведений, возврат блока 'Интерпретация'
        self._canvas.itemconfig("info_frame", state="hidden")
        self._canvas.itemconfig("info_text", state="hidden")
        self._canvas.itemconfig("btn_proverb", state="hidden")
        self._canvas.itemconfig("interp_block", state="normal")

    def run(self):
        self._win.mainloop()

if __name__ == "__main__":
    app = Task3UI()
    app.run()