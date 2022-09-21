# -*- coding: utf-8 -*-
'''
Bingolite
Universidade Presbiteriana Mackenzie
Ciência da Computação 
Turma 2D

Autores:
Gustavo Vilela Mitraud TIA: 32213611
Joao Lucas Macedo de Melo TIA: 
    
TODO
nada
'''

import funcs

def main():
    
    print('''
**************************** BINGOLITE ******************************
----criado por Gustavo Vilela Mitraud e Joao Lucas Macedo de Melo----''')
    print("\n")
        
    rodando_main = True
    while rodando_main: 
        arq = input("entre com o nome do arquivo com as cartelas: ")
        hall = open("hall.txt", "w")
        loop_cartelas = True
        
        try:
            arq = open(arq, "r")
        except FileNotFoundError:
            print("arquivo não encontrado ou não existe")
            continue
        

        # criando a lista com todas as cartelas e selecionando 4 entre elas
        
        linhas = arq.readlines()
        LISTA_CARTELAS = funcs.criarListaCartela(linhas)
        
        cartelas = funcs.randCartela(LISTA_CARTELAS)
        
        cur = 0
        answer = ""
    
        sorteado = funcs.sortearNumero()
        iter_sort = 0
        verdadeiros = []
        
        print("cartelas sorteadas: \n")

        vencedora = -1

        bool_cartelas = [[False]*5,[False]*5,[False]*5,[False]*5,[False]*5]


         # loop do jogo
        while loop_cartelas: 
            
            
            
            print(f'''******NUMERO SORTEADO: {sorteado[iter_sort]}******''')
            if answer != "":
                try:
                    # Aqui estamos checando para ver se é possivel converter o valor de answer para int
                    # Caso não, é chamado ValueError
                    # Caso sim, é feito mais um cheque para ver se o valor de answer é menor que o tamanho de cartelas sorteadas
                    # Caso sim, é chamado ValueError
                    
                    answer = int(answer) 
                    if answer > len(cartelas) :
                        raise ValueError
                except ValueError:
                    answer = input("numero invalido, digite um novo numero: ")
                    continue
                
                cur = answer - 1
                
                print("\n")    
                
            # A performance da seguinte parte do algoritmo é bem lenta, pois existêm varios for dentro de um for grande
            # Mas a parte de checar se os numeros das cartelas são iguais ao sorteado é bem complexa e o grupo não sabe como melhorar a performance 
            
            for i in range(4):
                if i == cur:
                    print(f"***cartela {i+1}*** -- ", end=" ")
                else:
                    print(f"cartela {i+1} -- ", end=" ")
                    
                # Aqui estamos guardando os numeros de todas as cartelas que são iguais ao numero sorteado num vetor chamado verdadeiros
                
                for j in range(len(cartelas[i])): #Assumindo que todas as cartelas tem o mesmo tamanho
                    if int(cartelas[i][j]) == sorteado[iter_sort]:
                        verdadeiros.append(cartelas[i][j])
                        bool_cartelas[i][j] = True
                    
                                
                # Aqui estamos checando se o numero atual da cartela atual é igual a algum numero do vetor verdadeiros, se sim, é printado de uma forma diferente
                for n in range(len(cartelas[i])):
                    desigual = ""
                    for m in range(len(verdadeiros)):
                        if cartelas[i][n] == verdadeiros[m] and cartelas[i][n] != desigual:
                            print(f"**{cartelas[i][n]}**", end=" ")
                            desigual = cartelas[i][n]

                            
                    if cartelas[i][n] != desigual:
                        print(f"{cartelas[i][n]}", end=" ")
                    
                print("\n")
        
            
                if all(bool_cartelas[i]):
                    vencedora = i
                
            
            
                    
            iter_sort += 1

            if vencedora != -1:
                print(f"*****CARTELA VENCEDORA: CARTELA {vencedora+1}*****")
                funcs.printarCartelas(cartelas[vencedora])
                print("\n")

                if vencedora == cur:
                    print("PARABENS, VOCÊ VENCEU!!")
                    nome = input("digite seu nome para o hall de vencedores:")
                    hall.write(nome)
                else:
                    print("DESCULPE, VOCÊ PERDEU")

                while True:
                    try:
                        continuar = int(input("deseja jogar denovo? (sim: 1, não = 0)"))
                        break
                    except ValueError:
                        print("resposta invalida, digite uma resposta valida")

                if continuar == 1:
                        loop_cartelas = False
                    
                else:
                    loop_cartelas, rodando_main = False, False 
            else:
                answer = input("Selecione a proxima cartela(só aperte enter caso não queira trocar): ")

    arq.close()
    hall.close()

if __name__ == "__main__":
    main()