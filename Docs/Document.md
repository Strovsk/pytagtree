---
tags: class
---

# Document Class
A compiler where all document high level tags are placed

# Initialization
- `allowOverride` 
	- type: bool
	- default: False
By default, all documents dont allow that an id can be used by two or more tags. Set this to True if you want use duplicate ids
---
- `globalIndent`
	- type: int
	- default: 2
	The indent used in all document
---
- `globalLineSize`
	- type: int
	- default: 150
	Max number of characters per line until 

# Methods
- `push`
	Add a child to Tag
	- params:
		- `item`
			- type: Component class object
			- default: None
	- return:
		- type: None
---
- `pop`
	Remove a child from Tag
	- params:
		- `id`
			- type: string
			- default: None
	- return:
		- type: None
---
- `__getContent
	Load the entire content of high level tags
	- params:
	- return:
		- type: string
---
- `printContent`
	Load a string content and print that to the console
	- params:
	- return:
		- type: string
- `saveContentTo`
	Save the content in 
	- params:
		- path:
			- type: string
			the local where to store the final content
	- return:
