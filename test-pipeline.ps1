# Script simples para testar antes de fazer o release
# Feito para o trabalho da faculdade

Write-Host "Testando o projeto antes do release..." -ForegroundColor Green

# Instalar o que precisa
Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

# Testar se o codigo esta certo
Write-Host "Verificando se o codigo esta sem erro..." -ForegroundColor Yellow
python -m py_compile main.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "main.py: OK" -ForegroundColor Green
} else {
    Write-Host "main.py: ERRO" -ForegroundColor Red
}

# Verificar arquivos da pasta src
Get-ChildItem -Path "src\" -Recurse -Filter "*.py" | ForEach-Object {
    python -m py_compile $_.FullName
    if ($LASTEXITCODE -eq 0) {
        Write-Host "$($_.Name): OK" -ForegroundColor Green
    } else {
        Write-Host "$($_.Name): ERRO" -ForegroundColor Red
    }
}

# Rodar flake8 se tiver instalado
Write-Host "Verificando estilo do codigo..." -ForegroundColor Yellow
flake8 src\ main.py --max-line-length=120
if ($LASTEXITCODE -eq 0) {
    Write-Host "Estilo: OK" -ForegroundColor Green
} else {
    Write-Host "Estilo: Alguns problemas encontrados" -ForegroundColor Yellow
}

# Rodar testes
Write-Host "Rodando testes..." -ForegroundColor Yellow
python -m pytest src\tests\ -v
if ($LASTEXITCODE -eq 0) {
    Write-Host "Testes: PASSOU" -ForegroundColor Green
} else {
    Write-Host "Testes: FALHOU" -ForegroundColor Red
}

Write-Host "Teste finalizado!" -ForegroundColor Green
