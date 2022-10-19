#                                       ANÁLISES / Curso em Vídeo Python

# len(frase) => Mostra o comprimento da frase. 

# frase.count('o') => Vai contar a quantidade de vezes que a letra 'o' aparece na frase.
    # frase.count('o',0,13) => já ira fatiar a contagem.

# frase.find('deo') => Vai mostrar o começo de 'deo' na frase.
# frase.rfind('deo') => Vai mostrar o final de 'deo' na frase.
    # frase.find('Android') => o resultado será '-1' quando não for encontrado.

# 'Curso' in frase => vai mostar se existe a palavra selecionada na frase, true ou false.

#                                       TRANSFORMAÇÃO / Curso em Vídeo Python

# frase.replace('Python','Android') => ele irá substituir a palavra Python por Android assim: Curso em Vídeo Android.

# frase.upper() => Irá trocar as letras para maiusculo quando não estiver.
# frase.lower() => Irá trocas as letras para minúsculo quando não estiver.

# frase.capitalize() => Irá deixar tudo em minúsculo porem só o inicio da frase estara em maiúsculo.
# frase.title() => Irá deixar em maiúsculo todo início de palavra.

# frase.strip() => Remove todo espaço inútil tanto no início quando no fim da frase.
    # frase.rstrip() => Removera APENAS os ultimos espaços da frase ao seja na direita (r=right)
    # frase.lstrip() => Removera APENAS os primeiros espaços da frase ao seja na esquerda(l=left)

#                                       DÍVISÃO e JUNÇÃO / Curso em Vídeo Python

# frase.split() => Vai dividir as palavras da frase pelo espaço, criando uma "lista" palavras/ elementos.
# '-'.join(frase) => Juntara todos elementos da frase separando com '-'.
