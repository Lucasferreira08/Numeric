from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class secantes(tk.Frame):
    def __init__(self, parent, inicio, fim, erro, funcao, num_iteracoes):
        super().__init__(parent)
        from Menu.menu import index
        self.controller = parent
        self.inicio = inicio
        self.fim = fim
        self.erro = erro
        self.funcao = funcao
        self.numIteracoes = num_iteracoes
        self.iteracoes = []
        self.secant_method(self.funcao, self.inicio, self.fim, self.erro, self.numIteracoes)

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Criar um título para a tela
        title = tk.Label(self, text="Iterações do Método das Secantes", font=("Arial", 16))
        title.grid(row=0, column=0, pady=10, sticky="n")

        self.plot_function(funcao, inicio, fim)

        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Criar uma tabela para mostrar as iterações
        self.tree = ttk.Treeview(frame_tabela, columns=("Iteração", "x0", "x1", "f(x0)", "f(x1)", "x", "f(x2)", "Erro"), show="headings")
        self.tree.heading("Iteração", text="Iteração")
        self.tree.heading("x0", text="x0")
        self.tree.heading("x1", text="x1")
        self.tree.heading("f(x0)", text="f(x0)")
        self.tree.heading("f(x1)", text="f(x1)")
        self.tree.heading("x", text="x2")
        self.tree.heading("f(x2)", text="f(x2)")
        self.tree.heading("Erro", text="Erro")

        # Configurar as colunas para centralização
        self.tree.column("Iteração", width=80, anchor="center")
        self.tree.column("x0", width=80, anchor="center")
        self.tree.column("x1", width=80, anchor="center")
        self.tree.column("f(x0)", width=80, anchor="center")
        self.tree.column("f(x1)", width=80, anchor="center")
        self.tree.column("x", width=80, anchor="center")
        self.tree.column("f(x2)", width=80, anchor="center")
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
        for i, (x0, x1, f_x0, f_x1, x, f_x2) in enumerate(self.iteracoes):
            self.tree.insert("", "end", values=(i + 1, f"{x0:.6f}", f"{x1:.6f}", f"{f_x0:.6f}", f"{f_x1:.6f}", f"{x:.6f}", f"{f_x2:.6f}", f"{erro:.6f}"))

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

    def secant_method(self, f, x0, x1, tol, max_iter):
        for i in range(max_iter):
            # Calcula o valor da função nos pontos x0 e x1
            f_x0 = f(x0)
            f_x1 = f(x1)

            # Evitar divisão por zero
            if f_x1 - f_x0 == 0:
                return

            # Fórmula do método das secantes
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

            self.iteracoes.append((x0, x1, f_x0, f_x1, x2, f(x2)))

            # Verifica a tolerância
            if abs(x2 - x1) < tol:
                return

            # Atualiza os pontos
            x0 = x1
            x1 = x2

        return