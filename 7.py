n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

s = n1 + n2
m = s / 2

if m < 7.0:
    print(f'A média entre {n1} e  {n2} é {m} e infelizmente o aluno está de recuperação =(')
else:
    print(f'A média entre {n1} e {n2} é {m} e o aluno passou =D')


