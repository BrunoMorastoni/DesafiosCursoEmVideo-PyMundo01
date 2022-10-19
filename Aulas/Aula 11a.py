#                                       Representação de cores

#   Código de cor ===>  \033[(estilo)(texto)(background) m
#       exemplo: \033[0:33:44m

t1=2
t2=3
#print('\033[4;31;43mOlá, mundo!')
print(f'Texto colorido em \033[1;35;43m{t1}\033[m e tambêm em \033[4;32;46m{t2}\033[m')