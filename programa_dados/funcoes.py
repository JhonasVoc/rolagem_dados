from random import randint

class Dados:
    def __init__(self, n_dados):
        self.n_dados = n_dados
        self.resultados = []
    
    def rolar_dados(self):
        self.resultados.clear()  # limpa resultados anteriores
        for _ in range(self.n_dados):
            self.resultados.append(randint(1, 6))
        return self.resultados
    
    def mostrar_resultados(self):
        print("\nResultados do lançamento:")
        for i, resultado in enumerate(self.resultados, 1):
            print(f"Dado {i}: {resultado}")
        print(f"Soma total: {sum(self.resultados)}")

import random
#%%
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

linhas = DICE_ART[2]
for linha in linhas:
    print(linha)


