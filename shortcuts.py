def renamed_method(used):
    print(used)


def another_method(obj):
    print(obj)


renamed_method('use_it')
renamed_method('use_it_again')

arr = [1, 2, 5, 7, -3]


def swap():
    arr[i], arr[i + 1] = arr[i + 1], arr[i]


for j in range(len(arr)):
    for i in range(0, len(arr) - j - 1):
        if arr[i] > arr[i + 1]:
            swap()
