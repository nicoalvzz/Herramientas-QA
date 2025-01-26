from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar las opciones de Firefox
options = FirefoxOptions()
# options.add_argument("--headless")  # Ejecuta el navegador en modo headless

# Inicializar el WebDriver remoto para Firefox
driver = webdriver.Remote(
    command_executor='http://138.199.149.0:4444/wd/hub',
    options=options
)

def extract_lleego_content():
    driver.get("https://lleego.com/")
    try:
        # Esperar hasta que la página se haya cargado
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Página de Lleego abierta con éxito")

        # Extraer todos los párrafos y encabezados que tengan contenido de texto
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        headers = driver.find_elements(By.TAG_NAME, "h1") + \
                  driver.find_elements(By.TAG_NAME, "h2") + \
                  driver.find_elements(By.TAG_NAME, "h3")

        # Filtrar párrafos y encabezados vacíos
        paragraphs = [p for p in paragraphs if p.text.strip() != ""]
        headers = [h for h in headers if h.text.strip() != ""]

        # Extraer y mostrar el texto de los párrafos
        for i, paragraph in enumerate(paragraphs):
            print(f"Párrafo {i+1}: {paragraph.text}")

        # Extraer y mostrar el texto de los encabezados
        for i, header in enumerate(headers):
            print(f"Encabezado {i+1}: {header.text}")

        # Extraer todos los enlaces con texto
        links = driver.find_elements(By.TAG_NAME, "a")
        links = [link for link in links if link.text.strip() != ""]
        for i, link in enumerate(links):
            href = link.get_attribute("href")
            text = link.text
            if href and text:  # Asegurarse de que el enlace y el texto no estén vacíos
                print(f"Enlace {i+1}: {text} ({href})")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    extract_lleego_content()

