# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
# de erro e voltando a pedir as informações.


usuario = input("Por gentileza, insira o seu nome de usuário: \n")
senha = input("Por gentileza, insira a sua senha: \n")

while usuario in senha or senha in usuario or "*" in senha:
    print("Nome usuário ou senha inválido, por gentileza, tente novamente.")

    usuario = input("Por gentileza, insira o seu nome de usuário: \n")
    senha = input("Por gentileza, insira a sua senha: \n")
    
print("Usuário e senhas, válidos.")  

