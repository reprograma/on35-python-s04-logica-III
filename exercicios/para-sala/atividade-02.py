#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:

    nome_usuario = input("digitar o nome do usuario: ")
    senha = input("digite uma senha: ")

    if senha == nome_usuario:
     print("senha invalida")

    else:
        print("Cadastro realizado com sucesso!")

    break
