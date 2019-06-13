def counting_votes(arr):
    for i in range(len(arr)-1):
        most = arr.count(arr[i])
        name_most = arr[i]
        if most <= arr.count(arr[i+1]):
            most = arr.count(arr[i+1])
            name_most = arr[i+1]
    return name_most