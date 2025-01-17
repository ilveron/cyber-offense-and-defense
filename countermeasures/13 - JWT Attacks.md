JWT stands for JSON Web Token.
It is a standardized format for sending cryptographically signed JSON data.
## Hierarchy
![[Pasted image 20250116205559.png]]
We usually refer to **JWS** as common **JWT** (and we will do it from now on)
## Structure
A JWT is made of three parts separated by a . (dot)

\<**header**>.\<**payload**>.\<**signature**>

The header and payload parts are simply base64-encoded, while the signature is derived from the first two parts using HMAC (Hash-based Message Authentication Code)

*NOTE*: The signature part can be missing if the signature algorithm specified in the header is `none`, but the . symbol before is mandatory (i.e., a JWT *always* contains a dot after the *header* and the *payload* part)
## Vulnerabilities
JWT vulnerabilities typically arise due to flawed JWT handling within the application. Since the header and payload parts are in clear (in JWT/JWS) and tamperable, it all relies on the secrecy of the server's secret key, as it is used to verify the signature.

- Accepting token with no signature
- Accepting tokens with tampered algorithm
- Weak encryption keys
- Misunderstanding symmetric and asymmetric encryption (in symmetric cryptography once the single key is leaked, it's game over)
- Using JWS thinking it is crpytographically encrypted