# Faça um programa que calcule o valor total investido por um colecionador em sua 
# coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

total_cd = int(input("Quantos CDs foram comprados no total? "))
lista = []
soma = 0
controle = 1

for preco in range(total_cd):
    preco_CD = float(input("Quanto custou esse CD? "))    
    
    while preco_CD <= 0:
        print("Valor inválido! Insira novamente o valor: ")
        preco_CD = float(input("Responda novamente. Qual o valor do CD? "))

    print(f"Foi adicionado o valor de {preco_CD} no CD {controle}")
    
    lista.append(preco_CD)
    soma = soma + preco_CD
    controle = controle + 1
    
media = soma / preco_CD

print(f"Os valores de cada CD são: \n",lista)
print(f"O valor médio gasto em cada CD é de {media:.2f} reais.")
print(f"O valor total investido na coleção é de {soma} reais")