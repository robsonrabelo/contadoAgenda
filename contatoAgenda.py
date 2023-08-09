agenda = {}

def adicionarContato(nome: str, telefone: str) -> None:
    agenda[nome] = telefone
    print('Contato adicionado com sucesso!')

def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda.keys():
        agenda[nome] = telefone
        print('Dados alterados com sucesso!')
    else:
        print('O contato não existe!')

def pesquisarContato(nome: str) -> None:
    if nome in agenda.keys():
        print('-----------------------------')
        print(f'Contato: {nome}')
        print(f'Telefone: {agenda[nome]}')
        print('-----------------------------')
    else:
        print('O contato não existe!')

def deletarContato(nome: str) -> None:
    if nome in agenda.keys():
        del agenda[nome]
        print('Contato removido da agenda!')
    else:
        print('Contato não existe!')

def listarTodos():
    for nome in agenda:
        print('\n --------------------------')
        print((f'Contato: {nome}'))
        print(f'Telefone: {agenda[nome]}')
        print('\n --------------------------')

while True:
    print("------ BEM VINDO AO MENU ------")
    opcao = int(input("1 - Adicionar contato \n"
                      "2 - Editar contato \n"
                      "3 - Pesquisar contato \n"
                      "4 - Deletar contato \n"
                      "5 - Listar contato \n"
                      "6 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        tel = input('Digite o telefone do contato: ')
        adicionarContato(nome, tel)
    elif opcao == 2:
        nome = input('Digite o nome do contato que você deseja alterar: ')
        tel = input('Digite o novo telefone: ')
        editarContato(nome, tel)
    elif opcao == 3:
        nome = input('Digite o nome do contato: ')
        pesquisarContato(nome)
    elif opcao == 4:
        nome = input('Digite o nome do cotato: ')
        deletarContato(nome)
    elif opcao == 5:
        listarTodos()
    elif opcao == 6:
        break