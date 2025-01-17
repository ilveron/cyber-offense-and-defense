## Single Sign-On (SSO)
Is an authentication process that allows users to authenticate on multiple services by using a **single set of** data and **credentials**.
## OAuth
OAuth is an authorization framework that enables **third-party applications** to obtain access to **limited set** of the user's resources on a server **without sharing** the user's **credentials**.

### A brief example
Let's start break down how OAuth works by providing an example. 
We need to authenticate users for our application "NoteShare".
For our purposes we just need to know these information about the user: full name and email.
Most people have a Google account. Google has all the information we need about the user. Google provides an OAuth service to share with us their data. Great!

### Keywords
#### Involved parties
- **User**: the one using the service
- **Service Provider**: the one who needs to authenticate the user (in the example - *NoteShare*)
- **Identity Provider**: the one providing the service with user's data (in the example - *Google*)
#### Parameters
##### Request (Service Provider -> Identity Provider)
- **client_id**: The unique identifier for the application requesting access.
- **client_secret**: A confidential key used to authenticate the application. Provided when the service is registered (like an API key).
- **redirect_uri**: The URL to which the user will be redirected after authorization.
- **response_type**: The type of response desired (e.g., code, token).
- **scope**: The permissions requested by the application (i.e., the set of user's data requested - in the case of the example, full name and email).
- **state**: A value used to maintain state between the request and callback. You may compare it to a CSRF token.
- **grant_type**: The type of grant being used (e.g., authorization_code, client_credentials).
- **code**: The authorization code received from the authorization server (only in code grant type).
##### Response (Service Provider <- Identity Provider)
- **state**: see above
- **access_token**: The token used to access protected resources.
- **refresh_token**: A token used to obtain a new access token when the current one expires.
- **token_type**: The type of token issued (e.g., Bearer).

### Flows
#### 🟢 Code grant
- Once the **authorization code** is sent to the **Service Provider** (*step 3*), all communications are done backend-to-backend (*dotted lines*)
![[Pasted image 20250114193334.png]]

#### 🔴 Implicit grant
- **Less secure**, usually used in single-page apps
- The access token is stored in the browser
- Deprecated in favor of **Proof Key for Code Exchange** (PKCE - "pixie")
- If service provider and identity provider are hosted in **the same domain**, use session-based authentication, as it's **safer**
![[Pasted image 20250114193443.png]]
## Vulnerabilities & Prevention
Vulnerabilities usually arise due to the flexibility and vague (by design) specificiation of OAuth. *Many configuration settings that are necessary for keeping users' data secure are optional*.
- **USE ALLOW LISTS** - both to mitigate open redirects (token theft) and improper validation
- **DO NOT** experiment with custom implementations, there exist well established libraries
- **DO NOT** put excessive trust in confidentiality of tokens stored in browsers
	- There is no way to make implicit grant 100% safe
		- If there's XSS, tokens can be stolen (as it is all done via the browser)
	- Browser memory > Session storage > Application storage > Cookies
		- 🔴 **Cookies** are transmitted with every request
		- 🔴 **Application storage** is shared across multiple tabs

