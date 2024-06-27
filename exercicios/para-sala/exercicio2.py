#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha seja igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Crie um usuário: ")
senha = input("Crie uma senha: ")

while usuario in senha or senha in usuario:
    print("A senha não pode ser o valor do usuário, gentileza criar nova senha.")
    usuario = input("Crie um usuário: ")
    senha = input("Crie uma senha: ")

print("Parabéns, seu cadastro foi realizado!")
    