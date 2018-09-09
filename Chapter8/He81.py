#
def TripleHop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    return TripleHop(x - 3) + TripleHop(x - 2) + TripleHop(x - 1)

print TripleHop(1)
print TripleHop(2)
print TripleHop(3)
print TripleHop(4)
print TripleHop(5)
print TripleHop(6)

# print Method2(1)
# print Method2(2)
# print Method2(3)
# print Method2(4)
# print Method2(5)
# print Method2(6)
