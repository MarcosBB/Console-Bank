echo "Testando o projeto antes do release..."

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Verificando se o codigo esta sem erro..."
python -m py_compile main.py
if [ $? -eq 0 ]; then
    echo "main.py: OK"
else
    echo "main.py: ERRO"
fi

find src/ -name "*.py" -exec python -m py_compile {} \;
if [ $? -eq 0 ]; then
    echo "Arquivos src/: OK"
else
    echo "Arquivos src/: ERRO"
fi

echo "Verificando estilo do codigo..."
flake8 src/ main.py --max-line-length=120
if [ $? -eq 0 ]; then
    echo "Estilo: OK"
else
    echo "Estilo: Alguns problemas encontrados"
fi

echo "Rodando testes..."
python -m pytest src/tests/ -v
if [ $? -eq 0 ]; then
    echo "Testes: PASSOU"
else
    echo "Testes: FALHOU"
fi

echo "Teste finalizado!"
