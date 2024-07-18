# * O cardápio de uma lanchonete é o seguinte:
# ```
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# ```
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = {
    100: {'item': 'Cachorro Quente', 'preco': 1.20},
    101: {'item': 'Bauru Simples', 'preco': 1.30},
    102: {'item': 'Bauru com ovo', 'preco': 1.50},
    103: {'item': 'Hamburguer', 'preco': 1.20},
    104: {'item': 'Cheeseburguer', 'preco': 1.30},
    105: {'item': 'Refrigerante', 'preco': 1.00}
}

pedido = []

while True:
    codigo = int(input('Digite o código do pedido (ou 0 para fechar): '))
    if codigo == 0:
        break
    elif codigo in cardapio:
        quantidade = int(input(f'Digite a quantidade de {
                         cardapio[codigo]['item']}: '))
        pedido.append((codigo, quantidade))
    else:
        print('Código inválido. Tente novamente')

print('\nResumo do pedido \n')
total = 0
for codigo, quantidade in pedido:
    print(f'{quantidade}x {cardapio[codigo]['item']} ({
          cardapio[codigo]['preco']:.2f}) = R$ {cardapio[codigo]['preco'] * quantidade:.2f}')
    total += cardapio[codigo]['preco'] * quantidade
print(f'\nTotal a pagar = R$ {total:.2f}')
