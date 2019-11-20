def ex_16():    
    primeiro_numero = float(input('Digite um número: '))
    segundo_numero = float(input('Digite outro número: '))

    if(primeiro_numero > segundo_numero):
        print('O número {} é maior.'.format(primeiro_numero))  
    elif(segundo_numero > primeiro_numero): 
        print('O número {} é maior.'.format(segundo_numero))
    else:
        print('Os números {0} e {1} são iguais.'.format(primeiro_numero, segundo_numero))


def run():
    ex_16()

run()

