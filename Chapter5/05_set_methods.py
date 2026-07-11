s1 = {1, 58, 89}
s2 = {57, 23, 16, 89}
small_set1 = {1,58}
small_set2 = {16, 89}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(small_set1.issubset(s1))
print(small_set2.issubset(s2))
print(s1.issuperset(small_set2))
print(small_set1.isdisjoint(small_set2))