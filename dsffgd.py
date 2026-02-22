my_set = set()
my_set = set( ['apple', 'cherry', 'mango'] )

my_set = { 'apple', 'cherry', 'mango', 'mango' }

print(my_set)
print(type(my_set))

# print(my_set[0])
# my_set[1] = 'pamelo'

print(len(my_set))

new_set = {True, 1, 0, False}
print(len(new_set))
print(new_set)

for item in my_set:
    print(item)

print('apple' in my_set)
print('banana' not in my_set)
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

intersection = first.intersection(second)
intersection = first & second # оператор &

print(intersection)

# union = first.union(second)
# union = first | second # оператор or
# print(union)
print(first)
print(second)
first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}

intersection = first.intersection(second)
intersection = first & second # оператор &

first.intersection_update(second)

print(intersection)
contacts = {
    'Антон': '0506959068',
    'Ліза': '0474838458',
    'Сергій': '0550404033'
}

print(contacts['Ліза'])
contacts['Сергій'] = '0650499596'
print(contacts['Сергій'])

contacts['Настя'] = '0500440405'
print(contacts['Настя'])

contacts.update({'Антон': '0670450044', 'Тимофій': '0897477744'})

print(contacts)
print(contacts.keys())
print(contacts.values())
print(contacts.items())

for i in contacts:
    print(f"{i}: {contacts[i]}")