#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Insira o seu usuário: ")
senha = input ("Insira a sua senha: ")


while (usuario == senha):
    print ("Operação inválida! A senha e o usuário não podem ser iguais.")
    usuario = input("Insira o seu usuário: ")
    senha = input("Insira a sua senha: ")

print ("Acesso permitido!")
