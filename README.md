# python-selenium-web-test
[![python-selenium-web-test](https://github.com/rlhorochovec/python-selenium-web-test/actions/workflows/ci.yaml/badge.svg)](https://github.com/rlhorochovec/python-selenium-web-test/actions/workflows/ci.yaml)

Projeto de automação de testes web utilizando Python, Selenium e Behave com GitHub Actions.

## Dependências
- selenium>=4.18.0
- behave>=1.2.6
- webdriver-manager>=4.0.1
- behave-html-formatter>=0.9.10
- allure-behave>=2.13.2

## Instalação
Instale python-selenium-web-test com pip

```bash
  cd python-selenium-web-test
  python -m venv .venv
  pip install -r requirements.txt
  pip install psycopg2-binary
```

## Rodando os testes
Para rodar os testes, rode o seguinte comando

```bash
  behave
```
## Relatório dos testes
Gerar o Behave Report
```bash
  behave -f html -o reports/relatorio_testes.html
  reports/relatorio_testes.html
```

Visualizar relatório dos testes publicado
[Visualizar](https://rlhorochovec.github.io/python-selenium-web-test/relatorio_testes.html)
