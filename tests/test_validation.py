# Importa a função que será testada.
from pyrecon.validator import validar_alvo

# Confirma que o endereço de loopback é aceito.
def test_aceita_localhost():
    assert validar_alvo("127.0.0.1")is True 

# Confirma que um endereço IPv4 privado é aceito.
def test_aceita_ip_privado():
    assert validar_alvo("192.168.1.10")is True


# Confirma que um IPv4 público como este é rejeitado.
def test_rejeita_ip_publico():
    assert validar_alvo("8.8.8.8") is False


# Confirma que um endereço IPv4 malformado é rejeitado.
def test_rejeita_ip_invalido():
    assert validar_alvo("999.999.999.999") is False

# Confirma que um nome de domínio não é aceito como IPv4.
def test_rejeita_hostname():
    assert validar_alvo("example.com") is False

# Confirma que uma string vazia é rejeitada.
def test_rejeita_string_vazia():
    assert validar_alvo("") is False

# Confirma que um tipo incorreto, como inteiro, é rejeitado.   
def test_rejeita_tipo_incorreto():
    assert validar_alvo(None) is False
