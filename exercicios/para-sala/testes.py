contador = 0

while contador <= 5:
    print(contador)
    contador = contador + 1

macas = 10

while macas > 0:
    print("Comi uma maca")
    
    macas = macas - 1
    print(f"Tenho {macas} macas")
else:
    print("Acabaram as macas")

# ele gera um range de numeros, como se fosse uma lista que indica esses numeros. No caso do exemplo está 1- onde inicia, 6- onde finaliza 
# termina no 5, o limite é sempre no numero anterior a esse. O 2- indica que ele ta pulando e mostrando de 2 em 2 no terminal.
# iterador = 0 identifica o valor inicial

iterador = 0

for iterador in range (1,6,2):
    print (iterador)


animais = ["gatos", "cachorro", "periquito"]
for animais in animais:
    print(animais)

notas = [10, 5, 7, 8]
soma_notas = 0

for nota in notas:
    soma_notas = soma_notas + nota
else:
    media = soma_notas / len(notas)
    print(media)


# novo exemplo, no caso do break ele para o looping, se for o continue ele continua mesmo que ja tenha encontrado o que precisava.
# o continue ele passa todos os itens da lista, ele continua executando e o break para na rodada.

animais_de_estimacao = ["cachorro", "gato", "cobra"]

for animais in animais_de_estimacao:
    if animais == "gato":
        print ("você tem gato")
        break
    print(f"Esse animal não é um gato, é um {animais}")
else:
    print("Poxa, você não tem um gato")

adolescentes = [17, 12, 19, 20, 12]

for adolescente in adolescentes:
    if adolescente >= 18:
        print("Você pode entrar")
    elif adolescente < 18 and adolescente >= 15:
        print("Logo você podera entrar")
    else:
        print("Epa vai todo mundo pra casa")
    break

# continue pula a instrução atual e segue para próxima
# break ele para na condição inicial
# else do loop: sempre vai acontecer no final do loop, sempre acontece depois que todas as interações aconteceram, é uma conclusão.

roupas = {
    "casaco": {
        "cor": "amarelo",
        "tamanho": "G"
    },
    "calca": {
        "cor": "bordô",
        "tamanho": "G"
    }
}
{"cor": "amarelo"}
for nome_roupa, roupa in roupas.items():
    print(nome_roupa + ":")
    for nome_caracteristica, caracteristica in roupa.items():
        print(f"{nome_caracteristica}: {caracteristica}")

# primeiro é a chave e o segundo é o valor quando é olhado para as condições de casaco, por exemplo.
# nome roupa - calça ou casaco
# roupa - dicionario que está dentro dessa chave

