import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class telaPlotagem(tk.Frame):
    def __init__(self, parent, func_lambda, inicio, fim):
        super().__init__(parent)
        self.controller = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Plotar a função
        self.plot_function(func_lambda, inicio, fim)

    def plot_function(self, func_lambda, inicio, fim):
        x_vals = np.linspace(inicio, fim, 400)
        y_vals = func_lambda(x_vals)

        # Criar a figura e o eixo para o gráfico
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x_vals, y_vals, label="f(x)")
        ax.set_title("Plotagem de f(x)")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True)

        # Integrar o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)