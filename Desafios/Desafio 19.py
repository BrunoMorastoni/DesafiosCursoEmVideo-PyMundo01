import random
aluno1=str(input('Coloque o nome do primeiro aluno:'))
aluno2=str(input('Coloque o nome do segundo aluno:'))
aluno3=str(input('Coloque o nome do terceiro aluno:'))
aluno4=str(input('Coloque o nome do quarto aluno:'))
lista=[aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi {random.choice(lista)}')