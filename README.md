# Relatorio de funcionamento da tarefa

## > server_list.py

- `on_connect`: identifica no servidor quando um novo cliente se conecta 
- `on_disconnect`: identifica no servidor quando um cliente conectado se desconecta 

- `exposed_register`: Recebe os parametros _server_name_, _server_ip_, e _server_port_, verifica se o nome já se encontra registrado, se o nome e o ip forem iguais não faz nada, se o nome estiver igual e o ip diferente é chamado o método ***exposed_re_register***, que substitui os dados inconsistentes pelos novos dados recebidos. 
Se o nome não estiver registrado, o método o registra um novo servidor com os parametros recebidos.

- `exposed_lookup`: Recebe os parametros _server_name_ que deve vir como um FQN. Após receber o FQN é chamado o método ***exposed_fqn*** que trata o nome e o divide em duas partes. De posse dos nomes simples o método ***exposed_lookup*** faz a pesquisa do primeiro nome, se encontra-lo ele pesquisa o segundo nome no primeiro servidor encontrado. Após acha-los é devovido o _endereço ip_ e a _porta_ do segundo servidor ( servidor de aplicação ) para a maquina que chamou o método.


- `exposed_re_register`: Recebe os parametros _server_name_, _server_ip_, _server_port_, e substitui os dados do registro pelos dados recebidos. 

- `exposed_unregister`: Recebe o parametro _server_name_ e o deleta do registro, se o nome não for encontrado ele retorna uma mensagem de *"Nome não encontrado"*. 
OBS: Esse método deve ser chamado manualmente. 

- `exposed_retorna_lista`: Ao ser chamado esse método retorna a lista de servidores registrados no servidor ao qual há algum cliente conectado.
OBS: Esse método deve ser chamado manualmente. 

- `exposed_fqn`: Recebe um nome FQN e o transforma em nomes simples.

## > server_connect.py

Ao ser executado inicia o servidor raíz que após executado aguarda conexões de servidores de domínio. O servidor é iniciado chamando a classe *MyServer* que é criada no arquivo *server_list*. A porta do servidor é definida manualmente.

## > DeptVendas.py, DeptRH.py, CalcServer, CalcServer2

Chama o método ***exposed_register***, enviando os parametros definidos manualmente. Ao receber o valor True do método chamado ele cria um novo servidor se o usuário confirmar.
Se o usuário rejeitar, a execução do servidor não é iniciada.
OBS: Os servidores *DeptVendas.py*, e *DeptRH.py* se conectam ao servidor Raíz. Já os servidores *CalcServer* e *CalcServer2* se conectam aos servidores *DeptVendas.py* e *DeptRH.py* respectivamente.

## > cliente.py

chama o método *rpyc.connect* ao servidor raíz, ao estabelecer a conexão chama o método ***exposed_lookup*** enviando um FQN que é informado pelo usuário. Se o nome for encontrado, é chamado novamente o método *rpyc.connect*, porém agora com o servidor de aplicação pesquisado. Essa nova conexão é realizada com os dados de ip e porta retornados ao chamar o método ***exposed_lookup***.








