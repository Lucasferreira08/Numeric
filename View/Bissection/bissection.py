from tkinter import ttk
import tkinter as tk

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from View.Plotagem.telaPlotagem import telaPlotagem

class bissection(tk.Frame):
    def __init__(self, parent, inicio, fim, erro, funcao):
        super().__init__(parent)
        from View.Menu.index import index
        self.controller = parent
        self.inicio = inicio
        self.fim = fim
        self.erro = erro
        self.funcao = funcao
        self.iteracoes = []
        self.bissectionFunction()

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Configurar o frame para não propagar o redimensionamento
        self.grid_propagate(False)

        # Criar um título para a tela
        title = tk.Label(self, text="Iterações do Método da Bissecção", font=("Arial", 16))
        title.grid(row=0, column=0, pady=10, sticky="n")

        self.plot_function(funcao, inicio, fim)

        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Criar uma tabela para mostrar as iterações
        self.tree = ttk.Treeview(frame_tabela, columns=("Iteração", "a", "b", "f(a)", "f(b)", "Erro"), show="headings")
        self.tree.heading("Iteração", text="Iteração")
        self.tree.heading("a", text="a")
        self.tree.heading("b", text="b")
        self.tree.heading("f(a)", text="f(a)")
        self.tree.heading("f(b)", text="f(b)")
        self.tree.heading("Erro", text="Erro")

        # Configurar as colunas para centralização
        self.tree.column("Iteração", width=80, anchor="center")
        self.tree.column("a", width=80, anchor="center")
        self.tree.column("b", width=80, anchor="center")
        self.tree.column("f(a)", width=80, anchor="center")
        self.tree.column("f(b)", width=80, anchor="center")
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
        for i, (a, b, fa, fb, erro) in enumerate(self.iteracoes):
            self.tree.insert("", "end", values=(i + 1, f"{a:.4f}", f"{b:.4f}", f"{fa:.4f}", f"{fb:.4f}", f"{erro:.4f}"))

        # Adicionar botões
        btn_voltar = tk.Button(self, text="Voltar ao Menu", command=lambda: self.controller.switch_frame(index(self.controller)))
        btn_voltar.grid(row=3, column=0, sticky="sw", padx=10, pady=10)

        btn_plotar = tk.Button(self, text="Plotar Função", command=lambda: self.controller.switch_frame(
                lambda: telaPlotagem(self.controller, funcao, inicio, fim)))
        btn_plotar.grid(row=3, column=0, sticky="se", padx=10, pady=10)

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

    @staticmethod
    def meio(a, b):
        m = (b + a) / 2
        return m

    def bissectionFunction(self):
        if self.funcao(self.inicio) * self.funcao(self.fim) >= 0:
            print("Não é certo a existência de raiz")
            exit()

        if abs(self.funcao(self.inicio)) <= self.erro:
            print(f"Raiz {self.inicio} - {self.funcao(self.inicio)}")

        if abs(self.funcao(self.fim)) <= self.erro:
            print(f"Raiz {self.fim} - {self.funcao(self.fim)}")
        i = 0
        while True:
            m = bissection.meio(self.inicio, self.fim)

            self.iteracoes.append((self.inicio, self.fim, m, self.funcao(m), self.erro))
            
            i += 1
            if abs(self.funcao(m)) <= self.erro:
                print(f"Raiz {m} - {self.funcao(m)}")
                break

            if self.funcao(self.inicio) * self.funcao(m) < 0:
                self.fim = m
            else:
                self.inicio = m