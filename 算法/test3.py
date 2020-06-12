l = [1,2,3,4,6,7,8,9]

def binary_search(l,item):
    first = 0
    last = len(l)
    while first <= last:
        mid = (first + last) // 2
        if l[mid-1] == item:
            return True
        elif l[mid-1] < item:
            first = mid + 1
        elif l[mid-1] > item:
            last = mid - 1

    return False

print(binary_search(l,5))



def binary_sort(l,item):
    mid = len(l)//2
    if len(l) <= 0:
        return False
    if l[mid-1] == item:
        return True
    elif item > l[mid-1]:
        return binary_search(l[mid:],item)
    elif item < l[mid-1]:
        return binary_search(l[:mid-1],item)

print(binary_search(l,4))