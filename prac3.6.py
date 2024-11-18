
from numpy import diff


my_set = {1, 2, 3, 4}

my_set.add(5)
my_set.remove(3)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print(set1)
print(set2)
print(union_set)
print(intersection_set)
print(difference_set)