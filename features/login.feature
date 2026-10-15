# language: pt
Funcionalidade: Autenticação no sistema
  Como usuário do sistema
  Quero fazer login com credenciais válidas e inválidas
  Para validar o controle de acesso

  Cenário: Login com sucesso
    Dado que estou na página de login
    Quando preencho o usuário "admin" e a senha "admin"
    E clico no botão de login
    Então devo ser redirecionado para a área logada com sucesso

  Cenário: Login com falha
    Dado que estou na página de login
    Quando preencho o usuário "user" e a senha "admin"
    E clico no botão de login
    Então devo ver uma mensagem de erro de autenticação