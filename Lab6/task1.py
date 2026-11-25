from tkinter import *
import math


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
class Task1UI:
    def __init__(self):
        self._win = Win("Задание 1: Фигуры и тексты", 700, 500, 300, 100, "#f0f0f0")
        self._win.columnconfigure(0, weight=1)
        self._win.rowconfigure(0, weight=1)

        self._canvas = Canvas_(self._win, 680, 480, "white")
        self._canvas.show(0, 0, 1, 1, 10, 10)

        # Словарь для хранения информации о фигурах
        self._shapes = {}
        # Словарь для хранения информации о текстах
        self._texts = {}

        self._win.after(100, self._draw_scene)

    def _draw_scene(self):
        self._canvas.delete("all")

        # Создание исходных фигур

        # Создание овала
        self._canvas.create_oval(50, 50, 200, 150, fill="green", outline="black", width=2, tags="oval")
        self._shapes["oval"] = {"type": "oval", "coords": (50, 50, 200, 150), "color": "green", "name": "овал"}

        # Создание прямоугольника
        self._canvas.create_rectangle(250, 50, 400, 150, fill="blue", outline="black", width=2, tags="rect")
        self._shapes["rect"] = {"type": "rect", "coords": (250, 50, 400, 150), "color": "blue", "name": "прямоугольник"}

        # Создание треугольника
        self._canvas.create_polygon(450, 50, 620, 150, 450, 150, fill="red", outline="black", width=2, tags="tri")
        self._shapes["tri"] = {"type": "tri", "coords": (450, 50, 620, 150, 450, 150), "color": "red",
                               "name": "треугольник"}

        # Создание исходных текстовых меток

        # Текст для создания шестиугольника при клике ПКМ
        self._canvas.create_text(125, 280, text="шестиугольник", font=("Arial", 13, "bold"), fill="black",
                                 tags="txt_hex")
        self._texts["txt_hex"] = {"x": 125, "y": 280, "name": "ШЕСТИУГОЛЬНИК", "shape_type": "hex"}

        # Текст для создания круга при клике ПКМ
        self._canvas.create_text(325, 280, text="круг", font=("Arial", 13, "bold"), fill="black", tags="txt_circle")
        self._texts["txt_circle"] = {"x": 325, "y": 280, "name": "круг", "shape_type": "circle"}

        # Текст для создания сектора при клике ПКМ
        self._canvas.create_text(500, 280, text="сектор", font=("Arial", 13, "bold"), fill="black", tags="txt_sector")
        self._texts["txt_sector"] = {"x": 500, "y": 280, "name": "сектор", "shape_type": "sector"}

        # Привязка событий мыши к объектам

        # Замена фигуры текстом при клике ЛКМ
        for tag in self._shapes:
            self._canvas.tag_bind(tag, "<Button-1>", lambda e, t=tag: self._shape_to_text(t))

        # Замена текста фигурой при клике ПКМ
        for tag in self._texts:
            self._canvas.tag_bind(tag, "<Button-3>", lambda e, t=tag: self._text_to_shape(t))

    # Метод замены фигуры текстом с её названием
    def _shape_to_text(self, shape_tag):
        shape = self._shapes[shape_tag]
        coords = shape["coords"]
        cx = (coords[0] + coords[2]) / 2
        cy = (coords[1] + coords[3]) / 2

        # Удаление фигуры с холста
        self._canvas.delete(shape_tag)

        # Создание текста с названием фигуры
        text_tag = f"text_{shape_tag}"
        self._canvas.create_text(cx, cy, text=shape["name"],
                                 font=("Arial", 14, "bold"), fill=shape["color"],
                                 tags=text_tag)
        self._texts[text_tag] = {"x": cx, "y": cy, "name": shape["name"], "shape_type": shape["type"]}

        # Привязка события ПКМ для возврата фигуры
        self._canvas.tag_bind(text_tag, "<Button-3>", lambda e, t=text_tag: self._text_to_shape(t))

        del self._shapes[shape_tag]

    # Метод замены текста фигурой
    def _text_to_shape(self, text_tag):
        txt = self._texts[text_tag]
        x, y = txt["x"], txt["y"]
        shape_type = txt["shape_type"]

        # Удаление текста с холста
        self._canvas.delete(text_tag)

        # Отрисовка фигуры в зависимости от её типа
        if shape_type == "oval":
            # Отрисовка овала
            tag = "oval"
            self._canvas.create_oval(x - 75, y - 50, x + 75, y + 50, fill="green", outline="black", width=2, tags=tag)
            self._shapes[tag] = {"type": "oval", "coords": (x - 75, y - 50, x + 75, y + 50), "color": "green",
                                 "name": "овал"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        elif shape_type == "rect":
            # Отрисовка прямоугольника
            tag = "rect"
            self._canvas.create_rectangle(x - 75, y - 50, x + 75, y + 50, fill="blue", outline="black", width=2,
                                          tags=tag)
            self._shapes[tag] = {"type": "rect", "coords": (x - 75, y - 50, x + 75, y + 50), "color": "blue",
                                 "name": "прямоугольник"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        elif shape_type == "tri":
            # Отрисовка треугольника
            tag = "tri"
            self._canvas.create_polygon(x - 60, y - 50, x + 60, y - 50, x, y + 50, fill="red", outline="black", width=2,
                                        tags=tag)
            self._shapes[tag] = {"type": "tri", "coords": (x - 60, y - 50, x + 60, y - 50, x, y + 50), "color": "red",
                                 "name": "треугольник"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        elif shape_type == "hex":
            # Отрисовка шестиугольника
            tag = "hex"
            r = 60
            points = []
            for i in range(6):
                angle = math.pi / 3 * i - math.pi / 6
                px = x + r * math.cos(angle)
                py = y + r * math.sin(angle)
                points.extend([px, py])
            self._canvas.create_polygon(points, fill="purple", outline="black", width=2, tags=tag)
            self._shapes[tag] = {"type": "hex", "coords": tuple(points), "color": "purple", "name": "шестиугольник"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        elif shape_type == "circle":
            # Отрисовка круга
            tag = "circle"
            r = 55
            self._canvas.create_oval(x - r, y - r, x + r, y + r, fill="orange", outline="black", width=2, tags=tag)
            self._shapes[tag] = {"type": "circle", "coords": (x - r, y - r, x + r, y + r), "color": "orange",
                                 "name": "круг"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        elif shape_type == "sector":
            # Отрисовка сектора
            tag = "sector"
            r = 60
            self._canvas.create_arc(x - r, y - r, x + r, y + r,
                                    start=0, extent=90,
                                    style="pieslice",
                                    fill="cyan", outline="black", width=2, tags=tag)
            self._shapes[tag] = {"type": "sector", "coords": (x - r, y - r, x + r, y + r), "color": "cyan",
                                 "name": "сектор"}
            self._canvas.tag_bind(tag, "<Button-1>", lambda e: self._shape_to_text(tag))

        del self._texts[text_tag]

    def run(self):
        self._win.mainloop()


if __name__ == "__main__":
    app = Task1UI()
    app.run()