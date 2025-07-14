def binary_search(numbers,key_value):
    start_index = 0
    end_index = len(numbers) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) //2 #discard any decimal

        mid_value = numbers[mid]

        if mid_value == key_value:
            return mid
        elif key_value > mid_value:
            start_index = mid + 1 #+1 coz list is in ascending order
        elif key_value < mid_value:
            end_index = mid- 1 #if element is less than mid value
    return -1

if __name__ == '__main__':
    key_value = 88
    numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    index =binary_search(numbers= numbers , key_value = key_value)
    print(f"Element {key_value} found at position:{binary_search(numbers, key_value)}")


