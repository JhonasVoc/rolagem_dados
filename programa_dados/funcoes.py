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
    
    def mostrar_resultados_art(self):
        print("\nResultados do lançamento com arte:")
        for resultado in self.resultados:
            for linha in DICE_ART[resultado]:
                print(linha)
            
        
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

