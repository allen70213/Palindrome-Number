x = input("請輸入數字: ")
z = str(x)

l, r = 0, len(z)-1
print(z)
while l < r:
    if z[l] != z[r]:
        print("false")
        break
    l += 1
    r -= 1
    if l == r:
        print("true")

