# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is 
# used to implement Insertion Sort.

class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]        # element we want to insert
            j = i-1           # index that scans the sorted part (left side)
    
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
    
            arr[j + 1] = key