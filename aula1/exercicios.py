def desafio_1():
    txt = open("aula1/resources/desafio1.txt").read()
    for x in txt:
        print(chr(ord(x) if ord(x)+2 < ord('a') else  ord(x)+2 if ord(x)+2 < ord('z') else ord(x)-24), end="")


def desafio_2():
    txt = open("aula1/resources/desafio2.txt").read()
    ltt = 'abcdefghijklmnopqrstuvwxyz'
    for a in txt:
        if (a in ltt):
            print(a, end="")