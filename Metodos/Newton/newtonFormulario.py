import tkinter as tk
from tkinter import ttk
import sympy as sp
from Metodos.Newton.newton import newton

class newtonFormulario(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        label_title = ttk.Label(self, text="Parâmetros para Usar o Método", font=("Arial", 14))
        label_title.grid(row=0, column=0, columnspan=2, pady=10)

        label_func = ttk.Label(self, text="Função f(x):")
        label_func.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.func_entry = ttk.Entry(self)
        self.func_entry.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

        # Campo para a derivada da função
        label_deriv = ttk.Label(self, text="Derivada f'(x):")
        label_deriv.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.deriv_entry = ttk.Entry(self)
        self.deriv_entry.grid(row=2, column=1, sticky="ew", padx=20, pady=5)

        label_inicio = ttk.Label(self, text="Início do intervalo:")
        label_inicio.grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.inicio_entry = ttk.Entry(self)
        self.inicio_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=5)

        label_fim = ttk.Label(self, text="Fim do intervalo:")
        label_fim.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.fim_entry = ttk.Entry(self)
        self.fim_entry.grid(row=4, column=1, sticky="ew", padx=20, pady=5)

        label_tol = ttk.Label(self, text="Tolerância:")
        label_tol.grid(row=5, column=0, sticky="e", padx=10, pady=5)
        self.tol_entry = ttk.Entry(self)
        self.tol_entry.grid(row=5, column=1, sticky="ew", padx=20, pady=5)

        label_max_iter = ttk.Label(self, text="Número máximo de iterações:")
        label_max_iter.grid(row=6, column=0, sticky="e", padx=10, pady=5)
        self.max_iter_entry = ttk.Entry(self)
        self.max_iter_entry.grid(row=6, column=1, sticky="ew", padx=20, pady=5)

        submit_btn = ttk.Button(self, text="Enviar", command=self.submit)
        submit_btn.grid(row=7, column=0, columnspan=2, pady=20)

    def submit(self):
        func = self.func_entry.get()
        deriv = self.deriv_entry.get()
        inicio = float(self.inicio_entry.get())
        fim = float(self.fim_entry.get())
        tol = float(self.tol_entry.get())
        max_iter = int(self.max_iter_entry.get())

        x = sp.symbols('x')
        func_expr = sp.sympify(func)
        func_lambda = sp.lambdify(x, func_expr, "numpy")

        deriv_expr = sp.sympify(deriv)
        deriv_lambda = sp.lambdify(x, deriv_expr, "numpy")

        self.controller.switch_frame(newton(self.controller, inicio, fim, tol, func_lambda, deriv_lambda, max_iter))