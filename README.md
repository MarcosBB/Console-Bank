# Console Bank
Sistema de banco com interface via console feito em `python`.

## Como usar
1. Instale o python 3.13.3.
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o arquivo `main.py`:
```bash
python main.py
```

### Rodando com Docker

Para executar a aplicação utilizando Docker, siga os passos abaixo:

1. **Construa a imagem Docker:**
   ```bash
   docker build -t console-bank-api .
   ```

2. **Execute o container:**
   ```bash
   docker run -p 8080:8080 console-bank-api
   ```

A API estará disponível em `http://localhost:8080`.

### Endpoints da API

Abaixo estão os endpoints disponíveis na API:

- **`GET /banco/status`**: Verifica o status da API e o número total de contas.
- **`GET /banco/conta`**: Lista todas as contas cadastradas.
- **`POST /banco/conta/`**: Cria uma nova conta.
  - **Body (JSON):** `{"tipo": "poupanca", "numero": 12345, "saldo_inicial": 100}`
- **`GET /banco/conta/<numero>`**: Busca uma conta pelo número.
- **`GET /banco/conta/<numero>/saldo`**: Consulta o saldo de uma conta.
- **`PUT /banco/conta/<numero>/credito`**: Adiciona um valor ao saldo da conta.
  - **Body (JSON):** `{"valor": 50}`
- **`PUT /banco/conta/<numero>/debito`**: Subtrai um valor do saldo da conta.
  - **Body (JSON):** `{"valor": 30}`
- **`PUT /banco/conta/transferencia`**: Transfere um valor entre duas contas.
  - **Body (JSON):** `{"from": 1001, "to": 1002, "amount": 100}`
- **`PUT /banco/conta/rendimento`**: Aplica juros a todas as contas poupança.
  - **Body (JSON, opcional):** `{"taxa": 1.5}` (se não informado, a taxa padrão será usada)

### Imagem no Docker Hub

A imagem Docker da API está disponível publicamente no Docker Hub:

**1. Baixar a imagem:**
```bash
docker pull marcosbb/console-bank-api:rel-1.0
```
*Observação: `rel-1.0` é um exemplo de tag. Use a tag da versão que deseja executar.*

**2. Executar o container:**
```bash
docker run -p 8080:8080 marcosbb/console-bank-api:rel-1.0
```

[**Link para o repositório no Docker Hub**](https://hub.docker.com/r/marcosbb/console-bank-api)

## Para os desenvolvedores
- Ao instalar libs sempre use o seguinte comando para atualizar as libs do projeto:
```bash
pip install -r requirements.txt
```

- Lembre-se de usar um ambiente virtual para não poluir o sistema com libs desnecessárias.
  - Para criar um ambiente virtual:
      ```bash
      python -m venv venv
      ```
  - Para ativar o ambiente virtual:
  - Windows:
      ```bash
      venv\Scripts\activate
      ```
  - Linux:
      ```bash
      source venv/bin/activate
      ```

- Ao criar uma nova branch, use o seguinte padrão:
```bash
git checkout -b feat#01/base-do-projeto
```

- Ao criar um novo commit, use o seguinte padrão para o comentário:
```bash
git commit -m "feat(#código-do-issue): nome da mudança"
```

- Para rodar os testes, use o seguinte comando na pasta raiz do projeto:
```bash
python -m pytest
```

## Equipe de devs
- [Marcos Beraldo Barros](https://github.com/MarcosBB)
- [Danrley Araújo de Lima](https://github.com/danrley-lima)
- [Mateus dos Santos Loiola](https://github.com/Mateus0808)
