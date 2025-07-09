import os
from src.api.api_rest import BankAPI
from src.models.bank import Bank
from src.services.BankService import BankService


def setup_banco():
    banco = Bank()

    # contas de teste
    banco.criar_conta(1001, "simples")
    banco.criar_conta(1002, "bonus")
    banco.criar_conta(1003, "poupanca", 1000)
    banco.creditar(1001, 500)

    return banco


def main():
    print("Console Bank - API REST")

    banco = setup_banco()
    service = BankService(banco)

    host = os.environ.get("APP_HOST", "0.0.0.0")
    port = int(os.environ.get("APP_PORT", 8080))

    print(f"API rodando em http://{host}:{port}")

    api = BankAPI(service)

    try:
        api.start_server(host=host, port=port, debug=False)
    except KeyboardInterrupt:
        print("Saindo...")


if __name__ == "__main__":
    main()
