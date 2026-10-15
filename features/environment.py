import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    os.makedirs("reports/screenshots", exist_ok=True)

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    # Ative o headless caso vá rodar em servidores de CI/CD sem interface gráfica
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        if scenario.status == "failed":
            safe_name = scenario.name.replace(" ", "_").lower()
            screenshot_path = f"reports/screenshots/{safe_name}.png"
            context.driver.save_screenshot(screenshot_path)
            print(f"\n[Evidência] Screenshot de falha salva em: {screenshot_path}")
        
        context.driver.quit()