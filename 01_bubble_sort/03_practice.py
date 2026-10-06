# class Bubble:
#     def bubble_sort(self, arr):

#         n = len(arr)

#         for i in range(n-1):
#             swap = False

#             for j in range(n-i-1):
#                 if arr[j] > arr[j+1]:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#                     swap = True

#             if not swap:
#                 break 
#         return arr

#     def main(self):
#         n = int(input("Enter the number of elements: "))
#         arr = []
#         for i in range(n):
#             arr.append(int(input(f"element: {i}  ")))
#         print("arr: ", arr)
#         res = self.bubble_sort(arr)
#         print("bubble result: ", res)     

# obj = Bubble()
# obj.main()                   


arr=[5, 6,4,2,8,8, 9]
n = len(arr)

for i in range(n):
    swap = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True

    if not swap:
        break 

print(arr)           