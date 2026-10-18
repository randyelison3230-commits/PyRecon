
import pyrecon.scanner as scanner


def test_rejeita_alvo_nao_cadastrado(monkeypatch):
    # Simula que o Nmap está instalado.
    monkeypatch.setattr(scanner, "nmap_disponivel", lambda: True)

    # Simula uma lista de alvos autorizados vazia.
    monkeypatch.setattr(scanner, "listar_alvos", lambda: [])

    # Registra se o Nmap foi chamado.
    nmap_chamado = False

    def executar_nmap(*args, **kwargs):
        nonlocal nmap_chamado
        nmap_chamado = True

    monkeypatch.setattr(scanner.subprocess, "run", executar_nmap)

    # Testa um IP válido, mas não cadastrado.
    resultado = scanner.reconhecer_alvo("192.168.50.99")

    assert "não cadastrado" in resultado
    assert nmap_chamado is False
