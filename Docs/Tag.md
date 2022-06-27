---
tags: class
---

# Tag Class
A class that extends and implements the [[Component]] class

# Initialization
- `tagName` 
	- type: string
	- default: None
Tag name
---
- `id` 
	- type: string
	- default: None
	All tags have an id by default. If the user not type one, the class will generate a random id
---
- `params` 
	- type: list of tuples or strings
	- default: None
	The tag params will be here. If you want a fake div with a _param_ equals 2 and _disabled_ param like this:
	```html
	<div param="2" disabled />
	```
	It means that passed params are:
	```python
	[('param', 2), disabled ]
	```

---
- `maxLenLine`  ^f8f0c8
	- type: int
	- default: None
	Max size of characteres in each line. If length is greater than max value, the algorithm will format final result breaking the content in another lines.
---
- `indentation` 
	- type: int
	- default: 2
	Indentation size (in spaces) when it's render
---
- `innerText`
	- type: string
	- default: None
	Tag placed into the tag. A div with _innerText_='something' will result:
	```html
	<div>something</div>
	```
---
- `noSlashAtEnd`
	- type: bool
	- default: False
	Remove slash for self closed tags
---
- `hideId`
	- type: bool
	- default: False
	The id exists to prevent infinite recursive calls in [[tree generation algorithm]]. It works like a unique attribute for tags. By default, the tag id is rendered in final content, but it can be hide setting _hideId_ to True

# Methods
- `getFormattedParams`
	Return the formatted [[Tag#^8f421e|params]] to be placed in final result based in [[Tag#^f8f0c8|max legth line]]. If it's exceed the limit value, it'll break the line.
	- params: 
	- return:
		- type: string
---
- `getFormattedValue`
	Return the formatted [[Tag#^bb31a7|inner text]] to be placed in final result based in [[Tag#^f8f0c8|max legth line]]. If it's exceed the limit value, it'll break the line
	- params: 
	- return:
		- type: string
---
- `push`
	extended from [[Component]] ![[Component#^pushDescription]]
---
- `pop`
	extended from [[Component]] ![[Component#^popDescription]]
---

---
- `genContent`
	extended from [[Component]] ![[Component#^genContentDescription]]
	