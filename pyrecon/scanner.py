
# Permite verificar se um executável está disponível no sistema.
import shutil

# Permite executar comandos externos, como o Nmap.
import subprocess

# Permite interpretar e validar endereços IP.
import ipaddress

# Importa a validação de IPv4 e a lista de alvos cadastrados.
from pyrecon.validator import validar_alvo
from pyrecon.targets import listar_alvos


# Verifica se o comando Nmap está disponível no sistema.
def nmap_disponivel() -> bool:
    """Verifica se o Nmap está instalado."""
    return shutil.which("nmap") is not None


# Executa uma varredura TCP em um alvo cadastrado.
def reconhecer_alvo(alvo: str) -> str:
    """Reconhece portas TCP de um alvo cadastrado."""

    # Impede a execução se o Nmap não estiver instalado.
    if not nmap_disponivel():
        return "Erro: Nmap não encontrado no sistema."

    # Confere se o alvo recebido é um texto.
    if not isinstance(alvo, str):
        return "Erro: o alvo precisa ser um endereço IPv4."

    # Valida o endereço IPv4.
    if not validar_alvo(alvo):
        return "Erro: endereço IPv4 inválido ou fora do escopo."

    # Normaliza o endereço para comparar com a lista.
    endereco = str(ipaddress.ip_address(alvo.strip()))

    # Consulta os alvos cadastrados.
    try:
        alvos_cadastrados = listar_alvos()
    except (OSError, ValueError) as erro:
        return f"Erro ao consultar a lista de alvos: {erro}"
    except Exception:
        return "Erro inesperado ao consultar a lista de alvos."

    # Bloqueia qualquer endereço que não esteja cadastrado.
    if endereco not in alvos_cadastrados:
        return "Erro: alvo não cadastrado. Cadastre-o antes de escanear."

    # Monta o comando do Nmap como uma lista de argumentos.
    # -sT: usa conexões TCP.
    # -sV: tenta identificar os serviços e suas versões.
    # --top-ports 20: verifica as 20 portas mais comuns.
    comando = [
        "nmap",
        "-sT",
        "-sV",
        "--top-ports", "20",
        endereco,
    ]

    # Executa o Nmap e captura sua saída.
    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )

    # Trata o caso em que a execução excede 120 segundos.
    except subprocess.TimeoutExpired:
        return "Erro: a varredura excedeu o tempo limite."

    # Trata erros do sistema ao tentar executar o comando.
    except OSError as erro:
        return f"Erro ao executar o Nmap: {erro}"

    # Verifica se o Nmap terminou com um código de erro.
    if resultado.returncode != 0:
        return resultado.stderr.strip() or "Erro durante a varredura."

    # Devolve o relatório produzido pelo Nmap.
    return resultado.stdout
