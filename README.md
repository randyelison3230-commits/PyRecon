# PyRecon

Ferramenta de reconhecimento de rede desenvolvida em Python para fins educacionais e utilização em laboratórios autorizados.

## Objetivo

O PyRecon permite validar endereços IPv4 privados, gerenciar uma lista local de alvos e executar reconhecimento de portas TCP e identificação de serviços utilizando o Nmap.

## Funcionalidades

- Validação de endereços IPv4 privados e localhost.
- Cadastro de alvos em arquivo JSON.
- Listagem e remoção de alvos cadastrados.
- Verificação do cadastro antes de iniciar uma varredura.
- Reconhecimento das 20 portas TCP mais comuns.
- Tentativa de identificação de serviços e versões com o Nmap.
- Tratamento de erros e tempo limite de execução.
- Testes automatizados com pytest.

## Tecnologias

- Python 3.14 — ambiente de desenvolvimento atual.
- Nmap — reconhecimento de portas e serviços.
- pytest — testes automatizados.

## Requisitos

- Python 3 instalado.
- Nmap instalado e disponível no PATH.
- Git, caso deseje clonar o repositório.

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd PyRecon
```

Crie um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Verifique se o Nmap está instalado:

```bash
nmap --version
```

## Execução

Inicie o programa com:

```bash
python main.py
```

O menu permite validar IPs, cadastrar e listar alvos, executar reconhecimento e remover alvos.

## Testes

Instale o pytest no ambiente virtual, se necessário:

```bash
python -m pip install pytest
```

Execute os testes:

```bash
python -m pytest -v
```

## Escopo e uso responsável

Utilize o PyRecon somente em máquinas próprias ou em sistemas para os quais você tenha autorização explícita de teste.

O cadastro de um endereço no programa é uma proteção operacional, não uma comprovação de autorização legal.

## Status do projeto

Projeto educacional em desenvolvimento, com foco no aprendizado de Python, testes automatizados e fundamentos de reconhecimento de rede.