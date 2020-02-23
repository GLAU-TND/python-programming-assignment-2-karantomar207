x = eval(input())
b = [min(x)]
a = min(x)[-1]
x.remove(min(x))
for i in x:
    for j in x:
        if a == j[0] and j[-1] != b[0][0]:
            b.append(j)
            a = j[-1]
            x.remove(j)
            break
b = b + x
print(b)
