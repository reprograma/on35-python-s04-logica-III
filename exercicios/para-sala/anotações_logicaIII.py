
#loop while
contador = 0

while contador <= 5:
    print(contador)
    contador = contador + 1

#while com else
maçãs = 10

while maçãs > 0:
    print("Comi uma maçã")
    maçãs = maçãs - 1
    print(f"tenho {maçãs} maçãs")
else:
    print("Acabaram as minhas maçãs :/")

#loop for + range

iterador = 0

for iterador in range(10,-1,-2):
    print(f"Dei dois passos agora estou no {iterador}")

#loop for

#loop for para printar apenas um elemento de lista
podium = ["primeiro lugar: joanna", "segundo lugar: camila", "terceiro lugar: theodoro"]
contador = 0
for competidor in podium:
    contador = contador + 1
    if contador != 3:
        continue
    print(competidor)

perfil = {
"nome" : "Xainã",
"sobrenome" : "França",
"Idade" : "24",
"cidade" : "Recife"
}

for nome_info, info in perfil.items():
    print(nome_info + ': ' + info)


animais = ["cachorro", "gato", "cobra","elefante", "papagaio", "gato", "gato"]
numero_de_gatos = 0

for animal in animais:
    if animal == "gato":
       numero_de_gatos = numero_de_gatos + 1
print(f"Você tem {numero_de_gatos} gato(s)")



roupa_xaina = {
    "blusa": {
        "cor":"marrom",
        "tamanho" : "g"
    },

    "short": {
        "cor":"listrado",
        "tamanho":"p"
    }
}

for nome_de_roupa, roupa in roupa_xaina.items():
    print(nome_de_roupa + ":")
    for caracteristica in roupa.values():
        print (caracteristica)


#append e updates

perfil = {
"nome": "xai",
"idade": "24"
}
perfil.update({"onde_mora": "Recife"})
print(perfil)


animais = ["cachorro", "gato", "passarinho"]
animais.append("cágado")
tamanho = len(animais)
print(tamanho)


