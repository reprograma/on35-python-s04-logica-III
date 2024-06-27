#* O cardápio de uma lanchonete é o seguinte:
#   Especificação   Código  Preço
#   Cachorro Quente 100     R$ 1,20
#   Bauru Simples   101     R$ 1,30
#   Bauru com ovo   102     R$ 1,50
#   Hambúrguer      103     R$ 1,20
#   Cheeseburguer   104     R$ 1,30
#   Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

# Definição do cardápio
cardapio = {
    100: {"item": "Cachorro Quente", "preco": 1.20},
    101: {"item": "Bauru Simples", "preco": 1.30},
    102: {"item": "Bauru com ovo", "preco": 1.50},
    103: {"item": "Hambúrguer", "preco": 1.20},
    104: {"item": "Cheeseburguer", "preco": 1.30},
    105: {"item": "Refrigerante", "preco": 1.00}
}

total_geral = 0
pedidos = []


while True:
    print('-'*40)
    print('  Especificação   |', ' Código | ', ' Preço ')
    print('-'*40)
    print('  Cachorro Quente |', '  100   |', ' R$ 1,20')
    print('   Bauru Simples  |', '  101   |', ' R$ 1,30')
    print('   Bauru com ovo  |','  102   |', ' R$ 1,50')
    print('    Hambúrguer    |','  103   |', ' R$ 1,20')
    print('   Cheeseburguer  |','  104   |', ' R$ 1,30')
    print('   Refrigerante   |', '  105   |', ' R$ 1,00')
    print('-'*40)

    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))

    if codigo == 0:
        break
    elif codigo in cardapio:
        quantidade = int(input(f"Quantos {cardapio[codigo]['item']} você deseja? "))
        valor = cardapio[codigo]['preco'] * quantidade
        total_geral += valor
        pedidos.append((cardapio[codigo]['item'], quantidade, valor))
    else:
        print("Código inválido. Tente novamente.")


print("\nResumo do pedido:")
for item, quantidade, valor in pedidos:
    print(f"{item}: {quantidade} x R$ {valor/quantidade:.2f} = R$ {valor:.2f}")

print(f"\nTotal geral: R$ {total_geral:.2f}")
