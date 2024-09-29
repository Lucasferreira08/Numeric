import tkinter as tk
from tkinter import ttk
import sympy as sp
from Metodos.MultiplosMetodos.multiplos import multiplos

class multiplosFormulario(tk.Frame):
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
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_rowconfigure(11, weight=1)
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

        label_b_iter = ttk.Label(self, text="Número de iterações(Bissecção):")
        label_b_iter.grid(row=7, column=0, sticky="e", padx=10, pady=5)
        self.iter_bissection = ttk.Entry(self)
        self.iter_bissection.grid(row=7, column=1, sticky="ew", padx=20, pady=5)

        label_fp_iter = ttk.Label(self, text="Número de iterações(Falsa Posição):")
        label_fp_iter.grid(row=8, column=0, sticky="e", padx=10, pady=5)
        self.iter_fp = ttk.Entry(self)
        self.iter_fp.grid(row=8, column=1, sticky="ew", padx=20, pady=5)

        label_s_iter = ttk.Label(self, text="Número de iterações(Secantes):")
        label_s_iter.grid(row=9, column=0, sticky="e", padx=10, pady=5)
        self.iter_secantes = ttk.Entry(self)
        self.iter_secantes.grid(row=9, column=1, sticky="ew", padx=20, pady=5)

        label_rn_iter = ttk.Label(self, text="Número de iterações(Raphson-Newton):")
        label_rn_iter.grid(row=10, column=0, sticky="e", padx=10, pady=5)
        self.iter_newton = ttk.Entry(self)
        self.iter_newton.grid(row=10, column=1, sticky="ew", padx=20, pady=5)

        submit_btn = ttk.Button(self, text="Enviar", command=self.submit)
        submit_btn.grid(row=11, column=0, columnspan=2, pady=20)

    def submit(self):
        func = self.func_entry.get()
        deriv = self.deriv_entry.get()
        inicio = float(self.inicio_entry.get())
        fim = float(self.fim_entry.get())
        tol = float(self.tol_entry.get())
        bissection = int(self.iter_bissection.get())
        fp = int(self.iter_fp.get())
        newton = int(self.iter_newton.get())
        secantes = int(self.iter_secantes.get())

        x = sp.symbols('x')
        func_expr = sp.sympify(func)
        func_lambda = sp.lambdify(x, func_expr, "numpy")

        deriv_expr = sp.sympify(deriv)
        deriv_lambda = sp.lambdify(x, deriv_expr, "numpy")

        self.controller.switch_frame(multiplos(self.controller, inicio, fim, tol, func_lambda, deriv_lambda, bissection, fp, newton, secantes))