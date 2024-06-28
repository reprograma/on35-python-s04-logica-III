#  O cardápio de uma lanchonete é o seguinte:
# ```
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# ```
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.


produtos = {

    "100": [1.20],
    "101": [1.30],
    "102": [1.50],
    "103": [1.20],
    "104": [1.30],
    "105": [1.00]

}

cardapio = int(input(f"Insira aqui o código do produto {produtos} , ou digite 0 para sair "))
quantidade = float(input(f"Insira aqui a quantidade do produto "))

while (cardapio != 0):
    print(float(input(f"O valor a ser pago é de {cardapio * quantidade}")))
    cardapio = int(input(f"Insira aqui o código do produto "))
    quantidade = float(input(f"Insira aqui a quantidade do produto "))
    
    
resultado = cardapio * quantidade
print(f"O valor a ser pago é de {resultado}")

  



