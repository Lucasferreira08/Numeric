from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class fp(tk.Frame):
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
        self.fpFunction()

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Configurar o frame para não propagar o redimensionamento
        #self.grid_propagate(False)

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
        self.tree.heading("a", text="Início")
        self.tree.heading("b", text="Fim")
        self.tree.heading("f(a)", text="Média")
        self.tree.heading("f(b)", text="f(Média)")
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
            self.tree.insert("", "end", values=(i + 1, f"{a:.6f}", f"{b:.6f}", f"{fa:.6f}", f"{fb:.6f}", f"{erro:.6f}"))

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

    def meio(self, a, b):

        m = (self.funcao(b)*a - self.funcao(a)*b)/(self.funcao(b) - self.funcao(a))

        return m

    def fpFunction(self):
        #if self.funcao(self.inicio) * self.funcao(self.fim) >= 0:
            #return

        i=0
        while True:
            m = fp.meio(self, self.inicio, self.fim)
            i+=1

            self.iteracoes.append((self.inicio, self.fim, m, self.funcao(m), self.erro))

            if abs(self.funcao(m)) <= self.erro or i>=self.numIteracoes:
                break

            if self.funcao(self.inicio) * self.funcao(m) < 0:
                self.fim = m
            else:
                self.inicio = m