def bucket_sort(arr):
    if len(arr)==0:
        return arr
    max_value,min_value=max(arr),min(arr)
    bucket_range=(max_value-min_value)/len(arr)
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index=int((num-min_value)/bucket_range)
        if index == len(arr):
            index-=1
        buckets[index].append(num)
    sorted_arr=[]
    zfbzsfb
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr

arr=[45,21,9,32,58,33,47]
sorted_arr = bucket_sort(arr)
print("Sorted Array:", sorted_arr)