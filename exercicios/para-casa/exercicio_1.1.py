# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 

total_eleitoras = int(input("Informe o número total de eleitoras:"))
candidatas = ["Ana", "Bia", "Clara"]

votos = {
    "Ana": 0,
    "Bia": 0, 
    "Clara": 0}

for eleitora in range (total_eleitoras):
    print(f"Eleitora {eleitora +1}:")
    voto = (input("Insira a sua candidata: "))
    if voto in candidatas:
        votos[voto] += 1
    else:
        print("Candidata inválida. Por favor, insira um nome válido.")

print("\nResultado da eleição:")
for candidata, num_votos in votos.items():
    print(f"{candidata}: {num_votos} votos")
   


