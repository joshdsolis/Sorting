# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) .
        for j in range(1, len(arr)-1):
            second_cur_index = j
            next_smallest = second_cur_index



        # TO-DO: swap
            if arr[smallest_index] > arr[next_smallest]:
                x = arr[smallest_index] 
                arr[smallest_index] = arr[next_smallest]
                arr[next_smallest] = x


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr