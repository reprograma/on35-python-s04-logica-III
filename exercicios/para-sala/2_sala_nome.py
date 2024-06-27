# Exercício de Sala 🏫  

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def solicitar():
  usuario = input('Digite seu usuário: ')  
  usuario_maiusc = usuario.upper()
  
  usuario_senha(usuario_maiusc)

def usuario_senha(nome):
  
  senha_cadastro = input('Digite sua senha: ')
  senha_maiusc = senha_cadastro.upper()
  
  while senha_maiusc == nome:
    senha = input('A senha nao pode ser igual ao nome do usuario.\nDigite uma senha válida: ')
    senha_maiusc = senha.upper()
  print('Usuário cadastrado com sucesso!')

solicitar()


#-----------------------------------------


def solicitar():
  usuario = input('Digite seu usuário: ')  
  usuario_maiusc = usuario.upper()
  
  usuario_senha(usuario_maiusc)

def usuario_senha(nome):
  
  senha = input('Digite sua senha: ')
  senha_maiusc = senha.upper()
  
  while senha_maiusc in nome or nome in senha_maiusc or "*" in senha:
    senha = input('A senha nao pode ser igual ao nome do usuario.\nDigite uma senha válida: ')
    senha_maiusc = senha.upper()
  print('Usuário cadastrado com sucesso!') 


solicitar()