#%%
import PIL      
from PIL import Image, ImageTk


from funcoes import Dados
import time

print("Bem vindo ao nosso programa de rolagem de dados!")

arte = """   _______
  /\ o o o\\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/"""

print(arte)

print("Esse programa simula o lançamento de dados. Você pode escolher entre 1 e 4 Dados.")

n_dados =int(input("Quantos dados você quer lançar? (1-4) "))

while n_dados < 1 or n_dados > 4:
    print(" Entrada invalída,Tente novamente!")
    n_dados =int(input("Quantos dados você quer lançar? (1-4) "))


#%%
dados_jogo = Dados(n_dados)
dados_jogo.rolar_dados()
dados_jogo.mostrar_resultados()
dados_jogo.mostrar_resultados_art()

# %%
