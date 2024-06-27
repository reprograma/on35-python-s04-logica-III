# * Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
# o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

# O usuário inicia informando a quantidade de cds existente na sua coleção
# Em seguida temos a variável vazia para armazenar os preços gastos em cada cd.
total_Cds = int(input('Insira a quantidade total de CDs da sua coleção: '))
total_investimentoCD = 0.0

# O loop for vai solicitar o valor de cada disco na sequência interando cada novo preço dentro da variável
# E depois  a variável media_investimento armazena o resultado dos cálculos.
for conta_cd in range(total_Cds):
    insira_precos = float(input(f"Insira o valor pago pelo CD {conta_cd+1}: "))
    total_investimentoCD += insira_precos

media_investimento = total_investimentoCD / total_Cds

print(f"O valor total investido em sua coleção foi: R${total_investimentoCD}")
print(f"O valor médio investido em sua coleção foi: R${media_investimento}")
