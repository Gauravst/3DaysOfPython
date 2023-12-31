# dictionaries and dictionaries methods

a = {}

b = {
	'name' : 'gaurav',
	'class' : '12th',
  'subject' : {
		'maths' : 45,
		'hindi' : 56
	}
}

print(b)
print(b['name'])
print(b['subject']['hindi'])
print(b.get('name'))
print(b.keys())
print(b.values())
print(b.items())