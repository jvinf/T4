import rpyc
from server_list import *

my_name = 'CalcServer'
my_ip = '172.31.16.204'
my_port = 4010

c = rpyc.connect("172.31.91.81", 4001)


registrado = c.root.exposed_register(my_name, my_ip, my_port)


if registrado:
    var = input("Deseja iniciar o servidor? Sim ou Não: ")
    if var.capitalize() == 'Sim':
        print('Server Startado')
    
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(MyServer, port=4010, protocol_config={'allow_public_attrs': True,})
        
        print("O servidor CalcServer foi iniciado e está executando")
        print("Aguardando conexões...")
        t.start()
    else:
        print("Ok!")
