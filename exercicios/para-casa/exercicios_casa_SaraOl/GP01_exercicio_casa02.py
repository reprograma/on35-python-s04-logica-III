# * Faça um programa que imprima na tela os números de 1 a 20 um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

# Primeiro laço imprime os números conforme solicitado e o retorno é o padrão na vertical
for umAoVinte in range(1,21):
    print(umAoVinte)

# O segundo laço é parecido com o primeiro, no entanto o comando if verifica os número menores que 20 
# e os printa na horizontal separados por vírgula e espaço.
# Já o else remove a vírgula ao final.
for umAoVinte in range(1,21):
    if umAoVinte < 20:
        print(umAoVinte, end=', ')
    else:
        print(umAoVinte)