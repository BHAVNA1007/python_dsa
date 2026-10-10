#bubble
# arr =[7, 2, 3, 1, 9, 6]
# n = len(arr)

# for i in range(n-1):
#     swap = False

#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#            arr[j], arr[j+1] = arr[j+1], arr[j]
#            swap = True
#     if not swap:
#         break
# print(arr)    


# selection
# arr = [8, 2, 1, 3, 5, 9, 4]
# n = len(arr)

# for i in range(n-1):
#     min = i
#     for j in range(i+1, n):
#         if arr[j] < arr[min]:
#             min = j
#     arr[i], arr[min] = arr[min], arr[i]

# print(arr)         
    

#insertion 
# arr = [8, 2, 1, 3, 5, 9, 4]
# n = len(arr)

# for i in range(1, n):
#     j = i-1
#     key = i

#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j-= 1
#     arr[j+1] = key    
# print(arr)




arr =[6,1,3,2,9,5,7]
n = len(arr)

for i in range(1, n):
    j = i-1
    key = i

    while j >= 0 and arr[j]> key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key  
print(arr)      