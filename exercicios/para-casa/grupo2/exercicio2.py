# * A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

numero = range (1, 91)
contagem = 1
 
for conta in numero:
    conta = (contagem + conta)
    print (conta)
