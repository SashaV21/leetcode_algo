s = input()

ans = 0
book = {}
i = 0

for j, l in enumerate(s):
    book[l] = 1 + book.get(l, 0)
    while len(book) > 2:
        book[s[i]] -= 1
        if book[s[i]]== 0:
            del book[s[i]]
        i += 1
    ans = max(ans, j - i + 1)

print(ans)