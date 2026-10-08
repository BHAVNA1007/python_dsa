class InsertionSort:

    def insertion_sort(self, arr):

        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i-1
            

            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j-1

            arr[j+1] = key
        return arr 

    def main(self):
        n = int(input("enter number of element: "))
        arr = []

        for i in range(n):
            arr.append(int(input(f"Enter element {i}: ")))
        print(arr)

        res = self.insertion_sort(arr)
        print("the result of the insertion sort is: ", res)

obj = InsertionSort()
obj.main()        


