h = int(input())
m = int(input())
s = int(input())
a = int(input())
seg_total = h * 3600 + m * 60 + s + a

h = seg_total // 3600
while h > 24:
    h = h % 24

m = (seg_total - seg_total // 3600 * 3600) // 60
s = seg_total - seg_total // 3600 * 3600 - m * 60

print(h)
print(m)
print(s)
