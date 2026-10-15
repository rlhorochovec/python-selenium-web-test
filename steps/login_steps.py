from behave import given, when, then
from pages.login_page import LoginPage

@given('que estou na página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()

@when('preencho o usuário "{usuario}" e a senha "{senha}"')
def step_impl(context, usuario, senha):
    context.login_page.preencher_usuario(usuario)
    context.login_page.preencher_senha(senha)

@when('clico no botão de login')
def step_impl(context):
    context.login_page.clicar_login()

@then('devo ser redirecionado para a área logada com sucesso')
def step_impl(context):
    mensagem = context.login_page.obter_mensagem_sucesso()
    assert "Administrador" in mensagem

@then('devo ver uma mensagem de erro de autenticação')
def step_impl(context):
    mensagem = context.login_page.obter_mensagem()
    assert "Usuário e/ou senha incorretos!" in mensagem