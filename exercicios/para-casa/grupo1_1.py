# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor 
# votar e ao final mostrar o número de votos de cada candidato.

total_eleitores = int(input("Digite o número total de eleitores na secão eleitoral:"))

voto_armazenado_lula1 = 0
voto_armazenado_dilma2 = 0
voto_armazenado_haddad3 = 0

for i in range(total_eleitores):
    print(f"Eleitor {i + 1}, vote com responsabilidade, o país esta em suas mãos: \n")
    
    print("1 - Lula")
    print("2 - Dilma")
    print("3 - Haddad")

    voto = int(input("Seu voto é secreto (meu código não kkkkkk), digite aqui: \n"))

    if voto == 1:
        voto_armazenado_lula1 += 1
    elif voto == 2:
        voto_armazenado_dilma2 += 1
    elif voto == 3:
        voto_armazenado_haddad3 += 1
    else:
        print("Candidato inválido! Vote nas seguintes opções: 1- Lula, 2- Dilma ou 3 - Haddad.")
        # voto = int(input("Seu voto é secreto, digite aqui: \n")) 

    # resultado_eleicao = [armazenado_candidato1, armazenado_candidado2, armazenado_candidado3]
    # vencedor_eleicao = max(resultado_eleicao)


print("\nResultados da eleição:")
print(f"Candidato Lula: {voto_armazenado_lula1} votos")
print(f"Candidato Dilma: {voto_armazenado_dilma2} votos")
print(f"Candidato Haddad: {voto_armazenado_haddad3} votos")





