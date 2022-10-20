r1=float(input('Digite um valor:'))
r2=float(input('Digite um segundo valor:'))
r3=float(input('Digite um ultimo valor:'))
print('Vamos conferir se esses valores formam um triângulo')

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo')
else:
    print(f'As retas {r1}, {r2} e {r3} não podem formar um triângulo')