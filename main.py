from src import Bank
from src import FrontendApp

bank = Bank()
bank.criar_conta(1)
bank.criar_conta(2)
bank.criar_conta(3, "bonus")
bank.criar_conta(4, "poupanca")
frontend_app = FrontendApp(bank)
frontend_app.run()
