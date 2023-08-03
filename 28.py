from random import randint
cpu = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ele.....') #Faz o computador ''PENSAR'' em um número de 0 a 5
print('-=-' * 20)
player = int(input('Em que número  eu pensei?: ')) #Pergunta ao usuário qual número o computador ''PENSOU''
if player == cpu:
    print('Parabéns!, Você acertou o número!!')
else
    print(f'Você errou o número :( \n O número era {cpu}, nao {player}!')
