# s = input()
# p = input()
#
# example = sorted(p)
# res = []
# left = 0
# for right in range(len(p), len(s) + 1):
#     wind = sorted(s[left:right])
#     print(wind, left, right)
#     if wind == example:
#         res.append(left)
#     left += 1
#
# print(res)

s = input()
p = input()
res = []

wind_dict = dict()
example_dict = dict()
count = 0

for i in range(len(p)):
    example_dict[p[i]] = 1 + example_dict.get(p[i], 0)

for item in s[0:len(p)]:
    wind_dict[item] = 1 + wind_dict.get(item, 0)

if wind_dict == example_dict:
    res.append(count)

for i in range(len(p), len(s)):
    wind_dict[s[i]] = 1 + wind_dict.get(s[i], 0)
    wind_dict[s[count]] -= 1
    if wind_dict[s[count]] == 0:
        del wind_dict[s[count]]
    count += 1
    if wind_dict == example_dict:
        res.append(count)

print(res)