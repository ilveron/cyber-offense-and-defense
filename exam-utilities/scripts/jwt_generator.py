import jwt

UPPER_BOUND = 500
PAYLOAD_PARAMETER = "param"
HEADERS = {"alg": "none", "typ": "JWT"}

with open("generated_jwts.txt", "w") as f:
    for k in range(0, UPPER_BOUND):
        jwt = jwt.encode({PAYLOAD_PARAMETER: k}, None, headers=HEADERS)
        f.write(f"{jwt}\n")

