n, k = map(int, input().split())

def find_positive(scores):
    n = len(scores)
    l, r = 0, n-1
    idx = -1
    while l <= r:
        mid = (l+r) // 2
        s = scores[mid]
        if s > 0:
            idx = mid
            l = mid + 1
        elif s <= 0:
            r = mid - 1
    return idx

def last_occurrence(scores, target):
    n = len(scores)
    l, r = 0, n-1
    idx = -1
    while l <= r:
        mid = (l+r) // 2
        s = scores[mid]
        if s == target:
            idx = mid
            l = mid + 1
        elif s < target:
            r = mid - 1
        else:
            l = mid + 1
    return idx


scores = list(map(int, input().split()))
target = scores[k-1]
idx = find_positive(scores) if target <= 0 else last_occurrence(scores, target)
    
print(idx + 1)

