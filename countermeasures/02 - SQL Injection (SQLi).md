### ==**Prepared Statements**==
 - Use well established libraries
 - "*It will not work if you concatenate strings while creating the prepared statements!*" - I don't even know what that can possibly mean.

### ==**Evergreen recommendations**==
- Validate input coming from outside the trust boundary (e.g., user, database)
- Use domain primitives (yes, the ones from Secure Software Design) for input and output. If some content is invalid it shouldn't even exist!

### CAUTION!
There exist automation tools (like **SQLMap**) that can automatically find vulnerabilities in SQL implementation.