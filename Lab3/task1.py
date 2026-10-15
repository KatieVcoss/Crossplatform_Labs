import os
import tkinter as tk
from PIL import Image, ImageTk

class Window: #Класс, описывающий атрибуты и методы окна приложения
    def __init__(self,title,width,height,x,y,bg_color,img_path):
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.bg_color = bg_color
        self._img_path = img_path
        self._root = None
        self._photo = None

    def build(self,master=None): #Метод создания и настройки экземпляра окна
        if master is None:
            self._root = tk.Tk()
        else:
            self._root = tk.Toplevel(master)

        self._root.title(self.title)
        self._root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self._root.configure(bg=self.bg_color)
        self._root.resizable(False,False)

        # Загрузка изображения
        if os.path.exists(self._img_path):
            img = Image.open(self._img_path)
            # Масштабирование под размер окна
            img=img.resize((self.width-5,self.height-5), Image.Resampling.LANCZOS)

            self._photo = ImageTk.PhotoImage(img) # сохранение ссылки
            lbl = tk.Label(self._root, image=self._photo,bg=self.bg_color)
            lbl.pack(expand=True,fill='both',padx=10,pady=10)
        else:
            lbl = tk.Label(self._root,text=f"{self.title}\n(Изображение не найдено)",
                            bg=self.bg_color, fg="gray", font=("Arial",12))
            lbl.pack(expand=True)

        return self._root

win1 = Window("Окно 1: Рисунок Paint",350,250,100,100,"#f0f8ff", "img1.png")
win2 = Window("Окно 2: Фотография",350,250,480,100,"#fffaf0", "img2.png")
win3 = Window("Окно 3: Скриншот LexQView",350,250,290,380,"#f5f5f5", "img3.png")

# Запуск главного окна
root = win1.build()
# Запуск дочерних окон
win2.build(master=root)
win3.build(master=root)
root.mainloop()