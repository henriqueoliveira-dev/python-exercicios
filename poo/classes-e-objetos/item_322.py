"""Conteúdo extraído de: 15_Avores01.ipynb_1vmN3BW1.ipynb
Célula original: 0
Origem registrada no manifesto: Drive
Tipo: 📚 Aula/exemplo
"""

import tkinter as tk

from tkinter import ttk, messagebox

import networkx

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class No:

    def __init__(self, valor):

        self.valor = valor

        self.esquerdo = None

        self.direito = None

class ABB:

    def __init__(self):

        self.raiz = None

    def inserir(self, valor):

        if self.raiz is None:

             self.raiz = No(valor)

        else:
             self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):

         if valor < no_atual:

            if no_atual.esquerdo is None:

                no_atual.esquerdo =  No(valor)

            else:

                self._inserir_recursivo(no_atual.esquerdo, valor)

            if no_atual.direito is None:

                no_atual.direito =  No(valor)

            else:

                self._inserir_recursivo(no_atual.direito, valor)
