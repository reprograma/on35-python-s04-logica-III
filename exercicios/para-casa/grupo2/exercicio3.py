#O cardápio de uma lanchonete é o seguinte:
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = {
    100: {'item': 'Cachorro Quente', 'preco': 1.20},
    101: {'item': 'Bauru Simples', 'preco': 1.30},
    102: {'item': 'Bauru com ovo', 'preco': 1.50},
    103: {'item': 'Hambúrguer', 'preco': 1.20},
    104: {'item': 'Cheeseburguer', 'preco': 1.30},
    105: {'item': 'Refrigerante', 'preco': 1.00}
}

itens_pedido =[]
valor_por_itens=[]

pedido_finalizado ="não"

while pedido_finalizado == "não":

    codigo = int(input("Insira o código do produto: "))  
    quantidade = int(input("Insira a quantidade: "))
    valor_item = float(cardapio[codigo]['preco']) * (quantidade)
    itens_pedido.append(codigo),itens_pedido.append({cardapio[codigo]['item']}),itens_pedido.append(quantidade),itens_pedido.append(valor_item)
    valor_por_itens.append(valor_item)
    
    pedido_finalizado = input("Deseja finalizar seu pedido?(sim/não): ").lower()
    if pedido_finalizado == "sim" :
        print(itens_pedido,sep="\n")
        total_do_pedido = sum(valor_por_itens)
        print(f"Pedido finalizado - Valor final R${total_do_pedido:.2f}, Obrigado pela sua compra!")
        break
    



   


