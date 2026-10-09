from tkinter import *

win = Tk()
win.geometry("350x145+600+150")

# Настройка сетки 3х3: углы фиксированы (weight=0), центр растягивается (weight=1)
win.columnconfigure(0, weight=0); win.columnconfigure(1, weight=1); win.columnconfigure(2, weight=0)
win.rowconfigure(0, weight=0); win.rowconfigure(1, weight=1); win.rowconfigure(2, weight=0)

# Создание четырех угловых фреймов с внешними отступами (padx)
fr_tl = Frame(win, borderwidth=10, relief="raised", bg="lime", width=50, height=50)
fr_tl.grid(row=0, column=0, padx=(50, 0))
fr_tr = Frame(win, borderwidth=10, relief="raised", bg="lime", width=50, height=50)
fr_tr.grid(row=0, column=2, padx=(0, 50))

fr_dl = Frame(win, borderwidth=10, relief="raised", bg="lime", width=50, height=50)
fr_dl.grid(row=2, column=0, padx=(50, 0))
fr_dr = Frame(win, borderwidth=10, relief="raised", bg="lime", width=50, height=50)
fr_dr.grid(row=2, column=2, padx=(0, 50))

# Центральная метка с параметром activebackground (цвет при наведении)
mid_lbl = Label(win, borderwidth=10, relief="raised", bg="lime", activebackground="blue", height=2)
mid_lbl.grid(row=1, column=1, sticky="nsew")

# Привязка событий мыши: смена состояния виджета на active при наведении и normal при уходе
mid_lbl.bind("<Enter>", lambda x: x.widget.config(state="active"))
mid_lbl.bind("<Leave>", lambda x: x.widget.config(state="normal"))

win.mainloop()