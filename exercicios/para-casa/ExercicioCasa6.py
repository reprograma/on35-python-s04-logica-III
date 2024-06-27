cardapio = {
    100: {"nome": "Cachorro Quente", "preco": 1.20},
    101: {"nome": "Bauru Simples", "preco": 1.30},
    102: {"nome": "Bauru com ovo", "preco": 1.50},
    103: {"nome": "Hambúrguer", "preco": 1.20},
    104: {"nome": "Cheeseburguer", "preco": 1.30},
    105: {"nome": "Refrigerante", "preco": 1.00}
}

totalPedido = 0

while True:
    cod = int(input("Informe o código do item ou 0 para encerrar: "))
    if cod == 0:
        break 
    elif cod in cardapio:
        quantidade = int(input("Informe a quantidade desejada: "))
        precoItem = cardapio[cod]["preco"] * quantidade
        totalPedido += precoItem
        print(f"Valor a ser pago pelo {cardapio[cod]['nome']}: R$ {precoItem:.2f}")
    else:
        print("Código inválido. Tente novamente.")

print(f"Total do pedido: R$ {totalPedido:.2f}")
