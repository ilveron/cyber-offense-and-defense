# Command injection
**Validation** is the keyword here!
- Use **allow lists** in favor of disallow lists
- Check whether the input and the output make sense
# File upload vulnerabilities
Also here prefer using **allow lists** instead of disallow lists over file extensions, since they could work at first but then be useless if a newer file extension comes around (e.g., you disallowed .php but then .php5 came into play).

#### Other suggestions
- Validate filenames against path traversal (***use filesystem APIs***)
- Avoid collisions by renaming uploaded files to have unique filenames (***UUIDs***)
- "*Quarantine*" files in a **temporary filesystem** until they are fully validated
- Use well-known and trustworthy frameworks for pre-processing file uploads (e.g., Django)
