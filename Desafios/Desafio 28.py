import random
n = int(input('Tente acertar o número entre 0 e 5:'))
na = random.randint(0,5)
if na == n:
    print(f'Parabéns você acertou o número {n}')
else:
    print(f'Você errou o número aleatório gerado era {na}')