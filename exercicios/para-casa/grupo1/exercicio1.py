#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidatos = ["Zoela", "Matteo", "Azzaro"]
eleitores = int(input("Insira a quantidade total de eleitores: "))
votos = []

for contagem in range (eleitores):
    print(f"total de eleitores de {eleitores}")
    voto = input("Insira o nome do seu candidato considerando as opções abaixo: \n Zoela \n Matteo \n Azzaro \n ").lower()
    votos.append(voto)
   

votos_Zoela = votos.count("zoela")
votos_Matteo = votos.count("matteo")
votos_Azzaro = votos.count("azzaro")

print (f"A quantidade de votos foi \nZoela teve {votos_Zoela}\nMatteo teve {votos_Matteo} \nAzzaro teve {votos_Azzaro}")