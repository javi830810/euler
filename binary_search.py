
arr = [1,2,3, 4, 5, 6]

#In Place
def binary_search(elem, arr, init=None, end=None):
    if not init and not end:
        init = 0
        end = len(arr)

    if  end < init or init >= len(arr):
        return False

    if init == end:
        return arr[init] == elem

    mid_point = (init+end)/2
    median = arr[mid_point]

    if elem == median:
        return True
    elif elem < median:
        return binary_search(elem, arr, init, mid_point)
    else:
        return binary_search(elem, arr, mid_point+1, end)

# Memory Cost
def binary_search_2(elem, arr):
    mid_point = len(arr)/2
    if not arr:
        return False
    elif mid_point == 0:
        return arr[0] == elem
    elif elem < arr[mid_point]:
        return binary_search_2(elem, arr[0:mid_point])
    else:
        return binary_search_2(elem, arr[mid_point:len(arr)])


print binary_search(5, arr)

print binary_search_2(5, arr)





# for x in arr:
#     print str(binary_search(x, arr)) + ' == ' + 'True'
