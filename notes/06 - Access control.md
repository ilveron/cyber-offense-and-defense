We are talking about **authorization** (AuthZ)
Policies are set of constraint made of triples `(Subject, Object, Role)` where:
- **Subject**: User, group, role...
- **Object**: A resource of the system, another user, the policy constraint themselves...
- **Access right**: read, write, execute...

Policies are often combined (i.e., not mutually exclusive). Sometimes this can be a bad idea.

# Access control formulas
## Discretionary Access Control (DAC)
The owner of a resource states who has and who hasn't certain access rights to his resource (Pretty classic, used in UNIX)
### Implementations
#### Access Matrix
- **Objects** (resources) on columns
- **Subjects** (users) on rows
#### Access Control List (ACL)
It's the Access Matrix decomposed by **columns**
e.g., File1 -> (UserA, rw), (UserC, r) - *UserB has no access rights on File1* 

*Perfect for checking the access rights of all the users per **each resource**

#### Capability Tickets
It's the Access Matrix decomposed by **rows**
e.g., UserA -> (File1, `rw-`), (File2, `r--`) - *no access rights on File3*

*Perfect for checking the access rights of **each user** over all the resources*

#### Authorization Tables
Best of both worlds
A table made of triples: `(Subject, Access Mode, Object)`
- **Filter by subject** and you get **capability tickets**
- **Filter by object** and you get an **ACL**
## Mandatory Access Control (MAC)
- Subjects are given **security clearances** (*access level*)
- Objects are given **security labels** (critical level)
**Subjects** can access **Objects** having critical level less or equal ($\le$) than their clearance level
Emerged for military security. Usually computer systems need more flexibility
### Examples
Given the subjects:
- **UserA**: clearance level 3
- **UserB**: clearance level 2
- **UserC**: clearance level 1

Given the objects:
- **File1**: critical level 2
- **File2**: critical level 3
- **File3**: critical level 2
- **File4**: critical level 2

The access rights are as follows:
- **UserA** can access all the files (**File1**, **File2**, **File3**, **File4**)
- **UserB** can access **File1**, **File3** and **File** 4
- **UserC** can't access any of the files
## Role-Based Access Control (RBAC)
Restricts system access to authorized users based on their assigned roles within an organization
- Simple, yet powerful!
- The set of roles is usually relatively static
- The associations between users and roles, instead, may change frequently
- Assigning access rights to roles results in a more stable policy
![[Pasted image 20250109124650.png]]
## Attribute-Based Access Control (ABAC)
Grants access to resources based on the attributes of users, resources, and the environment, allowing for more granular and dynamic access decisions.

- Powerful but expensive
- Ok for web services, where latency isn't crucial

### Example
Let's say we have the user:
- Name: Teenager
- Age: 16

And the resource:
- Name: You don't want your child to see this movie
- Minimum Age: 18

The user does not fit the age requirement (Age >= Minimum Age), hence they cannot access the movie.
# Problems
## Broken Access Control
Access Control is broken when users can access resources that they are not supposed to.

- **Vertical privilege escalation**: gain access to higher level (more critical) functionalities
- **Horizontal privilege escalation**: gain access to resources of "same level" users
### Insecure Direct Object Reference (IDOR)
Missing access control on a resource that can be accessed by directly referencing the object ID![[Pasted image 20250109151914.png]]

# Prevention
- Obfuscation alone will not be enough
- Secure defaults
	- **Deny access** by default
	- Authorize **only admins** by default
- **Don't mix** access control mechanisms!
- Test, **PLEASE TEST**!