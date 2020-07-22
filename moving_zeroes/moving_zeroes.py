'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new_arr1 = []
    new_arr2 = []
    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr1.append(arr[i])
        elif arr[i] == 0:
            new_arr2.append(arr[i])
    new_arr = new_arr1 + new_arr2
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")