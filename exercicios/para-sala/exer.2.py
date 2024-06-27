# * Faça um programa que leia um nome de usuário e a sua senha e não aceite 
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = input("Insira o nome do usuário: ")
senha_usuario = input("Insira a senha do usuário: ")

while nome_usuario == senha_usuario:
        print("Usuário e senha iguais, favor, digitar novamente.")
        nome_usuario = input("Insira o nome do usuário: ")
        senha_usuario = input("Insira a senha do usuário: ")

print("Acesso criado - Válido.")
        
        

