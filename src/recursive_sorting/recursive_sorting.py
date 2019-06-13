# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    nA = 0
    nB = 0
    for i in range(0, elements):
        if nA >= len(arrA):   # all elements in arrA have been merged
            merged_arr[i] = arrB[nB]   
            nB += 1     
        elif nB >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[nA]
            nA += 1
        elif arrA[nA] < arrB[nB]:
            merged_arr[i] = arrA[nA]
            nA += 1
        else:
            merged_arr[i] = arrB[nB]
            nB +=1
    return merged_arr

merge([1,3,5], [2,4,6])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        arr = merge(left, right)
    return arr




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
