def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
#       print(array)
    return array


arr = [12, 11, 13, 5, 6]

print("Current array is:", arr)
new_arr = insertionSort(arr)
print("Sorted array is:", new_arr)
