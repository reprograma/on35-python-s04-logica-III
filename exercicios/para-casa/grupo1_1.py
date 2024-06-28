# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor 
# votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input("Digite o número total de eleitores na secão eleitoral: \n"))

voto_armazenado_lula = 0
voto_armazenado_dilma = 0
voto_armazenado_haddad = 0

for i in range(total_eleitores):
    print(f"Eleitor {i + 1}, vote com responsabilidade, o país esta em suas mãos: \n")
    print("1 - Lula")
    print("2 - Dilma")
    print("3 - Haddad \n")
    voto = int(input("Seu voto é secreto (meu código não kkkkkk), digite aqui: \n"))

    if voto == 1:
        voto_armazenado_lula += 1
    elif voto == 2:
        voto_armazenado_dilma += 1
    elif voto == 3:
        voto_armazenado_haddad += 1
    else:
        print("Candidato inválido! Vote nas seguintes opções: 1- Lula, 2- Dilma ou 3 - Haddad.")
         
print("\nResultados da eleição:")
print(f"Candidato Lula: {voto_armazenado_lula} votos")
print(f"Candidato Dilma: {voto_armazenado_dilma} votos")
print(f"Candidato Haddad: {voto_armazenado_haddad} votos")





