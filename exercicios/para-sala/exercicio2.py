# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username == password:
        print("Nome de usuário ou senha incorretos. Tente novamente.")
        continue
    else:
        print("Acesso permitido!")
        break
