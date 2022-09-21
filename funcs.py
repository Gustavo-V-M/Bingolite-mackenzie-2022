# -*- coding: utf-8 -*-
"""
Bingolite
Universidade Presbiteriana Mackenzie
Ciência da Computação 
Turma 2D

Autores:
Gustavo Vilela Mitraud TIA: 32213611
João TIA: 
    

"""
import random

def criarListaCartela(linhas):
    # essa funcao cria uma lista com todas as cartelas das linhas
    
    aux = [[]]*len(linhas)
    for i in range(len(linhas)):
        aux[i] = linhas[i].rstrip().split(",")
    
    return aux

def randCartela(lista_cartelas):
    # essa funcao seleciona 4 cartelas e as retorna
    
    aux = [[]]*4
    samples = random.sample(range(len(lista_cartelas)), 4)
    for i in range(len(aux)):
        
        aux[i] = lista_cartelas[samples[i]]
    
    return aux

def trocarCartelas(lista_cartelas, n):
    # essa funcao troca da cartela atual para uma a indicada pelo usuario
    
    return lista_cartelas[n]


def sortearNumero():
    return random.sample(range(1,50), 49)

def printarCartelas(cartela, special=False):
    for i in range(len(cartela)):
        if special == True:
            print(f'''*****{cartela[i]}*****''', end=" ")
        else:
            print(f"{cartela[i]}", end=" ")


    