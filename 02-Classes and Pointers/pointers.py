num1 = 14

num2 = num1
print('Before num2 is updated')
print('num1 =', num1)
print('num2 =', num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print('\nAFter num2 is updated')
print('num1 =', num1)
print('num2 =', num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# dictionary test with pointers

dict1 = {
    'value': 11
    }

dict2 = dict1 # pointer created

print("\nBefore value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 12

print("\nAfter dict2 value is updated.")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))