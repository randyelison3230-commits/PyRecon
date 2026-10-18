
# Bibliotecas para trabalhar com JSON, endereços IP e caminhos.
import json
import ipaddress
from pathlib import Path

# Importa a função que valida endereços IPv4.
from pyrecon.validator import validar_alvo


# Define o arquivo de armazenamento na pasta principal do projeto.
ARQUIVO_ALVOS = Path(__file__).resolve().parent.parent / "alvos.json"


# Carrega os alvos cadastrados.
def listar_alvos() -> list[str]:
    """Retorna a lista de alvos cadastrados."""

    # Se o arquivo ainda não existe, retorna uma lista vazia.
    if not ARQUIVO_ALVOS.exists():
        return []

    # Abre o arquivo JSON para leitura.
    with ARQUIVO_ALVOS.open("r", encoding="utf-8") as arquivo:
        alvos = json.load(arquivo)

    # Confere se o conteúdo é uma lista de textos.
    if not isinstance(alvos, list):
        raise ValueError("O arquivo de alvos precisa conter uma lista.")

    if not all(isinstance(alvo, str) for alvo in alvos):
        raise ValueError("O arquivo contém alvos em formato inválido.")

    return alvos


# Salva os alvos cadastrados no arquivo JSON.
def salvar_alvos(alvos: list[str]) -> None:
    """Grava a lista de alvos no arquivo."""

    with ARQUIVO_ALVOS.open("w", encoding="utf-8") as arquivo:
        json.dump(alvos, arquivo, indent=4, ensure_ascii=False)


# Cadastra um endereço IPv4 válido.
def adicionar_alvo(alvo: str) -> bool:
    """Adiciona um alvo se ele ainda não estiver cadastrado."""

    if not validar_alvo(alvo):
        return False

    # Normaliza o endereço para evitar duplicatas.
    alvo = str(ipaddress.ip_address(alvo.strip()))

    alvos = listar_alvos()

    # Não cadastra um endereço repetido.
    if alvo in alvos:
        return False

    alvos.append(alvo)
    salvar_alvos(alvos)

    return True


# Remove um endereço da lista.
def remover_alvo(alvo: str) -> bool:
    """Remove um alvo cadastrado."""

    if not validar_alvo(alvo):
        return False

    alvo = str(ipaddress.ip_address(alvo.strip()))
    alvos = listar_alvos()

    if alvo not in alvos:
        return False

    alvos.remove(alvo)
    salvar_alvos(alvos)

    return True
