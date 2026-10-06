class Main:
    def bubble_sort(self, arr):
    
        n = len(arr)
        for i in range(n-1):
            swap = False
    
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True 
    
            if not swap:
                break
        return arr
    def main(self):
        n = int(input("enter number of elements: "))
        arr = []
        for i in range(n):
            arr.append(int(input(f"enter ele {i}: ")))
        ans = self.bubble_sort(arr)
        print("array is",arr)    
        print("sorted array is",ans)

obj = Main()
obj.main()


            


