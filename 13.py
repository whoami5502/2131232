salário = float(input('Digite o salário de um funcionario: R$ '))
novo = (salário * 15 / 100)
aumento = novo + salário

print(f'O salário do funcionário que antes era {salário:.2f} agora é {aumento:.2f} pelo aumento de 15%')
