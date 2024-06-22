#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 1
candidato2 = 2
candidato3 = 3

senha = input("Crie uma senha: ")

while (senha == usuario):
    print("A senha não pode ser o valor do usuário, gentileza criar nova senha.")
    usuario = input("Crie um usuário: ")
    senha = input("Crie uma senha: ")

print("Parabéns, seu cadastro foi realizado!")