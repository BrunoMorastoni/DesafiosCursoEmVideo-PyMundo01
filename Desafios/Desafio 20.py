import random
a1=str(input('1º aluno:'))
a2=str(input('2º aluno:'))
a3=str(input('3º aluno:'))
a4=str(input('4º aluno:'))
lista=[a1, a2, a3, a4]
print(f'Os alunos {lista} foram sorteados\nassim:{random.sample(lista, k=4)}')
