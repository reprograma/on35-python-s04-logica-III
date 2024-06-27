nota = float(input("Insira uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota inválida, digite outra nota por favor: "))
    
print(f"A nota {nota} é válida")
    
    