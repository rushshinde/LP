def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


# Take input from the user
data = input("Enter the elements of the array (space-separated): ").split()
data = [int(num) for num in data]  # Convert input strings to integers
size = len(data)

selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
