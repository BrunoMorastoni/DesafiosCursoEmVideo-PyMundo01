vel=float(input('Quantos Km/h você estava andando?'))
multa= (vel - 80)*7
if vel > 80:
    print(f'Você estava andando a {vel} Km/h, sua foi de R$:{multa}')
else:
    print(f'Você estava na velocidade permitida de {vel} Km/h')