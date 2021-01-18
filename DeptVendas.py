import rpyc
from server_list import *

my_name = 'DeptVendas'
my_ip = '172.31.91.81'
my_port = 4001

c = rpyc.connect("172.31.29.114", 4000)


registrado = c.root.exposed_register(my_name, my_ip, my_port)



if registrado:
    var = input("Deseja iniciar o servidor? Sim ou Não: ")
    if var.capitalize() == 'Sim':
        print('Server Startado')
    
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(MyServer, port=4001, protocol_config={'allow_public_attrs': True,})
        
        print("O servidor DeptVendas foi iniciado e está executando")
        print("Aguardando conexões...")
        t.start()
    else:
        print("Ok!")
