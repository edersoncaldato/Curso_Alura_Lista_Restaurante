import os
from pdb import Restart

restaurantes = [{'nome':'Claudete Safada', 'categoria':'Italiano', 'ativo':False},
                {'nome':'Piranha Estelar', 'categoria':'Peixaria', 'ativo':True},
                {'nome':'Gordão da XJ', 'categoria':'Pizzaria', 'ativo':True}]

def voltar_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal

        Outputs:
        - Retorna ao menu principal
        '''
    input(f'Aperte enter para voltar ao menu principal \n')
    main()

def exibir_nome_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print('Sabor Express\n')

def exibir_subtitulos(text):
    ''' Exibe um subtítulo estilizado na tela

     Inputs:
     - texto: str - O texto do subtítulo
     '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text)
    print()


def exibir_menu():
    ''' Exibe as opções disponíveis no menu principal '''

    print('1 Cadastrar restaurante')
    print('2 Listar restaurantes')
    print('3 ativar restaurante')
    print('4 sair\n')


def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal

        Outputs:
        - Retorna ao menu principal
        '''
    print('Error\n')
    voltar_menu_principal()


def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''

    exibir_subtitulos('Finalizando Programa')


def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

       Inputs:
       - Nome do restaurante
       - Categoria

       Outputs:
       - Adiciona um novo restaurante a lista de restaurantes

       '''
    exibir_subtitulos('Cadastrando Restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    categoria = input(f'Digite a Categoria do {nome_restaurante}: \n')
    if nome_restaurante == '':
        print('Nome Inválido')
        voltar_menu_principal()
    else:
        dados_do_restaurente = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
        restaurantes.append(dados_do_restaurente)
        print(f'\nRestaurante {nome_restaurante} cadastrado!\n')
        voltar_menu_principal()


def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista

        Outputs:
        - Exibe a lista de restaurantes na tela
        '''
    exibir_subtitulos('Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante} | {categoria} | {ativo}\n")
    voltar_menu_principal()

def alternar_ativacao_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante

       Outputs:
       - Exibe mensagem indicando o sucesso da operação
       '''
        exibir_subtitulos('Alterando Restaurante')
        nome_restaurante = input('Nome do restaurante que desejar ativar ou desativar: ')
        restaurante_econtrado = False
        for restaurante in restaurantes:
            if nome_restaurante == restaurante['nome']:
                restaurante_econtrado = True
                restaurante['ativo'] = not restaurante['ativo']
                mensagem = f'O {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso!'
                print(mensagem)
        if not restaurante_econtrado:
            print('Restaurante não foi encontrado')
        voltar_menu_principal()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário

        Outputs:
        - Executa a opção escolhida pelo usuário
        '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_ativacao_restaurante()
                voltar_menu_principal()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    ''' Função principal que inicia o programa '''

    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()
