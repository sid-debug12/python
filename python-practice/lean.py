first = True
sec = False

case1 = not first
case2 = not sec
case3 = first or sec
case4 = case1 or sec
case5 = first or case2
case6 = case1 or case2

print(case1)
print(case2)
print(case3)
print(case4)
print(case5)
print(case6)
