import os

# Lista para armazenar as roupas
camisas = [
    {"nome": "Camisa Adidas 8", "tamanho": 42, "cor": "Preto/Branco", "ativo": True},
    {"nome": "Camisa Nike 8", "tamanho": 44, "cor": "Azul/Cinza", "ativo": False},
    {"nome": "Camisa Nike Elevate 3", "tamanho": 40, "cor": "Branco", "ativo": True}
]

def exibir_nome_do_programa():
    print("""
░█████╗░██╗░░░░░░█████╗░████████╗██╗░░██╗███████╗░██████╗  ██████╗░░█████╗░
██╔══██╗██║░░░░░██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║░░░██║░░░███████║█████╗░░╚█████╗░  ██║░░██║██║░░██║
██║░░██╗██║░░░░░██║░░██║░░░██║░░░██╔══██║██╔══╝░░░╚═══██╗  ██║░░██║██║░░██║
╚█████╔╝███████╗╚█████╔╝░░░██║░░░██║░░██║███████╗██████╔╝  ██████╔╝╚█████╔╝
░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░  ╚═════╝░░╚════╝░

██╗░░██╗███████╗██████╗░██╗░█████╗░
██║░░██║██╔════╝██╔══██╗██║██╔══██╗
███████║█████╗░░██████╔╝██║██║░░╚═╝
██╔══██║██╔══╝░░██╔══██╗██║██║░░██╗
██║░░██║███████╗██║░░██║██║╚█████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░
""")

def mostra_escolhas():
    print("1. Cadastrar camisas")
    print("2. Listar camisas")
    print("3. Ativar estoque")
    print("4. Sair")

def escolhe_opcao():
    
    def exibir_subtitulo(texto):
        os.system('cls')
        Linha =- len(texto)
        print(Linha)
        print(texto)
        print('')
    
    def retorna_menu():
        input('Digite uma tecla para voltar ao menu principal')
        main()

    def cadastrar_camisas():
        exibir_subtitulo('Cadastrar Camisa')
        
        nome_camisa = input('Digite a marca da camisa:')
        modelo_camisa = input('Digite o modelo:')
        dados_da_camisa = {'nome': nome_camisa,  'modelo': modelo_camisa,  'ativo':True}
        camisas.append(dados_da_camisa)
        print(f'A camisa {nome_camisa} foi cadastrada com sucesso\n")
        
        retorna_menu()

    def listar_camisas():
        exibir_subtitulo('Lista de Camisas Disponíveis')
        for camisa in camisas:
            nome_camisa = camisa['nome']
            modelo_camisa = camisa['modelo']
            ativo = 'Cadastrado' if ['camisas'] else  'Não cadastrado'
            print(f' - {nome_camisa.ljust(20)} | {modelo_camisa.ljust(20)} | {ativo}')
        retorna_menu()

    def ativar_camisas():
        exibir_subtitulo('Ativar camisa')
        nome_camisa = input('Digite o nome da camisa que desaja ativar:')
        camisa_encontrado = False

        for camisa in camisas:
            if nome_camisa == camisa('camisa'):
                camisa_encontrado = True
                camisa['camisa'] = not camisa['camisa']
                mensagem = f'A matricula de {nome_camisa} foi ativado com suceso' if camisa['ativo'] else f'A matricula {nome_camisa} foi desativado'
                print(mensagem)
        if not camisa_encontrado:
            print('Não encontrado')
        retorna_menu()

    def finalizar_programa():
        os.system('cls')
        print('Finalizando o programa\n')

    def opcao_invalida():
        print('Essa opção não é válida\n')
        input('Aperte qualquer tecla para voltar')
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastra_camisas()
        elif opcao_escolhida == 2:
            listar_camisas()
        elif opcao_escolhida == 3:
            ativar_camisas()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()
