import random

display_messages = [
    'Seja Feliz ;)',
    'Fique Tranquilo'

]

while True:
    resposta = input('Deseja receber um conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
            mensagem = random.choice(display_messages)
            print(mensagem)
            print( )