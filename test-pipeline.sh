#!/bin/bash

# Script para testar antes de fazer o release

echo "Testando o projeto..."

# Instalar dependencias
pip install -r requirements.txt

# Verificar compilacao
echo "Verificando compilacao..."
python -m py_compile main.py
find src/ -name "*.py" -exec python -m py_compile {} \;

# Verificar estilo do codigo
echo "Verificando estilo..."
flake8 src/ main.py --max-line-length=120

# Executar testes
echo "Executando testes..."
python -m pytest src/tests/ -v

echo "Teste concluido!"
