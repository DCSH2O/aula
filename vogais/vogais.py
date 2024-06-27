#Função cacavogais(): Essa função conta o número de vogais 
# em uma string (sequência de caracteres) digitada pelo usuário.
#

def cacavogais():
    #Variáveis:

# i: um contador que itera sobre cada caractere da string.
# j: um contador que soma o número de vogais encontradas.
# string: a string digitada pelo usuário.

    i = 0
    j = 0

    
    string = str (input("Digite alguma coisa: "))
#A função pede ao usuário que digite uma string
#  com input("Digite alguma coisa: ").



    for i in string:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
             j+=1
    print("vogais: ", j)
#Em resumo, a função cacavogais() conta o número de vogais em uma string digitada pelo usuário e imprime o resultado.
cacavogais()