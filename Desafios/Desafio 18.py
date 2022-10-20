import math
angulo=float(input('Coloque um ângulo:'))

#Jeito trabalhoso e foda
print(f'O ângulo {angulo} traduzido é\nSENO:{math.sin(math.radians(angulo)):.2f}\nCOSSENO:{math.cos(math.radians(angulo)):.2f}\nTANGENTE:{math.tan(math.radians(angulo)):.2f}')

#Jeito facil
    #seno=math.sin(math.radians(angulo))
    #print('O ângulo {} tem o seno de {:.2f}'.format(angulo, seno))
    #cosseno=math.cos(math.radians(angulo))
    #print('O ângulo {} tem o seno de {:.2f}'.format(angulo, cosseno))
    #tangente=math.tan(math.radians(angulo))
    #print('O ângulo {} tem o seno de {:.2f}'.format(angulo, tangente))