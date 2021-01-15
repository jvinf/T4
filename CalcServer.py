import rpyc
from server_list import *

my_name = 'CalcServer'
my_ip = '192.168.1.11'
my_port = 5001

c = rpyc.connect("localhost", 5000)


registrado = c.root.exposed_register(my_name, my_ip, my_port)


if registrado:
    var = input("Deseja iniciar o servidor? Sim ou Não: ")
    if var.capitalize() == 'Sim':
        print('Server Startado')
    
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(MyServer, port=5001, protocol_config={'allow_public_attrs': True,})
        
        print("O servidor CalcServer foi iniciado e está executando")
        print("Aguardando conexões...")
        t.start()
    else:
        print("Ok!")
