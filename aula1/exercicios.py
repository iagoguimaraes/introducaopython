def desafio_1():
    print('\n Resultado do desafio 1: \n')
    txt = open("aula1/resources/desafio1.txt").read()
    for x in txt:
        print(chr(ord(x) if ord(x)+2 < ord('a') else  ord(x)+2 if ord(x)+2 < ord('z') else ord(x)-24), end="")

def desafio_2():
    print('\n\n Resultado do desafio 2: \n')
    txt = open("aula1/resources/desafio2.txt").read()
    ltt = 'abcdefghijklmnopqrstuvwxyz'
    for a in txt:
        if (a in ltt):
            print(a, end="")
    print("\n")

def run():
    desafio_1()
    desafio_2()