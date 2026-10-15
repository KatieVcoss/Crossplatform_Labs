import tkinter as tk

class Window:
    def __init__(self,title,width,height,x,y,bg_color): #Класс главного окна приложения
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.bg_color = bg_color
        self._root = None

    def build(self):
        self._root = tk.Tk()
        self._root.title(self.title)
        self._root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self._root.configure(bg=self.bg_color)
        self._root.resizable(False,False)
        return self._root

class InputField: #Класс, описывающий поле ввода с подписью и единицей измерения
    def __init__(self,master,label_text,unit_text,x,y):
        self.master = master
        self.label_text = label_text
        self.unit_text = unit_text
        self.x = x
        self.y = y

        self.var = tk.StringVar()
        self._entry = None

    def build(self): #Создание графических элементов поля ввода
        tk.Label(self.master,text=self.label_text, font=("Arial", 12, "bold"),
                 bg=self.master.cget("bg")).place(x=self.x, y=self.y)
        self._entry = tk.Entry(self.master, textvariable=self.var, font=("Arial", 14),
                               width=12, justify="center")
        self._entry.place(x=self.x, y=self.y + 30)
        tk.Label(self.master, text=self.unit_text, font=("Arial", 10),
                 bg=self.master.cget("bg"), fg="gray").place(x=self.x, y=self.y + 65)

        return self._entry

    def bind_event(self, event_name, callback): #Метод для привязки событий к полю ввода
        self._entry.bind(event_name, callback)

def main():
    app_win = Window("Конвертер температур", 500, 500, 300, 100, "#e6f2ff")
    root = app_win.build()

    tk.Label(root, text="Автоматический конвертер", font=("Arial", 16, "bold"),
             bg=app_win.bg_color).place(x=120, y=50)

    # Создание экземпляров полей ввода
    field_c = InputField(root, "Температура", "°C (Цельсий)", 80, 180)
    field_f = InputField(root, "Температура", "°F (Фаренгейт)", 280, 180)

    entry_c = field_c.build()
    entry_f = field_f.build()

    # Флаг для предотвращения зацикливания при взаимном обновлении полей
    _is_updating = {"flag": False}

    def c_to_f(event=None):
        if _is_updating["flag"]: return
        _is_updating["flag"] = True
        try:
            c_val = float(field_c.var.get().replace(",", "."))
            f_val = round(c_val * 1.8 + 32, 2)
            field_f.var.set(str(f_val))
        except ValueError:
            field_f.var.set("")
        _is_updating["flag"] = False

    def f_to_c(event=None):
        if _is_updating["flag"]: return
        _is_updating["flag"] = True
        try:
            f_val = float(field_f.var.get().replace(",", "."))
            c_val = round((f_val - 32) / 1.8, 2)
            field_c.var.set(str(c_val))
        except ValueError:
            field_c.var.set("")
        _is_updating["flag"] = False

    # Привязка события отпускания клавиши
    field_c.bind_event("<KeyRelease>", c_to_f)
    field_f.bind_event("<KeyRelease>", f_to_c)

    root.mainloop()

if __name__=="__main__":
    main()