numbers = [5, 3, 4, 2, 1]
n = len(numbers)

for i in range(1, n):
    key = numbers[i]
    j = i-1

    while j >= 0 and numbers[j] > key:
        numbers[j+1] = numbers[j]
        j = j-1

    numbers[j+1] = key

print(numbers)

    


