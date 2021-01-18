import rpyc
from server_list import *


class DBList(MyServer):

    if __name__ == "__main__":
        from rpyc.utils.server import ThreadedServer
        t = ThreadedServer(MyServer, port=4000, protocol_config={'allow_public_attrs': True,})  
        print("O servidor raíz foi iniciado e está executando")
        print("Aguardando conexões...")
        t.start()




