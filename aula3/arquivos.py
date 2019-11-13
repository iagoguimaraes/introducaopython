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

def ex_2():
    usuarios = open('aula3/resources/usuarios.txt', 'r')
    relatorio = open('aula3/output/relatorio.txt', 'w')

    tamanho_total = 0
    cont_usuarios = 0

    vet_dados_usuario = []

    #preenche os vetores
    for dados_usuario in usuarios:
        nome_usuario = str(dados_usuario).split(' ')[0]
        tamanho_dir = str(dados_usuario).split(' ')[1].replace('\n', '')
        
        cont_usuarios = cont_usuarios + 1

        vet_dados_usuario.append([cont_usuarios, nome_usuario, tamanho_dir])

    #calcula o tamanho total
    for tamanhos in vet_dados_usuario:
        tamanho_total = tamanho_total + int(tamanhos[2])

    #printa o relatorio
    print('ACME Inc. Uso do espaço em disco pelos usuários')
    print('---------------------------------------------------------')
    print('Nr.  Usuário Espaço Utilizado    % do uso')
    
    for usr in vet_dados_usuario:

        tamanho_mb = int(usr[2]) / 1000000
        porcent_tamanho = ((100 * int(usr[2])) / tamanho_total)
    
        print('{0}  {1} {2:.2f} MB  {3:.2f}%'.format(usr[0], usr[1], tamanho_mb, porcent_tamanho).replace('.', ','))


def run():
    ex_1()
    
ex_2()