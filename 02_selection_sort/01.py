# arr = [5, 4, 3, 2, 1]
# n = len(arr)

# for i in range(n-1):
#     min = i

#     for j in range(i+1, n):

#         if arr[j] < arr[min]:

#             min = j

#     arr[i], arr[min] = arr[min], arr[i]

# print(arr)


class SelectionSort:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min = i

            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]

        return arr
    def main(self):
        n = int(input("Enter number of elements: "))
        arr = []

        for i in range(n):
            arr.append(int(input(f"elements {i}: ")))
        print(arr)

        res = self.selection_sort(arr)
        print("the result of selection sort is: ", res)

obj = SelectionSort()
obj.main()            


          




