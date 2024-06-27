
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Crie um usuario: ")
senha = input("Crie uma senha: ")

while usuario == senha:
    print ("a senha não pode ser igual ao usuario")
    usuario = input("Crie um usuario")
    senha = input("Crie uma senha")


print("Cadastro realizado com sucesso")


