
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(l,r):
    result = []
    i=j=0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i]); i+=1
        else:
            result.append(r[j]); j+=1
    result.extend(l[i:])
    result.extend(r[j:])
    result.extend(r[j:])
    return result

if __name__ == "__main__":
    data = [12,11,13,5,6,7]
    print("Input:", data)
    print("Sorted:", merge_sort(data))
