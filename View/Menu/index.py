import tkinter as tk
from tkinter import ttk

from View.FalsaPosicao.fpFormulario import fpFormulario
from View.formulario import formulario


class index(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent

        # Centralizando o menu na tela, mas tornando responsivo
        frame = ttk.Frame(self, padding="30")
        frame.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Botões do menu
        bisseccao_btn = ttk.Button(frame, text="Bissecção", command=lambda: self.controller.switch_frame(formulario(self.controller)))
        bisseccao_btn.pack(fill='x', pady=5)
        #bisseccao_btn.grid(row=1, column=1, columnspan=2)

        falsa_posicao_btn = ttk.Button(frame, text="Falsa Posição", command=lambda: self.controller.switch_frame(fpFormulario(self.controller)))
        falsa_posicao_btn.pack(fill='x', pady=5)
        #falsa_posicao_btn.grid(row=2, column=1, columnspan=2)

        raphson_newton_btn = ttk.Button(frame, text="Raphson-Newton", command=lambda: self.controller.switch_frame(formulario))
        raphson_newton_btn.pack(fill='x', pady=5)
        #raphson_newton_btn.grid(row=3, column=1, columnspan=2)

        secantes_btn = ttk.Button(frame, text="Secantes", command=lambda: self.controller.switch_frame(formulario))
        secantes_btn.pack(fill='x', pady=5)
        #secantes_btn.grid(row=4, column=1, columnspan=2)

        multiplos_btn = ttk.Button(frame, text="Múltiplos Métodos", command=lambda: self.controller.switch_frame(formulario))
        multiplos_btn.pack(fill='x', pady=5)
        #multiplos_btn.grid(row=5, column=1, columnspan=2)