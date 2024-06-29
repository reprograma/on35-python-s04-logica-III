#* Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

numero_eleitores_inserido = int(input("Quantos eleitores tem essa eleição?"))

def votacao(numero_eleitores):
    for eleicao in range (0, numero_eleitores):
        voto = int(input("Você quer votar no cadidato1, candidato2 ou candidato3? Responda com o número."))
        while not voto in range(1,4):
            print("Voto inválido")
            voto = int(input("Você quer votar no cadidato1, candidato2 ou candidato3? Responda com o número."))
        if voto == 1:
            votos_candidato1 += 1
        elif voto == 2:
            votos_candidato2 += 1
        elif voto == 3:
            votos_candidato3 += 1
        
    print(f"O candidato 1 teve {votos_candidato1}, o candidato 2 teve {votos_candidato2} e o candidato 3 teve {votos_candidato3}")
    
votacao(numero_eleitores_inserido)




#* Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

iterador = 0

for iterador in range (1, 21):
    print(iterador)

for iterador in range (1,21):
    print(iterador, end=" ")




#* Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

total_cds = int(input("Luisa, você tem uma coleção bem legal de CDs, não é? Tu sabe quantos CDs são ao total? "))
valor = []

for valor_cds in range (0, total_cds):
    valor_unidade = float(input("Olha esse CD. Quanto custou esse? "))
    valor.append(valor_unidade)
    valor_investido = sum(valor)
    media_investimento = valor_investido / len(valor)

print(f"Ah, então você investiu o total de R${valor_investido} e a média de invetimento é de R${media_investimento} por CD.")


