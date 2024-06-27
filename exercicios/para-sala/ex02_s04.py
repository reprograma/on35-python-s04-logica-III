#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input("Coloque seu nome de usuário: "))
senha = str(input("Coloque sua senha: "))

while usuario in senha or senha in usuario:    # usuario == senha usuário igual a senha
        print ("A senha inválida, tente novamente")
        usuario = str(input("Coloque seu nome de usuário: "))
        senha = str(input("Coloque sua senha: "))
else:
        print ('Usuário e senha criados com sucesso')