import	os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def subititulo(nome):
    '''Exibe o titulo do programa'''
    os.system('cls')
    linha = '*'*len(nome)
    print(linha)
    print(nome)
    print(linha)
    print('\n')

def voltar_ao_menu_principal():
    '''manda o usuario de volta pare executar outras opçoes'''
    input('\nDigite uma tecla para sair\n ')
    main()

def exibir_nome_do_programa():
    '''o nome do programa'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    '''opçoes disponives para o usuario escolher'''
    print('1. Cadastro restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n ')

def finalizar_app():
    '''finalizar o app'''
    subititulo('Sair')

def opcao_invalida():
    '''prevençao de erros'''
    subititulo('Opcao invalida')
    voltar_ao_menu_principal()

def cadstro_restaurante():
    '''cadastra o restaurante'''
    subititulo('Cadastro de novos restaurantes:')
    nome_do_restaurante = input('Insira o nome do restaurante a ser cadastrado:\n ')
    categoria_do_restaurante = input(f'Insira a Categoria do {nome_do_restaurante}:\n')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''mostra os restaurantes cadastrados'''
    subititulo('Listando os restaurantes:')

    print(f'{'Nome do restaurante '.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado' 
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def ativar_restaurante():
    '''Ativa ou desativa o restaurante indicado'''
    subititulo('Ativando o restaurante')

    nome_restaurante = input('Insira o nome do restaurante que deseja alterar: \n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com susesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com susesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante nao encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
        '''pede para o usuario escolher uma opçao oferecia no menu'''

    # try:
        opçao_escolida = int(input('Escolha uma opçao: '))
        if opçao_escolida == 1:
            cadstro_restaurante()
        elif opçao_escolida == 2:
            listar_restaurantes()
        elif opçao_escolida == 3:
            ativar_restaurante()
        elif opçao_escolida == 4:
            finalizar_app()
    #     else:
    #         opcao_invalida()
    # except:
    #     opcao_invalida()

def main():
    '''executa todo o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
