import base64
from io import BytesIO
import os
from PIL import Image, ImageOps
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    os.makedirs("reports/screenshots", exist_ok=True)

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    # Ative o headless caso vá rodar em servidores de CI/CD sem interface gráfica
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1900,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.execute_cdp_cmd(
        "Emulation.setDeviceMetricsOverride",
        {"width": 1900, "height": 1080, "deviceScaleFactor": 1, "mobile": False},
    )

def after_step(context, step):
    if hasattr(context, "driver"):
        screenshot = BytesIO(context.driver.get_screenshot_as_png())
        with Image.open(screenshot) as image:
            image = ImageOps.fit(image, (800, 450), method=Image.Resampling.LANCZOS)
            resized_screenshot = BytesIO()
            image.save(resized_screenshot, format="PNG")
        screenshot_data = base64.b64encode(resized_screenshot.getvalue()).decode("ascii")
        context.attach("image/png", screenshot_data)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        if scenario.status == "failed":
            safe_name = scenario.name.replace(" ", "_").lower()
            screenshot_path = f"reports/screenshots/{safe_name}.png"
            context.driver.save_screenshot(screenshot_path)
            print(f"\n[Evidência] Screenshot de falha salva em: {screenshot_path}")
        
        context.driver.quit()