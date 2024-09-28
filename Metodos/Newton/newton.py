from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class newton(tk.Frame):
    def __init__(self, parent, inicio, fim, erro, funcao, deriv, num_iteracoes):
        super().__init__(parent)
        from Menu.index import index
        self.controller = parent
        self.inicio = inicio
        self.fim = fim
        self.erro = erro
        self.funcao = funcao
        self.deriv = deriv
        self.numIteracoes = num_iteracoes
        self.iteracoes = []
        self.newtonFunction()

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Criar um título para a tela
        title = tk.Label(self, text="Iterações do Método Raphson-Newton", font=("Arial", 16))
        title.grid(row=0, column=0, pady=10, sticky="n")

        self.plot_function(funcao, inicio, fim)

        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Criar uma tabela para mostrar as iterações
        self.tree = ttk.Treeview(frame_tabela, columns=("Iteração", "x", "f(x)", "Erro"), show="headings")
        self.tree.heading("Iteração", text="Iteração")
        self.tree.heading("x", text="x")
        self.tree.heading("f(x)", text="f(x)")
        self.tree.heading("Erro", text="Erro")

        # Configurar as colunas para centralização
        self.tree.column("Iteração", width=80, anchor="center")
        self.tree.column("x", width=80, anchor="center")
        self.tree.column("f(x)", width=80, anchor="center")
        self.tree.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Expandir a área da tabela
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preencher a tabela com as iterações (exemplo de dados)
        for i, (x, fx, erro) in enumerate(self.iteracoes):
            self.tree.insert("", "end", values=(i + 1, f"{x:.6f}", f"{fx:.6f}", f"{erro:.6f}"))

        # Adicionar botões
        btn_voltar = tk.Button(self, text="Voltar ao Menu", command=lambda: self.controller.switch_frame(index(self.controller)))
        btn_voltar.grid(row=3, column=0, sticky="s", padx=10, pady=10)

    def plot_function(self, func_lambda, inicio, fim):
        x_vals = np.linspace(inicio, fim, 400)
        y_vals = func_lambda(x_vals)

        # Criar a figura e o eixo para o gráfico
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(x_vals, y_vals, label="f(x)")
        ax.set_title("Plotagem de f(x)")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True)

        # Remover espaços extras em torno do gráfico
        fig.tight_layout()

        # Integrar o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)

    def newtonFunction(self):
        xn = self.inicio
        for n in range(self.numIteracoes):
            fxn = self.funcao(xn)
            dfxn = self.deriv(xn)

            self.iteracoes.append((xn, fxn, self.erro))

            if abs(fxn) < self.erro:
                return xn
            if dfxn == 0:
                return None
            xn = xn - fxn / dfxn
        return None
