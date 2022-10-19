d=int(input('Qual a distância da sua viagem?'))
v1=d*0.50
v2=d*0.45
if d <= 200:
    print(f'A sua viagem de {d}Km, tem como valor da passagem R${v1:.2f}')
else:
    print(f'A sua viagem de {d}Km, tem como valor da passagem R${v2:.2f}')