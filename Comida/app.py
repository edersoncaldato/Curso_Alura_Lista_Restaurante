import os
from pdb import Restart

restaurantes = ['Intruso', 'Infalivel', 'entreiNumaCilada']

def voltar_menu_principal():
    input(f'Aperte enter para voltar ao menu principal \n')
    main()

def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_subtitulos(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(text)
    print()


def exibir_menu():
    print('1 Cadastrar restaurante')
    print('2 Listar restaurantes')
    print('3 ativar restaurante')
    print('4 sair\n')


def opcao_invalida():
    print('Error\n')
    voltar_menu_principal()


def finalizar_app():
    exibir_subtitulos('Finalizando Programa')


def cadastrar_restaurante():
    exibir_subtitulos('Cadastrando Restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    if nome_restaurante == '':
        print('Nome Inválido')
        voltar_menu_principal()
    else:
        restaurantes.append(nome_restaurante)
        print(f'\nRestaurante {nome_restaurante} cadastrado!\n')
        voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulos('Restaurante')
    for restaurante in restaurantes:
        print(f"- {restaurante}\n")
    voltar_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Você escolheu Ativar restaurante')
                voltar_menu_principal()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()
