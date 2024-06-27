maior_numero = 0
for numeros in range (5):
    numero = int(input(f"Insira um novo numero para analise: "))
    if numero > maior_numero:
        maior_numero = numero

print (f"Maior numero da lista: {maior_numero}")