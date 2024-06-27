nota = int(input("Coloque uma nota entre 0 e 10: "))
while not nota in range(11):     # nota != range:
    print("Nota inválida") 
    nota = int(input("Coloque uma nota entre 0 e 10: "))
print (f"Sua nota é {nota}")