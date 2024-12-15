## Grupo 2
# *Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

numero_tabuada = int(input("Qual tabuada você quer estudar agora? Me diz um número entre 1 e 10-> "))

for gerador_tabuada in range (1, 11):
    numero_multiplicado = int(input("E qual número você quer multiplicar? Valendo apenas valores entre 1 e 10 -> "))
    if numero_tabuada <= 10 and numero_multiplicado <= 10:
        resultado = numero_multiplicado * numero_tabuada
        print(f"{numero_tabuada} x {numero_multiplicado} = {resultado}")
    else:
        print("Esse não é um número váido para nossa tabuada")
        break

#* A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


#* O cardápio de uma lanchonete é o seguinte:

#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00

#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
