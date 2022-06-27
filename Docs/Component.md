---
tags: class
---

# Component Class
A template class that implements all algorithm basis of TagTree

# Initialization
- `ComponentName` 
	- type: string
	- default: 'Component'
Tag name
---
- `indentationSize`  ^a81c59
	- type: int
	- default: 2
	Indentation size
---
- `indentation`  ^6e039b
	- type: int
	- default: 0
	Indentation level when it's render
---
- `noSlashAtEnd`
	- type: bool
	- default: False
	Remove slash for self closed tags

# Methods
- `push`
	Add a child to Tag ^pushDescription
	- params:
		- `item`
			- type: Component class object
			- default: None
	- return:
		- type: None
---
- `pop`
	Remove a child from Tag ^popDescription
	- params:
		- `id`
			- type: string
			- default: None
	- return:
		- type: None
---
- `__renderIndentation`
	Render the indentation in spaces based on previously defined  [[Component#^a81c59|indentation size]]
	- params:
		- `size`
			- type: int
			- default: -1
			If -1, the rendered value will be the default [[Component#^a81c59|indentation size]]
	- return:
		- type: string
---
- `addIndentation`
	Add one more level to initial indentation defined in [[Component#^6e039b|indentation param]]
	- parms:
		- `fatherIndentation`
			- type: int
			- default: None
			Father basis indentation needed when tags are into tag trees
		- return:
			- type: None
---
- `removeIndentation`
	Remove one level from initial indentation defined in [[Component#^6e039b|indentation param]]
	- parms:
		- `fatherIndentation`
			- type: int
			- default: None
			Father basis indentation needed when tags are into tag trees
		- return:
			- type: None
---
- `genContent`
	Return a string with formatted configs of tree ^genContentDescription
	- params:
	- return: 
		- type: string