#examples for demo-ing list manipulation

simple_list = [1,2,3,4]
simple_list.extend([5,6,7,8])
#delete function: del()
del(simple_list[0]) #deletes first element
del simple_list[0] #alternate syntax


print('simple_list = ', simple_list)
#dictionary
d = {'name': 'Brian', 'age': 33, 'race': 'blanco'}
print(d.items()) #yeilds list of dict items as tuples
#use case
for key, val in d.items():
    print('key, val = ', key, ',', val)
del d['name']
print(d.items()) #yeilds list of dict items as tuples

#tuple
#has less methods than d
#cannot use del on tuple b/c tuples are immutable
t = (1,2,2,3)
print(t.count(2))

#set
s = {'Brian', 'David', 'Alex', 'Brian'}
print(s)
# only prints "Brian" 1x cuz sets are for unique values

