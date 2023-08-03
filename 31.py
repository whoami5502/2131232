from time import sleep
distancia  = float(input('Digite a distancia da sua viagem: '))
sleep (1)
print(f'Oh, então voce quer uma viagem de {distancia:.0f} km?, eu posso calcular o preço para você!')
print('Se for mais de 200 km eu posso fazer um descontinho para você!')
sleep (1)
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'Já fiz os calculos!, o preço da sua viagem é {preco:.2f} !')
