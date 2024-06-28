# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
#  e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.
def calcular_colecao_cds():
  """
  Função para calcular o valor total e médio de uma coleção de CDs.

  Retorna um dicionário com as seguintes chaves:
    'total': Valor total investido na coleção (float)
    'media': Valor médio gasto por CD (float)
  """

  # Inicialização de variáveis
  total = 0
  cont = 0

  # Solicita ao usuário a quantidade de CDs
  quantidade = int(input("Digite a quantidade de CDs na coleção: "))

  # Loop para iterar sobre cada CD
  for _ in range(quantidade):
    valor_cd = float(input(f"Digite o valor do CD {cont + 1}: "))
    total += valor_cd
    cont += 1

  # Cálculo do valor médio
  media = total / cont

  # Retorna um dicionário com os resultados
  return {'total': total, 'media': media}

# Chamada da função e exibição dos resultados
resultado = calcular_colecao_cds()

print(f"Valor total investido: R${resultado['total']:.2f}")
print(f"Valor médio por CD: R${resultado['media']:.2f}")
