a = [1,2,3,4]
su = []
for start in range(len(a)):
    for stop in range(start + 1, len(a) + 1):
        su.append(a[start:stop])

print(su)