# Importa as funções de gerenciamento dos alvos.
from pyrecon.targets import listar_alvos, adicionar_alvo, remover_alvo
# Importa a função responsável por validar endereços IPv4.
from pyrecon.validator import validar_alvo
# Importa a função que executa o reconhecimento usando o Nmap.
from pyrecon.scanner import reconhecer_alvo

# Exibe o menu principal do PyRecon.
def mostrar_menu():
    print("\n" + "=" * 35)
    print("          PyRecon")
    print("  Ferramenta de Reconhecimento")
    print("=" * 35)
    print("1. Validar um endereço IPv4")
    print("2. Cadastrar alvo autrorizado")
    print("3. Listar alvos autorizados")
    print("4. Reconhecer portas e serviços")
    print("5. Remover alvo autorizado")
    print("6. Sair")
    print("=" * 35)

# Controla o fluxo principal do programa.
def main():
    # Mantém o menu em execução até o usuário escolher sair.
    while True:
        mostrar_menu()

        # Recebe a opção escolhida pelo usuário.
        opcao = input("Escolha uma opção: ").strip()

        # Opção 1: verifica se o endereço IPv4 é válido.
        if opcao == "1":
            print("\nValidação de endereço IPv4")

            # Solicita o endereço ao usuário.
            alvo = input("Digite o endereço IP: ").strip()

            # Verifica a validade do endereço.
            if validar_alvo(alvo):
                print(f"[+] Endereço IPv4 válido e dentro das faixas aceitas: {alvo}")
            else:
                print(f"[-] Endereço inválido ou fora das faixas aceitas: {alvo}")

        # Opção 2: cadastra um alvo na lista.
        elif opcao == "2":
            print("\nCadastro de alvo autorizado")

            # Solicita o IP que será cadastrado.
            alvo = input("Digite o IP do alvo: ").strip()

            # O cadastro representa a declaração de que existe autorização.
            if adicionar_alvo(alvo):
                print(f"[+] Alvo cadastrado: {alvo}")
            else:
                print("[-] Cadastro recusado: IP inválido ou já cadastrado.")

        # Opção 3: exibe os alvos cadastrados.
        elif opcao == "3":
            print("\nAlvos cadastrados")

            # Recupera a lista salva no arquivo JSON.
            alvos = listar_alvos()

            if alvos:
                for indice, alvo in enumerate(alvos, start=1):
                    print(f"{indice}. {alvo}")
            else:
                print("Nenhum alvo cadastrado.")

        # Opção 4: executa o reconhecimento de portas e serviços.
        elif opcao == "4":
            print("\nReconhecimento de portas e serviços")

            # Solicita o IP que será examinado.
            alvo = input("Digite o IP do alvo cadastrado: ").strip()

            # Confere se o IP está cadastrado.
            if alvo in listar_alvos():
                print(f"\n[+] Iniciando reconhecimento de {alvo}...")

                # Executa o scanner e guarda o resultado.
                resultado = reconhecer_alvo(alvo)

                # Exibe a saída retornada pelo Nmap.
                print("\n" + resultado)
            else:
                print("[-] Alvo não cadastrado. Cadastre-o antes de escanear.")

        # Opção 5: remove um alvo cadastrado.
        elif opcao == "5":
            print("\nRemover alvo autorizado")

            # Solicita o IP que será removido.
            alvo = input("Digite o IP que deseja remover: ").strip()

            if remover_alvo(alvo):
                print(f"[+] Alvo removido: {alvo}")
            else:
                print("[-] IP inválido ou não encontrado na lista.")

        # Opção 6: encerra o programa.
        elif opcao == "6":
            print("\nEncerrando o PyRecon...")
            break

        # Trata opções inexistentes.
        else:
            print("\nOpção inválida. Tente novamente.")


# Executa main() somente quando este arquivo é iniciado diretamente.
if __name__ == "__main__":
    main()