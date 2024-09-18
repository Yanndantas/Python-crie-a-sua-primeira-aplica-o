import os

restaurantes = [{'nome':'praça','categoria':'Japonesa', 'ativo':False},
                {'nome':'pizza suprema', 'categoria':'italiana','ativo':True},
                {'nome':'cantina','categoria':'italiano', 'ativo':False}]


def exibir_nome_do_programa():
    '''
    Esta função exibe o nome do programa printando o nome "sabor express"
    '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░/n""")
    
def exibir_opcoes():
    '''
    Esta função exibe as opções possíveis para escolha
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
    Esta função finaliza as atividades do código
    '''
    exibir_subtitulo('Finalizando app')


def voltar_ao_menu_principal():
    '''
    Esta função volta ao menu principal
    input: qualquer tecla
    output: retorna a função "exibir_opcoes" 
    '''
    input('Digite uma tecla para voltar ao menu principal ')
    main()


def opcao_invalida():
    '''
    Esta função printa que a opção escolhida não é valida e retorna ao menum principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''
    Esta função exibe uma decoração para o texto
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''
    Está função é responsável por cadastrar um novo restaurante

        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante, {nome_do_restaurante},foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''
    Esta função lista os restaurantes demonstrando todos os restaurantes cadastrados
    '''
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Sim' if restaurante['ativo'] else 'Não'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | Ativo: {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    '''
    Esta função permite alterar o estado do restaurante entre ativo e desativado

    input: nome do restaurante que deseja alterar o estado
    output: alteração do estado
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ').lower()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']
                mensagem = f'O restaurante {nome_restaurante} foi {"ativado" if restaurante["ativo"] else "desativado"} com sucesso'
                print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''
    Função que permite selecionar as opções do menu principal
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # opcao_escolhida = int(opcao_escolhida)
        print(f'Voce escolheu a opcao', {opcao_escolhida})


        if opcao_escolhida ==1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
	


def main():
 '''
 Esta função inicia o app utilizando as funções criadas
 '''
 os.system('cls')
 exibir_nome_do_programa()
 exibir_opcoes()
 escolher_opcao()

if __name__ == '__main__':
    main()