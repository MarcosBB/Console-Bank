# Script para testar antes de fazer o release

Write-Host "Testando o projeto..." -ForegroundColor Green

# Instalar dependencias
pip install -r requirements.txt

# Verificar compilacao
Write-Host "Verificando compilacao..." -ForegroundColor Yellow
python -m py_compile main.py
Get-ChildItem -Path "src\" -Recurse -Filter "*.py" | ForEach-Object {
    python -m py_compile $_.FullName
}

# Verificar estilo do codigo
Write-Host "Verificando estilo..." -ForegroundColor Yellow
flake8 src\ main.py --max-line-length=120

# Executar testes
Write-Host "Executando testes..." -ForegroundColor Yellow
python -m pytest src\tests\ -v

Write-Host "Teste concluido!" -ForegroundColor Green
