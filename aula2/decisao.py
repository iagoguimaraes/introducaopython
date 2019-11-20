def ex_16():    
    primeiro_numero = float(input('Digite um número: '))
    segundo_numero = float(input('Digite outro número: '))

    if(primeiro_numero > segundo_numero):
        print('O número {} é maior.'.format(primeiro_numero))  
    elif(segundo_numero > primeiro_numero): 
        print('O número {} é maior.'.format(segundo_numero))
    else:
        print('Os números {0} e {1} são iguais.'.format(primeiro_numero, segundo_numero))

def ex_17(numero):
    if (float(numero) < 0):
        print('O número {} é negativo.'.format(numero))
    elif(float(numero) > 0):
        print('O número {} é positivo.'.format(numero))
    else:
        print('Você digitou {}.'.format(numero))

def ex_19(letra):
    if(letra.isalpha()):
        vogais = ['A', 'E', 'I', 'O', 'U']

        print('{} é uma vogal.'.format(letra)) if letra.upper() in vogais else print('{} é uma consoante.'.format(letra))
    else:
        print('Letra inválida.')


def run():
    ex_16()
    ex_17(input('Digite um número: '))
    ex_19(input('Digite uma letra: '))
