# Exercício de Sala 🏫  

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# While
def zero_a_dez (num):    
  while num <0 or num > 10:
    num = int(input('Digite um número válido: '))
  return f'A nota digitada foi: {num}!'

def solicita():
  try:  
    nota = int(input('Digite uma nota entre 0 e 10: '))
    resultado_nota = zero_a_dez(nota)
    return resultado_nota
  except:
    return 'Digite um número inteiro entre 0 e 10!'

print(solicita())