arr = [1,0,2,0,1,0,3,1,0,2]
l = len(arr)

def left(arr, l):
    fn_count = [arr[0]]
    for i in range(l-1):
        fn_count.append(max(fn_count[i], arr[i+1]))
    return fn_count

def right(arr, l):
    fn_count = [0 for x in range(l) ]
    fn_count[-1] = arr[-1]
    for i in range(l-2, -1, -1):
        fn_count[i] = max(fn_count[i+1], arr[i])
    print(fn_count)
    return fn_count

def find_water(left, right, height, l):
    water = 0
    for i in range(l):
        water = water + min(left[i], right[i]) - height[i]
    return water

left_arr = left(arr,l)
right_arr = right(arr,l)
water_sum = find_water(left_arr, right_arr, arr, l)

    
print(water_sum)