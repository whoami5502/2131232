v = input('Digite um valor:')

print(f'O tipo primitivo desse valor é {type(v)}')
print(f'Seu valor é apenas espaços? {v.isspace()}')
print(f'Seu valor é alfabetico? {v.isalpha()}')
print(f'Seu valor é um número? {v.isnumeric()}')
print(f'Seu valor contém apenas maiúsculas? {v.isupper()}')
print(f'Seu valor contém apenas minúsculas? {v.islower()}')
print(f'Seu valor está capitalizado? {v.istitle()}')


