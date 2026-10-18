
# Biblioteca padrão para validar endereços IP.
import ipaddress


def validar_alvo(alvo: str) -> bool:
    """
    Verifica se o endereço informado é um IPv4 privado
    ou o endereço de loopback local.

    Esta função não verifica autorização.
    O cadastro é verificado separadamente pelo scanner.
    """

    # Aceita somente entradas em formato de texto.
    if not isinstance(alvo, str):
        return False

    # Remove espaços desnecessários.
    alvo = alvo.strip()

    # Tenta interpretar o endereço informado.
    try:
        endereco = ipaddress.ip_address(alvo)
    except ValueError:
        return False

    # Aceita somente IPv4.
    if not isinstance(endereco, ipaddress.IPv4Address):
        return False

    # Permite localhost.
    if endereco == ipaddress.IPv4Address("127.0.0.1"):
        return True

    # Define as faixas privadas de IPv4.
    redes_privadas = [
        ipaddress.ip_network("10.0.0.0/8"),
        ipaddress.ip_network("172.16.0.0/12"),
        ipaddress.ip_network("192.168.0.0/16"),
    ]

    # Verifica se o endereço pertence a uma faixa privada.
    return any(endereco in rede for rede in redes_privadas)
