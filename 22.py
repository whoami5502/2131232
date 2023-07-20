from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
letras = len(nome) - nome.count(' ')
primeiro = nome.find(' ')

print('Analisando seu nome')

print('.'* 3)
sleep(1)
print('.'* 3)
sleep(1)
print('.'* 3)
sleep(1)
print('.'* 3)
sleep(1)

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {letras} letras')
print(f'Seu primeiro nome tem {primeiro} letras')
