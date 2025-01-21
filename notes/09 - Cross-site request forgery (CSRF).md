Victims are induced to performs actions they do not intend to perform
# XSS vs CSRF
- **XSS**: attackers make victim execute malicious custom scripts on their browser, due to improper validation and escaping
- **CSRF**: attackers induce victims to perform actions (i.e., *HTTP requests*), they actually do not intend to perform 
**XSS** gives the attacker more freedom, and for this reason it is far more dangerous than **CSRF**.
Moreover, XSS implies CSRF, since all countermeasures taken for the latter can be canceled by exploiting the former.
# Impact
- CSRF in **password reset forms** can lead to an unpleasant moment for the victim
- CSRF in **money transfer forms** can lead to a **VERY** unpleasant moment for the victim
# Prevention
## CSRF Tokens
- Random and unpredictable strings associated to form with state-changing actions (POST, PUT, PATCH, DELETE)
- Generated and stored server-side. The one sent by the user and the one on the server must match, otherwise the request is dropped
- They should be unique for each session and form
## SameSite cookies
Attribute assigned to cookies
- 🔴 `SameSite=None`: the cookie is always transmitted (**BAD**) 
- 🟢 `SameSite=Lax`: the cookie is transmitted only if the request is triggered by top-level navigation or from the same domain (**BETTER** - *default in Chrome*)
- 🟢 `SameSite=Strict`: the cookie is transmitted iff the request is triggered by the same domain (**BEST** - but sometimes more flexibility is needed)
## Pay attention
CSRF countermeasures can be bypassed if the implementation is weak:
- Don't allow state-changing requests (e.g., password reset) to be carried out with **NON state-changing methods** (*GET*)
- If the requests come without a CSRF Token and you expect one, **DROP IT**
- Don't rely on client-side stuff (like expecting in the request the same CSRF Token both as a cookie and as a parameter), **ALWAYS DO CHECKS WITH DATA IN THE BACKEND**