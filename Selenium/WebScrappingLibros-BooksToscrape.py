import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Hacer una solicitud HTTP al sitio web
response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar los elementos que contienen los títulos y precios de los libros
books = soup.find_all('article', class_='product_pod')

# Extraer los títulos y precios de los libros
book_data = []
total_price = 0
for book in books:
    title = book.h3.a['title']
    price_text = book.find('p', class_='price_color').text
    # Convertir el precio a un número flotante
    price = float(price_text[1:])  # Eliminar el símbolo de la moneda y convertir a float
    total_price += price
    book_data.append([title, price_text])

# Mostrar los datos en formato de tabla
print(tabulate(book_data, headers=["Título", "Precio"], tablefmt="pretty"))

# Mostrar la suma total de los precios
print(f"\nSuma total de los precios: £{total_price:.2f}")

