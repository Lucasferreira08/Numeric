import tkinter as tk
from Menu.menu import index

class appManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métodos Numéricos")
        self.geometry("1000x800")

        self.grid_rowconfigure(0, weight=1)  # Faz com que a janela se expanda verticalmente
        self.grid_columnconfigure(0, weight=1)  # Faz com que a janela se expanda horizontalmente

        self._frame = None
        self.switch_frame(index(self))

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class
        self._frame.grid(row=0, column=0, sticky="nsew")