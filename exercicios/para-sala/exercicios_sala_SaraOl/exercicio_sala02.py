# * Faça um programa que leia um nome de usuário e a
# sua senha e não aceite a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informações.

entrada_dados = {}

def confere_dados():
    nome_de_usuario = input('Digite seu nome de usuario(a): ')
    senha = input('Insira sua senha: ')
    entrada_dados.update({nome_de_usuario: senha})

    for chave, valor in entrada_dados.items():
        if chave == valor:
            print('Esse tipo de senha não é permitida!\nPor favor, redefina uma nova senha')
            nome_de_usuario = input('Digite seu nome de usuario(a): ')
            senha = input('Insira sua senha: ') 
    else:
        return 'Acesso permitido, seja bem-vinde!'
    
print(confere_dados())