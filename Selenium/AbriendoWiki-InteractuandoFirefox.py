from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar las opciones de Firefox
options = FirefoxOptions()
# Quitar el modo headless para ver el navegador en acción
# options.add_argument("--headless")

# Inicializar el WebDriver remoto para Firefox
driver = webdriver.Remote(
    command_executor='http://IP:4444/wd/hub',
    options=options
)

def open_wikipedia():
    driver.get("https://es.wikipedia.org/wiki/Wikipedia")
    try:
        # Esperar hasta que el título de la página esté presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading"))
        )
        print("Página de Wikipedia abierta con éxito")

        # Mantén la sesión abierta para interacciones adicionales
        while True:
            input("Interactúa con el navegador y luego presiona CTR+Z si quieres cerrar la sesion...")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    open_wikipedia()
