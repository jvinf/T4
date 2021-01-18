class MyServer(rpyc.Service):
    lista_servidores = {}

    def on_connect(self, conn):
        print("Novo cliente conectado")

    def on_disconnect(self, conn):
        print("Cliente Desconectado")

    def exposed_register(self, server_name, server_ip, server_port):
        registrado = True
    
    def exposed_lookup(self, server_name):
        if type(nome) == list:
            if nome[0] in self.lista_servidores:
                if len(nome) > 1 and type(nome) != str:
                    a = rpyc.connect(self.lista_servidores[nome[0]][0], self.lista_servidores[nome[0]][1])

                    if nome[1] in a.root.lista_servidores:
                        return (a.root.lista_servidores[nome[1]])
                    else:
                        print("Não está no segundo nível")
                        return False
                else:
                    print("O nome está incompleto")
                    return False
            else:
                print("O nome digitado não foi encontrado")
                return False
                
                    
                
    def exposed_re_register(self, server_name, server_ip, server_port):
        self.lista_servidores[server_name] = (server_ip, server_port)
        print("O servidor",server_name ,"foi atualizado com os dados corretos")
        
    def exposed_unregister(self, server_name):
        Mensagem = ""
        if server_name in self.lista_servidores:
            del self.lista_servidores[server_name]
            print("O servidor",server_name, "foi deletado com sucesso")
            mensagem = "O servidor foi deletado com sucesso"
            return mensagem        
        else:
            print("Nome não encontrado")
            mensagem = "Nome não encontrado"
            return mensagem
    
    def exposed_retorna_lista(self):
        return self.lista_servidores
    
    def exposed_fqn(self, fqn):
        x = fqn.split(":")
        if type(x) == tuple:
            return x[0], x[1]
        else:
            return x
