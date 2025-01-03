class Solution:
 
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            # Sort first and second halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
    
    def merge(self, arr, l, mid, r):
        # Create temp arrays
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]
        
        i = 0
        j = 0
        k = l
        
        # Merge the temp arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy the remaining elements of left[], if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right[], if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1