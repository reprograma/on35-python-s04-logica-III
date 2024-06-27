# Exercício de Casa 🏠 

## Nome do Exercicio

## Grupo 1
# * Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.



candidatos=["Maria","Joao","Jose"]
 
eleitores =int(input("Número de eleitores: "))
candidatos=["Maria","Joao","Jose"]

lista_votos=[]
for eleitor in range(eleitores):
    nome_candidato = input("Escolha um dos três candidato para votar:\n-Maria\n-Jose,\n-Joao\n \n- ").lower()
    lista_votos.append(nome_candidato)
    

votos_maria = lista_votos.count("maria")
print(f"{candidatos[0]}: {votos_maria} voto(s)")

votos_jose = lista_votos.count("jose")
print(f"{candidatos[1]}: {votos_jose} voto(s)")

votos_joao= lista_votos.count("joao")
print(f"{candidatos[2]}: {votos_joao} voto(s)")

if votos_maria > (votos_joao and votos_jose):
    print(f"Maria foi a canditata mais votado com {votos_maria} votos e ganhou a eleição.")
elif votos_joao > (votos_maria and votos_jose):
    print(f"João foi a canditato mais votado com {votos_joao} votos e ganhou a eleição.")
elif votos_jose > (votos_joao and votos_maria):
    print(f"Jose foi a canditato mais votado com {votos_jose} votos e ganhou a eleição.")



