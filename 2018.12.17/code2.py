numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = []
even = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
        odds.append(i)
    else:
        even.append(i)

print(odds)
print(even)