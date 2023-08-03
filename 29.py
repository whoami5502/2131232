velocidade = float(input('Digite a velocidade do seu véiculo: '))
multa = (velocidade-80) * 7
if velocidade <= 80:
    print('Tenha um bom-dia!, a velocidade do seu véiculo está no limite suportado')
else:
    print(f'MULTADO!, você foi multado pois atingiu uma velocidade acima de 80km, >>{velocidade:.0f}<<')
    print(f'Você deve pagar {multa:.2f}R$ de multa.')
