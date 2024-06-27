usuario = input("Por gentileza, insira o seu nome de usuário: \n")
senha = input("Por gentileza, insira a sua senha: \n")
while usuario in senha or senha in usuario:
    print("Nome usuário ou senha inválido, por gentileza, tente novamente.")
    usuario = input("Por gentileza, insira o seu nome de usuário: \n")
    senha = input("Por gentileza, insira a sua senha: \n")
    
print("Usuário e senhas, válidos. Logado")