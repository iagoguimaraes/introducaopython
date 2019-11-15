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

    lista_ips.close()
    resultado.close()

def converte_bytes(valor_em_bytes):
    #converte bytes em megabytes
    return valor_em_bytes / 1000000

def calcula_percentual(valor_inferior, valor_total):
    #calcula porcentagem do valor passado em relacao ao valor total tambem passado
    return ((100 * valor_inferior) / valor_total)

def ex_2():
    usuarios = open('aula3/resources/usuarios.txt', 'r')
    relatorio = open('aula3/output/relatorio.txt', 'w')

    tamanho_total = 0
    cont_usuarios = 0

    vet_dados_usuario = []

    #preenche os vetores
    for dados_usuario in usuarios:
        #nome_usuario = str(dados_usuario).split(' ')[0]
        nome_usuario = str(dados_usuario)[0:15]
        #tamanho_dir = str(dados_usuario).split(' ')[1].replace('\n', '')
        tamanho_dir = str(dados_usuario)[15:].replace('\n', '')
        
        cont_usuarios = cont_usuarios + 1

        vet_dados_usuario.append([cont_usuarios, nome_usuario, tamanho_dir])

    #calcula o tamanho total
    for tamanhos in vet_dados_usuario:
        tamanho_total = tamanho_total + int(tamanhos[2])

    #printa o relatorio
    relatorio.write('ACME Inc.\t\t\tUso do espaço em disco pelos usuários\n')
    relatorio.write('---------------------------------------------------------\n')
    relatorio.write('Nr.\t\tUsuário\t\t\tEspaço Utilizado\t\t% do uso\n')
    
    for usr in vet_dados_usuario:

        tamanho_mb = converte_bytes(int(usr[2]))
        porcent_tamanho = calcula_percentual(int(usr[2]), tamanho_total)
    
        relatorio.write('{0}\t\t{1}\t{2:.2f} MB\t\t\t\t{3:.2f}%\n'.format(usr[0], usr[1], tamanho_mb, porcent_tamanho).replace('.', ','))
    

    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: {:.2f} MB\n'.format(converte_bytes(tamanho_total)).replace('.', ','))
    relatorio.write('Espaço médio ocupado: {:.2f} MB'.format((converte_bytes(tamanho_total)) / len(vet_dados_usuario)).replace('.', ','))

    usuarios.close()
    relatorio.close()


def run():
    ex_1()
    ex_2()