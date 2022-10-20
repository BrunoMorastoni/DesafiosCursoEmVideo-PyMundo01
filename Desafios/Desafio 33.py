n1=int(input('Coloque um número inteiro:'))
n2=int(input('Coloque mais um número inteiro:'))
n3=int(input('Coloque o último número inteiro:'))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')