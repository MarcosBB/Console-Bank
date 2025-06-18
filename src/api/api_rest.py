from flask import Flask, jsonify, request

from src.services.BankService import BankService


class BankAPI:
    def __init__(self, banco_service):
        self.service = banco_service
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/banco/conta/", methods=["POST"])
        def cadastrar_conta():
            data = request.get_json()
            if not data or "tipo" not in data or "numero" not in data:
                return jsonify({"erro": "Dados inválidos"}), 400

            resultado = self.service.cadastrar_conta(data["tipo"], data["numero"], data)

            if "erro" in resultado:
                return jsonify(resultado), 400
            return jsonify(resultado), 201

        @self.app.route("/banco/conta", methods=["GET"])
        def consultar_contas():
            contas = self.service.consultar_contas()
            return jsonify(contas)

        @self.app.route("/banco/conta/<int:numero>", methods=["GET"])
        def consultar_conta(numero):
            resultado = self.service.consultar_conta(numero)
            if "erro" in resultado:
                return jsonify(resultado), 404
            return jsonify(resultado)

        @self.app.route("/banco/conta/<int:numero>/saldo", methods=["GET"])
        def consultar_saldo(numero):
            resultado = self.service.consultar_saldo(numero)
            if "erro" in resultado:
                return jsonify(resultado), 404
            return jsonify(resultado)

        @self.app.route("/banco/conta/<int:numero>/credito", methods=["PUT"])
        def creditar(numero):
            data = request.get_json()
            if not data or "valor" not in data:
                return jsonify({"erro": "Valor obrigatório"}), 400

            resultado = self.service.creditar(numero, data["valor"])
            if "erro" in resultado:
                return jsonify(resultado), 400
            return jsonify(resultado)

        @self.app.route("/banco/conta/<int:numero>/debito", methods=["PUT"])
        def debitar(numero):
            data = request.get_json()
            if not data or "valor" not in data:
                return jsonify({"erro": "Valor obrigatório"}), 400

            resultado = self.service.debitar(numero, data["valor"])
            if "erro" in resultado:
                return jsonify(resultado), 400
            return jsonify(resultado)

        @self.app.route("/banco/conta/transferencia", methods=["PUT"])
        def transferir():
            data = request.get_json()
            if not data or not all(field in data for field in ["from", "to", "amount"]):
                return jsonify({"erro": "Dados incompletos"}), 400

            resultado = self.service.transferir(
                data["from"], data["to"], data["amount"]
            )

            if "erro" in resultado:
                return jsonify(resultado), 400
            return jsonify(resultado)

        @self.app.route("/banco/conta/rendimento", methods=["PUT"])
        def render_juros():
            data = request.get_json()
            taxa = data.get("taxa", 1.0) if data else 1.0

            resultado = self.service.render_juros(taxa)
            if "erro" in resultado:
                return jsonify(resultado), 400
            return jsonify(resultado)

        @self.app.route("/banco/status", methods=["GET"])
        def status():
            contas = self.service.consultar_contas()
            return jsonify({"status": "online", "total_contas": len(contas)})

    def start_server(self, host="127.0.0.1", port=3000, debug=False):
        print(f"API iniciando em {host}:{port}")
        self.app.run(host=host, port=port, debug=debug, use_reloader=False)

    def get_app(self):
        return self.app
