lst = [1, 2, 3, 5, 6, 7, 9]

for i in range(len(lst)):
    if lst[i] != i + 1:
        print("Smallest missing element:", i + 1)
        break
