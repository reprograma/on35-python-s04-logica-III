# Exercício de Casa - Grupo 2🏠

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# ```
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
# ```

def solicita_tabuada():
    try:
        n_tabuada = int(input('Digite o número para tabuada: '))
        t_tabuada = input('Digite a Operação: (+ - * /) ')
        calculo_tabuada = tabuada(n_tabuada, t_tabuada)
        return calculo_tabuada
    except:
        print('Digite um número inteiro válido!')

def tabuada(num_tabuada, tipo_tabuada):
    if tipo_tabuada == '+' or tipo_tabuada == '*' or tipo_tabuada == '-' or tipo_tabuada == '/':
        for i in range(1,11):
            if tipo_tabuada == '*':
                operacao = num_tabuada * i
            elif tipo_tabuada == '+':
                operacao = num_tabuada + i
            elif tipo_tabuada == '-':
                operacao = num_tabuada - i   
            else:
                operacao = (num_tabuada / i) 
                operacao = f'{operacao:.2f}'

            print(f'{num_tabuada} {tipo_tabuada} {i} = {operacao}')

            i = i + 1
    else:
        print('Digite uma operação válida!')

solicita_tabuada()