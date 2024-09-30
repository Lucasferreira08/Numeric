from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Metodos.metodosFuncoes import metodosFuncoes


class multiplos(tk.Frame):
    def __init__(self, parent, inicio, fim, erro, funcao, deriv, bissection, fp, newton, secantes):
        super().__init__(parent)
        from Menu.menu import index
        self.controller = parent
        self.inicio = inicio
        self.fim = fim
        self.inicioGraf = inicio
        self.fimGraf = fim
        self.erro = erro
        self.funcao = funcao
        self.deriv = deriv
        self.bissection = bissection
        self.fp = fp
        self.newton = newton
        self.secantes = secantes

        self.iteracoes_b, self.inicio, self.fim = metodosFuncoes.bissectionFunction(self.funcao, self.inicio, self.fim, self.erro, self.bissection)
        self.iteracoes_fp, self.inicio, self.fim = metodosFuncoes.fpFunction(self.funcao, self.inicio, self.fim, self.erro, self.fp)
        self.iteracoes_s, self.inicio, self.fim = metodosFuncoes.secant_method(self.funcao, self.inicio, self.fim, self.erro, self.secantes)
        self.iteracoes_n = metodosFuncoes.newtonFunction(self.funcao, self.deriv, self.inicio, self.fim, self.erro, self.newton)

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Criar um título para a tela
        title = tk.Label(self, text="Iterações do Método da Bissecção", font=("Arial", 16))
        title.grid(row=0, column=0, pady=5, sticky="n") # pady=10

        self.plot_function(self.funcao, self.inicioGraf, self.fimGraf)

        #self.bissectionFunction()
        self.create_table1(self.iteracoes_b, "Bissecção", 2, 0)

        #self.fpFunction()
        self.create_table1(self.iteracoes_fp, "Falsa-Posição", 3, 0)

        #self.secant_method(self.funcao, self.inicio, self.fim, self.erro, self.secantes)
        self.create_table3(self.iteracoes_s, "Secantes", 4, 0)

        #self.newtonFunction()
        self.create_table2(self.iteracoes_n, "Raphson-Newton", 5, 0)

        # Adicionar botões
        btn_voltar = tk.Button(self, text="Voltar ao Menu", command=lambda: self.controller.switch_frame(index(self.controller)))
        btn_voltar.grid(row=6, column=0, padx=10, pady=10, sticky="s")

    def create_table1(self, iteracoes, titulo, row, col):
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew") # pady=10

        # Cria a tabela
        self.tree = ttk.Treeview(frame_tabela, columns=(f"Iteração", "a", "b", "f(a)", "f(b)", "Erro"), show="headings")
        self.tree.heading("Iteração", text=f"Iteração({titulo})")
        self.tree.heading("a", text="a")
        self.tree.heading("b", text="b")
        self.tree.heading("f(a)", text="x")
        self.tree.heading("f(b)", text="f(x)")
        self.tree.heading("Erro", text="Erro")

        self.tree.column("Iteração", width=80, anchor="center")
        self.tree.column("a", width=80, anchor="center")
        self.tree.column("b", width=80, anchor="center")
        self.tree.column("f(b)", width=80, anchor="center")
        self.tree.column("f(a)", width=80, anchor="center")
        self.tree.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (a, b, x, fx, erro) in enumerate(iteracoes):
            self.tree.insert("", "end", values=(i + 1, f"{a:.6f}", f"{b:.6f}", f"{x:.6f}", f"{fx:.6f}", f"{erro:.6f}"))

    def create_table2(self, iteracoes, titulo, row, col):
        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Cria o título da tabela
        #table_title = tk.Label(frame_tabela, text=titulo, font=("Arial", 14))
        #table_title.grid(row=0, column=0, pady=5)

        # Cria a tabela
        self.tree2 = ttk.Treeview(frame_tabela, columns=("Iteração", "x", "f(x)", "Erro"), show="headings")
        self.tree2.heading("Iteração", text=f"Iteração({titulo})")
        self.tree2.heading("x", text="x")
        self.tree2.heading("f(x)", text="f(x)")
        self.tree2.heading("Erro", text="Erro")

        self.tree2.column("Iteração", width=80, anchor="center")
        self.tree2.column("x", width=80, anchor="center")
        self.tree2.column("f(x)", width=80, anchor="center")
        self.tree2.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree2.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        self.tree2.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (x, fx, erro) in enumerate(iteracoes):
            self.tree2.insert("", "end", values=(i + 1, f"{x:.6f}", f"{fx:.6f}", f"{erro:.6f}"))

    def create_table3(self, iteracoes, titulo, row, col):
        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Cria o título da tabela
        table_title = tk.Label(frame_tabela, text=titulo, font=("Arial", 14))
        table_title.grid(row=0, column=0, pady=5, sticky="n")

        # Cria a tabela
        self.tree3 = ttk.Treeview(frame_tabela, columns=("Iteração", "x0", "x1", "f(x0)", "f(x1)", "x", "f(x2)", "Erro"), show="headings")
        self.tree3.heading("Iteração", text=f"Iteração({titulo})")
        self.tree3.heading("x0", text="x0")
        self.tree3.heading("x1", text="x1")
        self.tree3.heading("f(x0)", text="f(x0)")
        self.tree3.heading("f(x1)", text="f(x1)")
        self.tree3.heading("x", text="x2")
        self.tree3.heading("f(x2)", text="f(x2)")
        self.tree3.heading("Erro", text="Erro")

        self.tree3.column("Iteração", width=80, anchor="center")
        self.tree3.column("x0", width=80, anchor="center")
        self.tree3.column("x1", width=80, anchor="center")
        self.tree3.column("f(x0)", width=80, anchor="center")
        self.tree3.column("f(x1)", width=80, anchor="center")
        self.tree3.column("x", width=80, anchor="center")
        self.tree3.column("f(x2)", width=80, anchor="center")
        self.tree3.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=self.tree3.yview)
        self.tree3.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        self.tree3.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (x0, x1, f_x0, f_x1, x, f_x2) in enumerate(iteracoes):
            self.tree3.insert("", "end", values=(i + 1, f"{x0:.6f}", f"{x1:.6f}", f"{f_x0:.6f}", f"{f_x1:.6f}", f"{x:.6f}", f"{f_x2:.6f}", f"{self.erro:.6f}"))

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