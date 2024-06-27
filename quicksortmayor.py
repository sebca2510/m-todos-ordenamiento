def quicksortmayor(arr):
    if len (arr) <= 1:
        return arr
    else:
        ref = arr[0]
        men = [x for x in arr[1:] if x <= ref]
        may = [x for x in arr[1:] if x > ref]
        return quicksortmayor(may) + [ref] + quicksortmayor(men)