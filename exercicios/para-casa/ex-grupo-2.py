#exercício tabuada 

numero = int(input("Informe um número para a tabuada entre 1 e 10: "))
if numero < 1 or numero > 10:
    raise ValueError("Número inválido. Por favor, insira um número entre 1 e 10.")

print(f"Esta é a tabuada de {numero}:")
for iterador in range(1, 11):
    resultado = numero * iterador
    print(f"{numero} X {iterador} = {resultado}")


#exercício cardápio


cardapio = {
    100: {"Lanche": "Cachorro Quente", "Preço": 1.20},
    101: {"Lanche": "Bauru Simples", "Preço": 1.30},
    102: {"Lanche": "Bauru com ovo", "Preço": 1.50},
    103: {"Lanche": "Hambúrguer", "Preço": 1.20},
    104: {"Lanche": "Cheeseburguer", "Preço": 1.30},
    105: {"Lanche": "Refrigerante", "Preço": 1.00}
}


total_do_pedido = 0.0

print("Olá, seja bem vinde à Comidas da Ka!")
print("")


print("Bem-vindo(a) à Lanchonete!")
print("Quando encerrar o pedido, digite 0.")

while True:
    try:
        codigo = int(input("Digite o código do item desejado: "))
        
        if codigo == 0:
            break
        elif codigo not in cardapio:
            print("Código inválido. Por favor, digite um código válido.")
            continue
        
        quantidade = int(input(f"Digite a quantidade de '{cardapio[codigo]['Lanche']}' desejada: "))
        
        preco_unitario = cardapio[codigo]["Preço"]
        valor_pago = preco_unitario * quantidade
        total_do_pedido += valor_pago
        
        
        print(f"Valor a ser pago por '{cardapio[codigo]['Lanche']}': R$ {valor_pago:.2f}")
    
    except ValueError:
        print("Erro: por favor, digite um número inteiro válido para o código e a quantidade.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


print(f"Total geral do pedido: R$ {total_do_pedido:.2f}")
print("Obrigado(a) por utilizar nossos serviços. Volte sempre!")
