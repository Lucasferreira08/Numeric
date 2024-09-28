import tkinter as tk
from tkinter import ttk
from Metodos.FalsaPosicao.fpFormulario import fpFormulario
from Metodos.Bissection.formulario import formulario
from Metodos.Newton.newtonFormulario import newtonFormulario
from Metodos.Secantes.secantesFormulario import secantesFormulario


class index(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent

        # Configuração da grid para o frame principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Criação dos botões do menu
        btn_bisseccao = ttk.Button(self, text="Método da Bissecção",
                                  command=lambda: parent.switch_frame(formulario(self.controller)))
        btn_falsa_posicao = ttk.Button(self, text="Método da Falsa Posição",
                                      command=lambda: parent.switch_frame(fpFormulario(self.controller)))
        btn_newton = ttk.Button(self, text="Método de Newton-Raphson",
                               command=lambda: parent.switch_frame(newtonFormulario(self.controller)))
        btn_secantes = ttk.Button(self, text="Método das Secantes",
                                 command=lambda: parent.switch_frame(secantesFormulario(self.controller)))

        # Posicionamento dos botões usando grid
        btn_bisseccao.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        btn_falsa_posicao.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        btn_newton.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        btn_secantes.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Centraliza o frame dentro da janela
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)  # Permite que as linhas cresçam
        self.grid_columnconfigure(0, weight=1)  # Espaçamento antes do menu
        self.grid_columnconfigure(2, weight=1)