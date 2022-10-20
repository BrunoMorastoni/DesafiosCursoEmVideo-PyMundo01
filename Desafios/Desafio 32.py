a=int(input('Digite um ano para que possamos saber se é bissexto'))
if a%4==0 and a%100 != 0 or a%400==0:
    print(f'O ano {a} é bissexto')
else:
    print(f'O ano {a} não é bissexto')