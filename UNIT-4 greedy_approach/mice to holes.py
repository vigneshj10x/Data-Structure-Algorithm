def assign_mice_to_holes(m,h):
    m.sort()
    h.sort()
    time=0
    for i in range(len(m)):
        time=max(time,abs(m[i]-h[i]))
    return time

mice  = [4, -4, 2]
holes = [4, 0, 5]

print("Minimum time required:", assign_mice_to_holes(mice, holes))
