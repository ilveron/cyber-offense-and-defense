# Information disclosure
#### Identify all sensitive information within your domain (and application)
- Audit code for potential information disclosure
- Don't hardcode credentials and sensitive information
#### Use generic error messages
- Implement a global exception handler
- ==DO NOT== use stack traces
#### Debugging and diagnostic features must be disabled
- Double check by testing for them in the deployed system
#### Use configs and third-party technology ==iff== you understood them well
# Directory traversal
#### DOs ✅
Use **FileSystem APIs**, get the canonical form of the path and ==validate it== following your business rules
#### DON'Ts ❌
- Use strings
- Reject strings solely by the presence of `../` => One can use an absolute path
- Remove any `../` (non recursively) => One can use `....//`, which after sanification becomes `../`
- Only accept paths with a given prefix => One can satisfy the constraint and still do whatever
- Only accept paths with a fixed suffix => One can use a null byte before the suffix, effectively nullifying it