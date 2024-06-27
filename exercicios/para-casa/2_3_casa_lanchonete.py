# Exercício de Casa - Grupo 2🏠

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
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

def solicita_qtd():
  try:
    print('Especificação    Código    Preço')
    print('Cachorro Quente   100     R$ 1,20')
    print('Bauru Simples     101     R$ 1,30')
    print('Bauru com ovo     102     R$ 1,50')
    print('Hambúrguer        103     R$ 1,20')
    print('Cheeseburguer     104     R$ 1,30')
    print('Refrigerante      105     R$ 1,00')

    qtd_vezes = int(input('Quantidade de pedidos: '))
    preco_pagar = valor_total(qtd_vezes)
    return preco_pagar
  
  except:
    print('Digite uma quantidade válida!')

def valor_total(qtd_vezes):

  preco_total = 0

  for i in range(1,qtd_vezes+1):

    cod_100 = 1.2
    cod_101 = 1.3
    cod_102 = 1.5 
    cod_103 = 1.2
    cod_104 = 1.3 
    cod_105 = 1 

    

    qtd_pedido = int(input(f'Quantidade do {i}º pedido: '))
    codigo = int(input(f'Código do {i}º pedido: '))
    
    if codigo == 100 or codigo == 101 or codigo == 102 or codigo == 103 or codigo == 104 or codigo == 105:
      if codigo == 100:
        preco_cod_100 = cod_100 * qtd_pedido
        preco_total = preco_total + preco_cod_100
      elif codigo == 101:
        preco_cod_101 = cod_101 * qtd_pedido
        preco_total = preco_total + preco_cod_101
      elif codigo == 102:
        preco_cod_102 = cod_102 * qtd_pedido
        preco_total = preco_total + preco_cod_102
      elif codigo == 103:
        preco_cod_103 = cod_103 * qtd_pedido
        preco_total = preco_total + preco_cod_103
      elif codigo == 104:
        preco_cod_104 = cod_104 * qtd_pedido
        preco_total = preco_total + preco_cod_104
      else:
        preco_cod_105 = cod_105 * qtd_pedido
        preco_total = preco_total + preco_cod_105
    else:
      print('Digite um código válido!')
      break
    i = i + 1

  print(f'Valor a pagar: R${preco_total:.2f}')  

solicita_qtd()