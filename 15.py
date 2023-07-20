nome = input('Olá, seja bem vindo(a) a concesionaria, qual é seu nome?: ')
print(f'Prazer em te conhecer {nome}, eu irei analisar o valor do véiculo que você alugou.')
print('Poderia me dizer a marca do véiculo?')
marca = input('Digite a marca do véiculo: ')
print('Obrigado, agora posso analisar melhor.')
print('Apenas irei te fazer algumas perguntas')
dias = int(input('Seu véiculo está alugado a quantos dias?: '))
km = float(input('Seu véiculo andou quantos km?: '))
pagodia = dias * 60
pagokm= km  * 0.15
pago = pagodia + pagokm
print(f'Pelas informações, você tem que pagar no total: {pago:.2f}R$, veja aqui os gastos: \n R${pagodia:.2f} de dias alugados e R${pagokm:.2f} de km rodados.')

