import set_module

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Union:", set_module.union(set1, set2))
print("Intersection:", set_module.intersection(set1, set2))
print("Difference:", set_module.difference(set1, set2))
print("Symmetric Difference:",
      set_module.symmetric_difference(set1, set2))
