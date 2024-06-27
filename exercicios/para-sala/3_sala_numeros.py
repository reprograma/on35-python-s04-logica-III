# Exercício de Sala 🏫  

# Faça um programa que leia 5 números e informe o maior número.

def maior():
  lista = []

  for i in range(5):
    numero = float(input(f'Digite um numero {i+1}º: '))
    lista.append(numero)
  return max(lista)


#-----------------------------------------


def maior_numero():
  maior_numero = 0
  for contador in range (1,6):
    numero = float(input(f'Insira o {contador}º numero: '))
    if numero > maior_numero:
      maior_numero = numero
  print(f'O maior número entre os 5 é: {maior_numero}')

print(maior())

maior_numero()