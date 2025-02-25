def meeting_rooms(intervals):
    data = []
    for interval in intervals:
        data.append((interval[0], 0))
        data.append((interval[1], 1))
    data.sort()
    count = 0
    for event in data:
        if event[1] == 0:
            count += 1
        else:
            count -= 1
    return count