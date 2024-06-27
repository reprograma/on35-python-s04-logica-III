#Exercício de Casa 🏠 Grupo 1 - Atividade números em vertical e horizontal de 1 a 20. 
#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os
# números um ao lado do outro.

def main():
    for i in range(1, 21):
        print(i)

if __name__ == "__main__":
    main()


def main():
    for i in range(1, 21):
        print(i, end=' ')

if __name__ == "__main__":
    main()