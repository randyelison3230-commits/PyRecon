#Importa as funções que serão testadas.
from pyrecon.targets import adicionar_alvo, listar_alvos,remover_alvo

def test_adiciona_alvo(monkeypatch, tmp_path):
    import pyrecon.targets as targets

    #Usa um arquivo tempórario para não alterar os alvos reais.
    arquivo_teste = tmp_path / "alvos.json"
    monkeypatch.setattr(targets, "ARQUIVO_ALVOS", arquivo_teste)

    assert adicionar_alvo("192.168.50.30") is True
    assert listar_alvos() == ["192.168.50.30"] 

#Verifica se o programa impede IPs duplicados.
def test_rejeita_alvo_duplicado(monkeypatch, tmp_path):
    import pyrecon.targets as targets

    arquivo_teste = tmp_path / "alvos.json"
    monkeypatch.setattr(targets, "ARQUIVO_ALVOS", arquivo_teste)

    assert adicionar_alvo("192.168.50.30")is True
    assert adicionar_alvo("192.168.50.30") is False

#Verifica se o programa recusa endereços inválidos.

def test_rejeita_ip_invalido():
    assert adicionar_alvo("999.999.999.999") is False


# Verifica se um alvo pode ser removido.
def test_remove_alvo(monkeypatch, tmp_path):
    import pyrecon.targets as targets

    arquivo_teste = tmp_path / "alvos.json"
    monkeypatch.setattr(targets, "ARQUIVO_ALVOS", arquivo_teste)

    adicionar_alvo("192.168.50.30")

    assert remover_alvo("192.168.50.30") is True
    assert listar_alvos() == []