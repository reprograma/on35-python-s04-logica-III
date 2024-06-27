print("Faça seu cadastro:")
usuario = input("Usuário: ")
senha = input("Senha: ")

while usuario == senha:
    print("A senha não pode ser igual ao usuário. Preencha valores diferentes.")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

print("Legal! Cadastro concluído!")
