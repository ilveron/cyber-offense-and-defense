# Server-side Request Forgery (SSRF)
It's a vulnerability that lets attackers send requests on behalf of a server.
By being able to do that attackers gain privileged positions on a network, bypass firewalls and access internal services.

## Impact
- Unauthorized leaks
- Data leakage
- Access other internal nodes of the network
- Access other backend systems
- Arbitrary Remote Command Execution (RCE)
- Use targeted servers as proxies to attack third-party systems
If the server serves an API for contacting other endpoints, and the API doesn't properly validate the input address. Problems will come, for sure.
## Usages
### SSRF attacks against the server itself
Usually SSRF arises for weak default configurations, wrong assumptions (like thinking that only trusted users can do requests from the server machine) and excessive trust.

### SSRF attacks against other backend systems
Since there wouldn't be any way to **distinguish** a request sent by **someone operating on the physical machine** and a request sent **via an API**, in the latter, allow/disallow list should be used and, just in case, sensitive internal nodes (*to which the attacked server has special privileges*) should authenticate the requester.
## Prevention
You can either use:
- **Allow lists**: Allow iff the URL **is** in the list
- **Disallow lists**: Allow iff the URL **is NOT** in the list
Obviously you should prefer allow lists, but sometimes keeping track of all the URL you should allow is impossible.
**In that case at least exclude internal and sensitive nodes!**

### Prevent bypasses
#### Disallow lists
There could be many representations of the same information (e.g., 127.0.0.1, 213070643, 017700000001 and 127.1 are all representations for *localhost*).

To prevent this, before doing any validation, **be sure** that the input is in canonical form!
#### Allow lists
They arise when regexes are used improperly.
**Always check fullmatch** instead of starts with/ends with

### Open redirects
**DO NOT ALLOW** external links in open redirects, as responses can carry auth tokens.
# XXE Injection
The problem here is mainly the usage of DTD (Document Type Definition).
If users can provide them (and they are processed), data can be leaked, DoS attacks can be launched etc...
## Prevention
Don't rely on defaults for XML, always check them.
Moreover:
- Disable inline DTD processing
	- Validate against a local DTD (or XML Schema)
- Disable XML serialization
	- Use JSON

 If you must use inline DTD:
- Disable external entities
- Set time and memory limits ([Billion laughs attack](https://en.wikipedia.org/wiki/Billion_laughs_attack))
- Sandbox the process