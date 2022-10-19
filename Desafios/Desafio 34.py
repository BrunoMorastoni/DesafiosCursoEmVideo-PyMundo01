salario=float(input('Digite seu salário atual:'))
aumento1= salario+(salario*10/100)
aumento2= salario+(salario*15/100)
if salario > 1250:
    print(f'Parabéns você ganhou um aumento de 10% de {salario}, seu salário atual é de R${aumento1}.')
if salario <= 1250:
    print(f'Parabéns você ganhou um aumento de 15% de {salario}, seu salário atual é de R${aumento2}.')