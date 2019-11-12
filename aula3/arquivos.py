def ex_1():
    lista_ips = open('aula3/resources/lista_ip.txt', 'r')
    resultado = open('aula3/output/resultado.txt', 'w')

    ip = []
    ips_validos = []
    ips_invalidos = []

    for ip in lista_ips:
        numeros_ip = str(ip.replace('\n', '')).split('.') 
        
        if(len(numeros_ip)) != 4:
            ips_invalidos.append(ip)
        else:
            valido = True
            for numero in numeros_ip:
                if(int(numero) < 0 or int(numero) > 255):
                    valido = False
                
            if(valido):
                ips_validos.append(ip)
            else:
                ips_invalidos.append(ip)
    
    cabecalho_validos = '[Endereços válidos:]' + '\n'
    resultado.write(cabecalho_validos)

    for validos in ips_validos:
        linha_ip_valido = str(validos)
        resultado.write(linha_ip_valido)
    
    cabecalho_invalidos = '\n' + '[Endereços inválidos:]' + '\n'
    resultado.write(cabecalho_invalidos)

    for invalidos in ips_invalidos:
        linha_ip_invalido = str(invalidos)
        resultado.write(linha_ip_invalido)

def run():
    ex_1()

run()