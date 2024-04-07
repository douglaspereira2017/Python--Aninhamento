import random
from time import sleep
print('{:=^40}'.format('JOKENPO'))
i = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
a = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
sleep(1)
na = random.randint(0, 2)
print('-='*11)
print('Computador escolheu {},'.format(i[na]))
print('Jogador escoleu {} ,'.format(i[a]))
print('-='*11)
if na == 0 :
    if a == 0 :

        print('Empate')

    elif 1 == a:

        print('Jogador ganhou')

    elif 2 == a:

        print('Computador ganhou')
    else:
        print('Jogada invalida, tente novamente')

elif na == 1 :
    if a == 0:
        print('computador ganhou')
    elif a == 1:
        print('Empate')
    elif a == 2:
        print('Jogador ganhou')
    else:
        print('Jogada invalida, tente novamente')
elif na == 2 :

    if a == 0:
        print('Jogador ganhou')
    elif a == 1:
        print('computador ganhou')
    elif a == 2:
        print('Empate')
    else:
        print('Jogada invalida, tente novamente')