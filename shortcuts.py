def renamed_method(used):
    print(used)


def another_method(obj):
    print(obj)


if renamed_method('use_it') is not None:
    pass
renamed_method('dont_use_it')

numbers = [7, -1, 2, 5]


def bubble_sort(arr):
    for j in range(len(numbers)):
        for i in range(0, len(numbers) - j - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]


bubble_sort(numbers)



