def cacavogais():
    i = 0
    j = 0
    string = str (input("Digite alguma coisa: "))
    for i in string:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
             j+=1
    print("vogais: ", j)

cacavogais()