#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a sua senha: ")

while usuario == senha:
  print ("Erro! A senha não pode ser a mesma que o nome do usuário. Digite novamente")
  senha = input("Digite a sua senha novamente: ")