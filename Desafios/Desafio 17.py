from math import hypot
co=float(input('Qual o valor do cateto oposto?'))
ca=float(input('Qual o valor do cateto adjacente?'))
print(f'A hipotenusa desse triângulo retângulo será de {hypot(co, ca):.2f}')

#Método antigo sem o import
    #hip=(co ** 2 + ca ** 2)**(1/2)
    #print(f'A hipotenusa desse triângulo retângulo será de {hip:.2f}')
