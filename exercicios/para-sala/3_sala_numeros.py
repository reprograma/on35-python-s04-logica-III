# Exercício de Sala 🏫  

# Faça um programa que leia 5 números e informe o maior número.

lista = []

for i in range(5):
  numero = float(input(f'Digite um numero {i+1}º: '))
  lista.append(numero)
print(max(lista))

maior_numero = 0
for contador in range (1,6):
  numero = float(input(f'Insira o numero {contador}: '))
  if numero > maior_numero:
    maior_numero = numero
print(f'O maior número entre os 5 é: {maior_numero}')