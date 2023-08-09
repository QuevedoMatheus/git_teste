import random
from .messages import display_messages
import time 

print('iniciando o projeto')
time.sleep(3)


while True:
    resposta = input('Deseja receber um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
            mensagem = random.choice(display_messages)
            print(mensagem)
            print( )