students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for elements in students:
	print elements["first_name"], elements["last_name"]

print
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for elements in users:
 	print elements
 	test = users[elements]
 	count = 1
 	for items in test:
 		name = items["first_name"].upper() + ' ' + items["last_name"].upper();
 		print str(count) + ' - '+ name + ' - ' + str(len(items["first_name"] + items["last_name"]))
 		count += 1
 	print