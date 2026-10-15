from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rlhorochovec.github.io/qa/"
        self.username_input = (By.ID, "login")
        self.password_input = (By.ID, "senha")
        self.login_button = (By.XPATH, "/html/body/main/form/button")
        self.flash_message = (By.ID, "erro")
        self.login_success = (By.XPATH, "/html/body/header[2]/div/div/div/h1")

    def abrir(self):
        self.driver.get(self.url)

    def preencher_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(*self.password_input).send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(*self.login_button).click()

    def obter_mensagem(self):
        return self.driver.find_element(*self.flash_message).text

    def obter_mensagem_sucesso(self):
        return self.driver.find_element(*self.login_success).text
