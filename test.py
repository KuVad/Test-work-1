#array_first =['1234', '1567', '-2', 'computer science']
#array_first =['Russia', 'Denmark', 'Kazan']
array_first = ['Hello', '2', 'world', ':-)'] 
new_array = []
i = 0

print(array_first)
while i < len(array_first):
    if len(array_first[i]) <= 3:
        new_array.append(array_first[i])
    i += 1
print(new_array)