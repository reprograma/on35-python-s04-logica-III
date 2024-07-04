 #Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario  = (input('Insira o seu usuário' ' ')) 
senha = (input ('Insira sua senha' ' ')) 

while usuario == senha:
    usuario = (input('O login e a senha não podem ser iguais! \n Insira o seu usuário novamente:' ' '))
    senha = (input ('Insira sua senha novamente:' ' '))


