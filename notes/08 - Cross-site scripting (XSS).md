Via XSS, attackers can execute custom scripts on a victim's browser due to improper validation and escaping.
# Categories
## Reflected XSS
The malicious script comes with the request and its effects are reflected in the response.
Attackers forge malicious requests and induce the victim to send that request
## Stored XSS
It is more severe than the other ones.
Done in two steps:
- The script is initially stored in the database by the attacker
- The script is then served to all users who request the resource on which it is stored
One malicious script can damage many users simultaneously and, more importantly, it doesn't need voluntary actions performed by the victim
## DOM-based XSS
Similar to Reflected XSS, its peculiarity is that it does not involve the backend server in any way, it's all done within the browser.
## Blind XSS

> [!QUOTE]
> "A stored XSS executed in another part of the application or in
> another application that you cannot see (like second-order SQLi).
> For example, malicious script sent via feedback forms and
> executed by the administrator in the dashboard."

Basically a Stored XSS whose effects can't be tested as the script is stored in an unspecified location (see the example in the quote above)
# Prevention
- Use the **HttpOnly** flag on cookies that don't need to be accessed by JavaScript (especially session cookies).
- **Validate** input!
	- Don't bother to sanitize that much (*reject strings at the moment in which you find out there's something wrong with them*)
- **Escape** the output
- Use well established libraries and frameworks (*e.g., Svelte, Angular ecc...*)
- Use a **Content Security Policy** (CSP)
	-  A good starting point for a CSP would be the following:
		- `default-src 'self'; // Blocks loading of resources from other domains.`
		- `script-src 'self'; // Blocks execution of scripts from external sources (including inline scripts).`
		- `object-src 'none'; // Blocks loading of objects.`
		- `frame-src 'none'; // Blocks embedding of the page in frames and iframes.`
		- `base-uri 'none'; // Blocks the use of the <base> tag.`
# Bypass filters
- Filters may be case sensitive, use `<Script>` instead of `<script>`
- Encode chars or strings that are disabled