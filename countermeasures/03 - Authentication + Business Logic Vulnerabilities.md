# Authentication
Use multiple (different) authentication factors, since by using only one you expose yourself exponentially one (password can be guessed, stolen, forgotten, smartcard/token can be lost or stolen etc.)
## Attacks prevention
#### Offline dictionary attacks
- Prevent unauthorized access to the password file
- Implement intrusion detection measures to identify a compromise

#### Specific account attack
- Lock out the account after a 5 failed login attempts (possibly just for some time)

#### Popular password attack
- Inhibit the use of common passwords
- Monitor authentication requests to identify patterns

#### Password guessing against single user
- Make passwords difficult to guess (minimum length, character set, no well-known words)

#### Workstation hijacking
- Invalidate sessions after a period of inactivity

#### Exploiting user mistakes (passwords written down, sharing of passwords, default passwords)
- User training, intrusion detection, multifactor authentication

#### Exploiting multiple password use
- User training


## How do authentication vulnerabilities arise?
Authentication vulnerabilities arise because of the implementation of weak authentication mechanisms (e.g., no protection against brute-force attacks), or for the presence of logic flaws leading to bypass authentication (*broken authentication*)

## Other suggestions
==NEVER EVER store users' password==, neither in clear nor encrypted!
Store instead the hash value of the password (cannot be reversed if the algorithm used isn't weak), and possibly hash the password multiple times, best if combined with a nonce (salt). The latter protects against replay attacks and attacks done via rainbow tables.

Avoid using easily guessable usernames (especially for high-privileged accounts), use random suffixes

## More prevention
#### Take care with user credentials
- Don’t store passwords
- Use HTTPS (redirect any HTTP request to HTTPS)

#### Don't count on users for security
- Implement an effective password policy

#### Prevent username enumeration
- Generic and identical error messages for invalid username or password

#### Implement robust brute-force protection
- Slow down attackers by issuing a CAPTCHA with every login attempt

#### Triple-check your verification logic
- Use well established libraries (don’t implement authentication by yourself!)

#### Don't forget supplementary functionality
- Should users be able to register by themselves?
- Is password reset/change properly implemented?

#### Implement proper multi-factor authentication
- Two is better than one… two different factors!

# Business Logic Vulnerabilities

## Some tips
- Understand the domain of the application
- Don't do implicit assumptions about the user behavior
- Don't do implicit assumptions about the behavior of other parts of the application
==DOMAIN DRIVEN DESIGN==!