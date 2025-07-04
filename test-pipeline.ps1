Write-Host "Testando o projeto antes do release..." -ForegroundColor Green

Write-Host "Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "Verificando se o codigo esta sem erro..." -ForegroundColor Yellow
python -m py_compile main.py
if ($LASTEXITCODE -eq 0) {
    Write-Host "main.py: OK" -ForegroundColor Green
} else {
    Write-Host "main.py: ERRO" -ForegroundColor Red
}

Get-ChildItem -Path "src\" -Recurse -Filter "*.py" | ForEach-Object {
    python -m py_compile $_.FullName
    if ($LASTEXITCODE -eq 0) {
        Write-Host "$($_.Name): OK" -ForegroundColor Green
    } else {
        Write-Host "$($_.Name): ERRO" -ForegroundColor Red
    }
}

Write-Host "Verificando estilo do codigo..." -ForegroundColor Yellow
flake8 src\ main.py --max-line-length=120
if ($LASTEXITCODE -eq 0) {
    Write-Host "Estilo: OK" -ForegroundColor Green
} else {
    Write-Host "Estilo: Alguns problemas encontrados" -ForegroundColor Yellow
}

Write-Host "Rodando testes..." -ForegroundColor Yellow
python -m pytest src\tests\ -v
if ($LASTEXITCODE -eq 0) {
    Write-Host "Testes: PASSOU" -ForegroundColor Green
} else {
    Write-Host "Testes: FALHOU" -ForegroundColor Red
}

Write-Host "Teste finalizado!" -ForegroundColor Green
