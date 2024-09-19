import tkinter as tk
from View.Menu.index import index

class appManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Métodos Numéricos")
        self.geometry("1000x800")

        self._frame = None  # Inicializa o frame atual como None

        # Configura a janela principal para expandir
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)

        self.switch_frame(index(self))  # Chama a tela inicial

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()

        #new_frame = frame_class
        #if hasattr(self, "_frame"):
            #self._frame.destroy()

        self._frame = frame_class
        #self._frame = new_frame
        self._frame.pack(fill="both", expand=True)
        #self._frame.grid(row=0, column=0, sticky="nsew")