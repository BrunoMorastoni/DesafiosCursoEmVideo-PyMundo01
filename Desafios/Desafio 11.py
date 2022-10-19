print('Vamos descobrir quanto de tinta será necessário para pintar certa parede!!!')
altura=float(input('Qual a altura desta parede'))
largura=float(input('Qual a largura desta parede'))
area=altura*largura
tinta=area/2
print(f'Sabendo que a parede tem {altura}m de altura e {largura}m de largura descobrimos que esta parede tem {area}m²\nlogo será necessário {tinta}l de tinta para pintala')