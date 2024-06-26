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
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

print('\n| COD |     PRODUTO     | VALOR | \n| 100 | Cachorro quente | 1,20R$| \n'
      '| 101 | Bauru Simples   | 1,30R$|\n| 102 | Bauru com ovo   | 1,50R$|\n| 103 | Hamburguer      | 1,20R$| \n'
      '| 104 | Chessburguer    | 1,30R$|\n| 105 | Refrigerante    | 1,00R$|\n'
      '\n Para sair digite 999')
total = 0
while True:
    produto = int(input('Informe o codigo: '))
    if(produto == 999):
        break
    qtd = int(input('Informe a quantidade: '))
    if produto == 100:
        total = 1.20 * qtd
    elif produto == 101:
        total = 1.30 * qtd
    elif produto == 102:
        total = 1.50 * qtd
    elif produto == 103:
        total = 1.20 * qtd
    elif produto == 104:
        total = 1.30 * qtd
    elif produto == 105:
        total = 1 * qtd
    else:
        print('Codigo invalido')
print(f'Você deve pagar {total} reais')