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