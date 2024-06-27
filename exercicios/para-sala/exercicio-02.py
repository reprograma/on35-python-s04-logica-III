# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Diga o nome de usuário: ")
    senha = input("Informe a senha: ")
    if usuario != senha:
        print("Usuário e senha registrados com sucesso.")
        break
    else:
        print("Erro: a senha não pode ser igual ao nome de usuário. Tente novamente.")