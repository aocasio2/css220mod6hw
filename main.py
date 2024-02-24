lst = [4, 2, 7, 3, 8, 5]
smallest = lst[0]
largest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print("Smallest number:", smallest)
print("Largest number:", largest)
