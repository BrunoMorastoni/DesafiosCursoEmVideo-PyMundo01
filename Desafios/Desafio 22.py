nome=input('Coloque seu nome completo:').strip()
print(f'Seu nome todo maiúsculo: {nome.upper()}')
print(f'Seu nome todo minúsculo: {nome.lower()}')
print(f'Seu nome tem {len(nome.strip())} letras, sem contar os espaços')
separado=nome.split()
print(f'Seu primeiro nome {separado[0]} tem {len(separado[0])} letras')