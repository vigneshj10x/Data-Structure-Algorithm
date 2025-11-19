import heapq
def heap_sort(x):
    h=[]
    res=[]
    for i in x:
        heapq.heappush(h,i)
    while h:
        res.append(heapq.heappop(h))
    return res
print(heap_sort([3,2,1,5,4]))
