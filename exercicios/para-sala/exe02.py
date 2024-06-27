# Exercício de Sala 🏫  

## Exercicio 2

#* Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

nome_usuario=input('Digite seu nome: ')
senha_usuario=input('Digite sua senha aqui: ')

while nome_usuario==senha_usuario:
    
    if nome_usuario == senha_usuario:
        print('A senha não pode ser igual ao usuario, tente novamente!')

        nome_usuario=input('Digite seu nome: ')
        senha_usuario=input('Digite sua senha aqui: ')
    else:
        print('Usuario e senha corretos')




