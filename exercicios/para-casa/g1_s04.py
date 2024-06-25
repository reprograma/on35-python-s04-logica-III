#*Numa eleição existem três candidatos. Faça um programa que peça o número total 
# de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos 
# de cada candidato.

votos_candidatos = []
eleitores = int(input("Digite o numero de eleitores: "))

for eleitor in range(eleitores):
    voto = int(input ("Digite o numero 1 , 2 ou 3 referente ao candidato em quem quer votar: "))
    if voto== 1:
        votos_candidatos.append(voto) 
        candidato_1 = votos_candidatos.count(1)
    
    if voto==2:
        votos_candidatos.append(voto) 
        candidato_2 = votos_candidatos.count(2)
        
    if voto==3:
        votos_candidatos.append(voto) 
        candidato_3 = votos_candidatos.count(3)   

        # se nao tiver voto como faz pra trazer o zero

print ("Votação encerrada!")

print (f"\nCandidato 1: {candidato_1} voto(s)")
print (f"\nCandidato 2: {candidato_1} voto(s)")
print (f"\nCandidato 3: {candidato_3} voto(s)")











#for eleitor in eleitores:
   # voto = input("insira seu candidato")
    #while not voto in candidatos:
        #voto = input("Candidato invalido, insira outro:")
    
#*Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
#  Depois modifique o programa para que ele mostre os números um ao lado do outro.


#*Faça um programa que calcule o valor total investido por um colecionador em sua coleção 
# de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a 
# quantidade de CDs e o valor para em cada um.