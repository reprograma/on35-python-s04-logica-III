# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


usuario = ("")
senha = ("")

while (usuario == senha):
    print ("A sua senha não pode conter seu nome")

    usuario = input("insira seu nome usuario: ")
    senha = input("insira sua senha: ")

print("Logado")