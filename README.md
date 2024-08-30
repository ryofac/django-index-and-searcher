# Projeto Django: Indexador e Buscador

Este projeto é uma aplicação Django baseada [na atividade de implementação de um indexador](https://github.com/ryofac/patro-search) do curso de Análise e Desenvolvimento de sistemas para a disciplina Programação para a Internet 1.

Consiste em um sistema simples de indexação e busca de dados em sites html, com um arquivo de configurações editável (`config.json`) que só pode ser modificado quando a aplicação é inicializada.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- Outros requisitos especificados no arquivo `requirements.txt`

## Configuração Inicial

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados:**
   Ajuste as configurações do banco de dados no arquivo `settings.py` conforme necessário.

4. **Migre o banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Editar o arquivo de configurações:**
   O arquivo `config.json` é editável apenas quando a aplicação é inicializada. Certifique-se de que as configurações necessárias estejam corretas antes de iniciar a aplicação.

## Como Buildar

Este projeto inclui um script `run.sh` para buildar a aplicação. Siga os passos abaixo para utilizá-lo:

1. **Dê permissão de execução ao script:**
   ```bash
   chmod +x run.sh
   ```

2. **Execute o script:**
   ```bash
   ./run.sh
   ```

   O script `run.sh` irá buildar a aplicação e configurar o ambiente conforme necessário.

## Executando o Projeto

Para iniciar o servidor de desenvolvimento, utilize o comando:

```bash
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000/`.

## Estrutura do Projeto
- **`buscador/`**: Diretório contendo a lógica de busca.
- **`buscador/indexer.py`**: Arquivo que contém a lógica de indexação.
- **`config/config.json`**: Arquivo de configurações, editável apenas na inicialização.
- **`run.sh`**: Script para buildar o projeto.
