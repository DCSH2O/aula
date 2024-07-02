



def saudacao():
    print('Olá, seja bem vindo(a) Digite sua nota de 1 a 10!')

saudacao()

def soma (a,b):
    a= int(input("Nota 1:"))
    b = int(input("Nota 2:"))
    nota= 8
    
    resultado= a+b
    print(f"valor {resultado} esperado")
    
    if nota<=resultado:
        print("Seu Time é Azul")
        
    else:
        print("Seu time é Vermelho")

    return resultado

print(soma(0,0))

