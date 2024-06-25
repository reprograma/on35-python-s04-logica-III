# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")

while (nome_usuario == senha):
 print ("Operação inválida!")
 nome_usuario = input("Insira seu usuário: ")
 senha = input("Insira sua senha: ")

print("Acesso permitido!")