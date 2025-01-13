# Insecure deserialization
Many languages use mechanisms to serialize and deserialize objects for storing and transfering them. These mechanisms are often unsafe.

By using deserialization, you are allowing users to have control over objects in your application. This can be utterly dangerous, as deserialization bypasses validation processes.

## Structure (in PHP)
Here follows an example of a serialized object
`O:3:"Car":4:{s:5:"brand";s:4:"Ford";s:5:"model";s:6:"Fiesta";s:4:"year";i:2018;s:5:"price";d:16570.15}`

Its correspondent class and deserialization:
```
<?php
	class Car{
		public $brand;
		public $model;
		public $year;
		public $price;
	}

	$brand = "Ford";
	$model = "Fiesta";
	$year = 2018;
	$price = 16570.15;
?>
```

In detail:
```
// An object of class Car, with 4 properties
0:3:"Car":4:{[...]}  

// Has a property named "brand", to which is assigned the string value "Ford"
[...]{s:5:"brand";s:4:"Ford";[...]}

// Has another string value ("Fiesta")

// Has a property named "year", to which is assigned the integer value 2018
[...]{[...];s:4:"year";i:2018;[...]}

// Has a property named "price", to which is assigned the float value 16570.15
[...]{[...];s:5:"price";d:16570.15;}
```
## Problems
If users have control over data that is deserialized, there's **nothing** that can prevent them from tampering with that object, **except** by adding some form **cryptographic signature**, but *why even bother*? 
## Prevention
🔴 Just **don't use** serialization/deserialization.
🟢 Use instead JSON encode/decode methods instead.
# Server-Side Template Injection (SSTI)
They occur when user input is concatenated as text directly into a template.
If what is passed in is not escaped there's no way to distinguish user data from template text. That way an attacker can essentially have all benefits of XSS + RCE: **a disaster**!

## Correct use of a template
This way user input is properly escaped and treated as bare data
![[Pasted image 20250113115438.png]]
## Incorrect use of a template
Far West!
![[Pasted image 20250113115528.png]]
## Prevention
🔴 Do not process user templates server-side
🔴 Do not concatenate user strings with the template
🟢 Use data bindings
🟢 If you must process template server-side, sandbox and disable dangerous modules. (Probably it's better not to allow sensitive data to travel to the client for processing)
🟢 Implement an allow list for allowed attributes

