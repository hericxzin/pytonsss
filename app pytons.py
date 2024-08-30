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
    print("1. Cadastrar Nova camisa")
    print("2. Listar camisas Disponíveis")
    print("3. Ativar/Desativar camisas")
    print("4. Sair")

def escolhe_opcao():
    def exibir_subtitulo(texto):
        os.system("cls" if os.name == 'nt' else 'clear')
        linha = '*' * 70
        print(texto)
        print(linha)
        print(linha)
    

    def retorna_menu():
        input("Digite uma tecla para voltar ao menu principal ")
        main()

    def cadastrar_camisa():
        exibir_subtitulo("Cadastrar Nova Camisa")
        nome_camisa = input("Digite o nome da camisa: ")
        tamanho = int(input("Digite o tamanho da camisa: "))
        cor = input("Digite a cor da camisa: ")
        ativo = input("A camisa está ativa? (Sim/Não): ").strip().lower() == 'sim'
        camisas.append({"nome": nome_camisa, "tamanho": tamanho, "cor": cor, "ativo": ativo})
        print(f"A camisa {nome_camisa} foi cadastrada com sucesso\n")
        retorna_menu()

    def listar_camisas():
        exibir_subtitulo("Lista de Camisas Disponíveis")
        if camisas:
            for i, camisa_item in enumerate(camisas, start=1):
                status = "Ativa" if camisa_item["ativo"] else "Inativa"
                print(f"{i}. Nome: {camisa_item['nome']} | Tamanho: {camisa_item['tamanho']} | Cor: {camisa_item['cor']} | Status: {status}")
        else:
            print("Nenhuma camisa cadastrada.")
        retorna_menu()

    def ativar_desativar_camisa():
        exibir_subtitulo("Ativar/Desativar Camisa")
        listar_camisas()
        if camisas:
            try:
                escolha = int(input("Digite o número da camisa para ativar/desativar: "))
                if 1 <= escolha <= len(camisas):
                    camisa_item = camisas[escolha - 1]
                    camisa_item["ativo"] = not camisa_item["ativo"]
                    status = "Ativa" if camisa_item["ativo"] else "Inativa"
                    print(f"A camisa {camisa_item['nome']} agora está {status}.")
                else:
                    print("Número inválido. Por favor, escolha um número da lista.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        retorna_menu()

    def finalizar_programa():
        os.system("cls" if os.name == 'nt' else 'clear')
        print("Finalizando o programa\n")

    def opcao_invalida():
        print("Opção inválida!")
        input("Aperte qualquer tecla para voltar")
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"voce escolheu a opção{opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_camisa()
        elif opcao_escolhida == 2:
            listar_camisas()
        elif opcao_escolhida == 3:
            ativar_desativar_camisa()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == "__main__":
    main()

