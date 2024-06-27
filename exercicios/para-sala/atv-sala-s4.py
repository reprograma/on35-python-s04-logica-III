## Nome do Exercicio

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Dê uma nota entre 0 e 10 para os nossos serviços: "))

while nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite novamente um número entre 0 e 10.")
    nota = float(input("Dê uma nota entre 0 e 10 para os nossos serviços: "))

print(f"Obrigada, você deu a nota {nota} para os nossos serviços!")


# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


nome_usuario = input("Nome de usuário: ")
senha = input("Senha: ")

while nome_usuario == senha:
    print("Sua senha não pode ser igual ao seu nome de usuário. Por favor, digite uma nova senha.")
    senha = input("Senha: ")

print(f"Obrigada! Usuário e senha cadastrados! :))")


# Faça um programa que leia 5 números e informe o maior número.

maior_numero = float(0)

for iterador in range(1, 6):
    numero = float(input(f"Digite o {iterador}º número: "))
    

    if numero > maior_numero:
        maior_numero = numero


print(f"O maior número digitado é: {maior_numero}")


# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for numero in range(1, 51):
    if numero % 2 != 0:
        print(numero)

