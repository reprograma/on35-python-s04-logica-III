#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
input("eleição do grêmio escolar para presidente")
candidatos = ["choso", "mahitto", "satoro"]
eleitores = int(input("Insira a quantidade total de eleitores: "))
votos = []

for contagem in range (eleitores):
    print(f"total de eleitores de {eleitores}")
    voto = input("Insira o nome do seu candidato considerando as opções abaixo: \n Choso \n Mahitto \n Sataro \n ").lower()
    votos.append(voto)
   

votos_choso = votos.count("choso")
votos_mahitto = votos.count("mahitto")
votos_satoro = votos.count("satoro")

print(f"A quantidade de votos foi \nchoso teve {votos_choso}\nmahitto teve {votos_Mahitto} \nsatoro teve {votos_satoro}")