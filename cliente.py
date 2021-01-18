import rpyc
import time
from constRaiz import *

class Cliente:
    conn_server = rpyc.connect(RAIZ_SERVER, RAIZ_PORT) #Conecta com o servidor raiz
    print("Conectando com o servidor raiz...")
    time.sleep(2)
    z = False
    while z == False:
        x = input("Digite o nome do servidor que você quer acessar: ")
        print("Fazendo a pesquisa no servidor raiz")
        time.sleep(2)
        z = conn_server.root.exposed_lookup(x) #faz o lookup no servidor de diretorio
        if z == False:
            print("O Nome não foi encontrado, por favor tente novamente.")


    print("Foi encontrado o servidor de aplicação")
    ip = z[0]
    porta = z[1]
    print (f'Endereço: {ip} Porta: {porta}') #após receber o endereço e porta ele imprime apenas para o conhecimento
    
    print("Usando os dados para se conectar no servidor de aplicação")
    time.sleep(2)
    conn_app = rpyc.connect(ip, porta) #Usa o endereço IP e porta recebidos para se conectar ao servidor de aplicação
    print("Conexão realizada com sucesso")
    time.sleep(2)
    print("Finalizando cliente...")
    time.sleep(2)
