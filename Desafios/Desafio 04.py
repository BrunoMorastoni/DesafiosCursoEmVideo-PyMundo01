n=input('Digite a algo:')
print('o seu tipo primitivo é', type(n))
print('Tem letras:', n.isalpha())
print('Tem números:', n.isnumeric())
print('Tem valor decimal:', n.isdecimal())
print('Está todo em "Caps":', n.isupper())
