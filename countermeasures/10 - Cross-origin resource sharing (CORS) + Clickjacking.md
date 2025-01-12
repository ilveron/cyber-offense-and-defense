# Cross-origin resource sharing (CORS)
CORS is a mechanism implemented **in browsers** to avoid accessing resources coming from undesired locations (i.e., *origins*).
It is a relaxation of the **Same-Origin Policy** (SOP)
## What is an origin
![[Pasted image 20250112163402.png]]
## Same-Origin Policy (SOP)
The SOP is the **default** origin policy in browsers.
As the name might suggest, it only allows access to resources within the same origin.
#### Example
A script in `https://example.com` can only access to resources coming from the exact same origin (i.e., `https://example.com`).
Even `https://api.example.com` and `http://example.com` are considered a different origins.

It is good to have a strict default policy, but many times web applications need to request and access resources from external application (e.g., to consume an API)
## Relaxing SOP (by implementing CORS)
Browsers add the `Origin: <your_origin_here>` header in the HTTP request, and expect the header `Access-Control-Allow-Origin: <that_same_domain_here>` in the HTTP response. If the origin is not listed in the response header the browser won't allow access to the resources of the response (even if the response reached the user).

Obviously in the backend there should be some mechanism to avoid processing the request if the origin isn't part of an allow list.
#### Wildcards
Wildcards can be used to avoid listing a big number of origins in the response header.
1) Say we wanted to include all subdomains of `https://example.com`
	We could add the following header to the response:
	`Access-Control-Allow-Origin: https://*.example.com`

2) Say we wanted to include every possible origin
	`Access-Control-Allow-Origin: *`
### Prevention
#### ⛔ DON'T
Pay attention, you **MUST NOT DO** what's stated below
- Use `Access-Control-Allow-Credentials: true`. It allows access to cookies and authentication headers. 
- Use `Access-Control-Allow-Origin: null`. It allows the null origin, effectively disabling CORS (as anyone can put `Origin: null` in the request headers)
- Reflect blindly the request's origin in the response header, as this would also disable CORS
- Use flawed regexes to validate the origin. 
#### ✅ DO
- Specify the `Access-Control-Allow-Origin` header if the response contains sensitive data
- Use allow lists in the backend (the one populating the `Access-Control-Allow-Origin` header)
- Think deeply if you really need `Access-Control-Allow-Origin: *`
- Meditate profoundly if you really need `Access-Control-Allow-Crendentials: true`
#### Headers incompatibility
`Access-Control-Allow-Origin: *` and `Access-Control-Allow-Crendentials: true` are incompatible, since the latter requires origins to be specified (no wildcards).
Browsers will throw CORS errors if both are used.
# Clickjacking
The attacker tricks a user into clicking on something different from what the user perceives, potentially causing them to unknowingly perform unintended actions on another website by embedding a hidden, transparent iframe over a legitimate and harmless page.
### Prevention
There exist specific headers to disable framing:
- `X-Frame-Options: DENY`
- `X-Frame-Options: SAMEORIGIN`

Content Security Policies (CSP) can be also used to disable use in frames. 
**MORE SECURE THAN THE METHOD ABOVE**
- `Content-Security-Policy: frame-ancestors 'none';`
- `Content-Security-Policy: frame-ancestors 'self';`
- `Content-Security-Policy: frame-ancestors 'self' *.example.com;`
Also these allow granular control over iframe embedding

Also SameSite policies for cookies can be used to prevent unauthorized cookie usage in iframes.
- `Set-Cookie: [...]; SameSite: Strict;`
- `Set-Cookie: [...]; SameSite: Lax;`
