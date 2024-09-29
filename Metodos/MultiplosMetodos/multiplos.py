from tkinter import ttk
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        self.iteracoes_b = []
        self.iteracoes_fp = []
        self.iteracoes_n = []
        self.iteracoes_s = []
        self.bissectionFunction()
        self.fpFunction()
        self.secant_method(self.funcao, self.inicio, self.fim, self.erro, self.secantes)
        self.newtonFunction()

        # Configurar o grid para tornar a tela responsiva
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Configurar o frame para não propagar o redimensionamento
        self.grid_propagate(False)

        # Criar um título para a tela
        title = tk.Label(self, text="Iterações do Método da Bissecção", font=("Arial", 16))
        title.grid(row=0, column=0, pady=5, sticky="n") # pady=10

        self.plot_function(self.funcao, self.inicioGraf, self.fimGraf)

        #self.bissectionFunction()
        self.create_table1(self.iteracoes_b, "Iterações Bissecção", 2, 0)

        #self.fpFunction()
        self.create_table1(self.iteracoes_fp, "Iterações Falsa-Posição", 3, 0)

        #self.secant_method(self.funcao, self.inicio, self.fim, self.erro, self.secantes)
        self.create_table3(self.iteracoes_s, "Iterações Secantes", 4, 0)

        #self.newtonFunction()
        self.create_table2(self.iteracoes_n, "Iterações Raphson-Newton", 5, 0)

        # Adicionar botões
        btn_voltar = tk.Button(self, text="Voltar ao Menu", command=lambda: self.controller.switch_frame(index(self.controller)))
        btn_voltar.grid(row=6, column=0, sticky="s", padx=10, pady=10)

    def create_table1(self, iteracoes, titulo, row, col):
        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew") # pady=10

        # Cria o título da tabela
        #table_title = tk.Label(frame_tabela, text=titulo, font=("Arial", 14))
        #table_title.grid(row=0, column=0, pady=5)

        # Cria a tabela
        tree = ttk.Treeview(frame_tabela, columns=("Iteração", "a", "b", "f(a)", "f(b)", "Erro"), show="headings")
        tree.heading("Iteração", text="Iteração")
        tree.heading("a", text="a")
        tree.heading("b", text="b")
        tree.heading("f(a)", text="x")
        tree.heading("f(b)", text="f(x)")
        tree.heading("Erro", text="Erro")

        tree.column("Iteração", width=80, anchor="center")
        tree.column("a", width=80, anchor="center")
        tree.column("b", width=80, anchor="center")
        tree.column("f(b)", width=80, anchor="center")
        tree.column("f(a)", width=80, anchor="center")
        tree.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tree.yview)
        tree.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (a, b, x, fx, erro) in enumerate(iteracoes):
            tree.insert("", "end", values=(i + 1, f"{a:.6f}", f"{b:.6f}", f"{x:.6f}", f"{fx:.6f}", f"{erro:.6f}"))

    def create_table2(self, iteracoes, titulo, row, col):
        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Cria o título da tabela
        #table_title = tk.Label(frame_tabela, text=titulo, font=("Arial", 14))
        #table_title.grid(row=0, column=0, pady=5)

        # Cria a tabela
        tree = ttk.Treeview(frame_tabela, columns=("Iteração", "x", "f(x)", "Erro"), show="headings")
        tree.heading("Iteração", text="Iteração")
        tree.heading("x", text="x")
        tree.heading("f(x)", text="f(x)")
        tree.heading("Erro", text="Erro")

        tree.column("Iteração", width=80, anchor="center")
        tree.column("x", width=80, anchor="center")
        tree.column("f(x)", width=80, anchor="center")
        tree.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tree.yview)
        tree.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (x, fx, erro) in enumerate(iteracoes):
            tree.insert("", "end", values=(i + 1, f"{x:.6f}", f"{fx:.6f}", f"{erro:.6f}"))

    def create_table3(self, iteracoes, titulo, row, col):
        # Criar uma área de scroll para a tabela
        frame_tabela = tk.Frame(self)
        frame_tabela.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Cria o título da tabela
        table_title = tk.Label(frame_tabela, text=titulo, font=("Arial", 14))
        table_title.grid(row=0, column=0, pady=5, sticky="n")

        # Cria a tabela
        tree = ttk.Treeview(frame_tabela, columns=("Iteração", "x0", "x1", "f(x0)", "f(x1)", "x", "f(x2)", "Erro"), show="headings")
        tree.heading("Iteração", text="Iteração")
        tree.heading("x0", text="x0")
        tree.heading("x1", text="x1")
        tree.heading("f(x0)", text="f(x0)")
        tree.heading("f(x1)", text="f(x1)")
        tree.heading("x", text="x2")
        tree.heading("f(x2)", text="f(x2)")
        tree.heading("Erro", text="Erro")

        tree.column("Iteração", width=80, anchor="center")
        tree.column("x0", width=80, anchor="center")
        tree.column("x1", width=80, anchor="center")
        tree.column("f(x0)", width=80, anchor="center")
        tree.column("f(x1)", width=80, anchor="center")
        tree.column("x", width=80, anchor="center")
        tree.column("f(x2)", width=80, anchor="center")
        tree.column("Erro", width=80, anchor="center")

        # Barra de rolagem
        scrollbar_y = ttk.Scrollbar(frame_tabela, orient=tk.VERTICAL, command=tree.yview)
        tree.config(yscrollcommand=scrollbar_y.set)

        # Posicionar a tabela e a barra de rolagem no grid
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")

        # Configurar grid no frame
        frame_tabela.grid_rowconfigure(0, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Preenche a tabela com os dados
        for i, (x0, x1, f_x0, f_x1, x, f_x2) in enumerate(iteracoes):
            tree.insert("", "end", values=(i + 1, f"{x0:.6f}", f"{x1:.6f}", f"{f_x0:.6f}", f"{f_x1:.6f}", f"{x:.6f}", f"{f_x2:.6f}", f"{self.erro:.6f}"))

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
        if self.bissection == 0:
            return

        i = 0
        while True:
            m = multiplos.meio(self.inicio, self.fim)

            self.iteracoes_b.append((self.inicio, self.fim, m, self.funcao(m), self.erro))

            i += 1
            if abs(self.funcao(m)) <= self.erro:
                print(f"Raiz {m} - {self.funcao(m)}")
                break

            if self.funcao(self.inicio) * self.funcao(m) < 0:
                self.fim = m
            else:
                self.inicio = m

            if (i>=self.bissection): break;

    def meioFp(self, a, b):

        m = (self.funcao(b)*a - self.funcao(a)*b)/(self.funcao(b) - self.funcao(a))

        return m

    def fpFunction(self):
        #if self.funcao(self.inicio) * self.funcao(self.fim) >= 0:
            #return

        if self.fp == 0:
            return

        i=0
        while True:
            m = multiplos.meioFp(self, self.inicio, self.fim)
            i+=1

            self.iteracoes_fp.append((self.inicio, self.fim, m, self.funcao(m), self.erro))

            if abs(self.funcao(m)) <= self.erro or i>=self.fp:
                break

            if self.funcao(self.inicio) * self.funcao(m) < 0:
                self.fim = m
            else:
                self.inicio = m

            if (i >= self.fp): break;

    def newtonFunction(self):
        xn = self.inicio
        if (self.newton == 0): return
        for n in range(self.newton):
            fxn = self.funcao(xn)
            dfxn = self.deriv(xn)

            self.iteracoes_n.append((xn, fxn, self.erro))

            if abs(fxn) < self.erro:
                return xn
            if dfxn == 0:
                return xn
            xn = xn - fxn / dfxn

            if (n+1 >= self.newton): return

    def secant_method(self, f, x0, x1, tol, max_iter):
        if (self.secantes == 0): return
        for i in range(max_iter):
            # Calcula o valor da função nos pontos x0 e x1
            f_x0 = f(x0)
            f_x1 = f(x1)

            # Evitar divisão por zero
            if f_x1 - f_x0 == 0:
                return

            # Fórmula do método das secantes
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

            self.iteracoes_s.append((x0, x1, f_x0, f_x1, x2, f(x2)))

            # Verifica a tolerância
            if abs(x2 - x1) < tol:
                return

            # Atualiza os pontos
            x0 = x1
            x1 = x2

            self.inicio = x1
            self.fim = x2

            if (i+1 >= self.secantes): return