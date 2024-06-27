# * A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

fibonacci = int(input('Insira o número para gerar a Sequência de Fibonacci: '))

primeiro = 0
segundo = 1

if (fibonacci == 1) or (fibonacci == 2):
    print('1')
else:
    for sequencia in range(2,fibonacci):
        n_termo = primeiro + segundo
        segundo = primeiro
        primeiro = n_termo
        sequencia += 1
        print(n_termo, end=', ')
    else:
        print(end='...')
