##* Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("insira seu usuário: ")
senha = input("insira sua senha: ")

while usuario == senha or usuario in senha or senha in usuario:
    print("erro o usário e senha não são validos")
    usuario = input("insira seu usuario: ")
    senha = input("insira sua senha: ")
