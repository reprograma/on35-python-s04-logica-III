# Exercício de Casa - Grupo 1🏠 

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

def solicita ():

    print('-------- Eleições 2024 --------')
    print('--------- Candidatas --------- ')

    try:
        eleitores = int(input('Quantidade de eleitores: '))
        votacao(eleitores)
    except:
        print('Digite um número inteiro!')
        
        
def votacao(qtd_eleitores):

    agnes,gaia,ju = 0,0,0


    for iterador in range(0,qtd_eleitores):

        print('(1) Agnes')
        print('(2) Gaia')
        print('(3) Ju')
        
        candidatas = 0
        
        candidatas = int(input(f'{iterador + 1}º Eleitor - Vote :'))
        if candidatas > 0 and candidatas <=3:
            if candidatas == 1:
                agnes = agnes + 1
            elif candidatas == 2:
                gaia = gaia + 1
            else:
                ju = ju + 1 
        else:
            print('Escolha as opções do painel!')
            break

    iterador += 1    
    
    if iterador == qtd_eleitores:
        if gaia > agnes and gaia > ju:
            print('gaia venceu!')
        elif agnes > gaia and agnes > ju:
            print('agnes venceu!')
        elif ju > agnes and ju > gaia:
            print('ju venceu!')
        elif gaia == agnes and agnes == ju:
            print('Houve empate entre as 3!')
        elif gaia == ju:
            print('Gaia empatou com Ju')
        elif ju == agnes:
            print('Ju empatou com Agnes')
        else:
            print('Gaia empatou com Agnes')


solicita()