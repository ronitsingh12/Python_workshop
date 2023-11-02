# A set is an  unordered collection of unique elements in python.
# 1.
# Adding Elements
# my_set = {1,2,3}
# my_set.add(9)
# print(my_set)

# 2.
#Removing Elements
# my_set.remove(2)
# remove gives error if i remove an element does not exist
# print(my_set)
# discard doesn't give error if i remove an element does not exist
# my_set.discard(3)
# print(my_set)

# 3.
# adding more than 1 element in set
# myset = {5,6}
# a = my_set.union(myset)
# print(a)

#4.
set1 = {1,3,6}
set2 = {2,3,1,4,5}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set2.difference(set1)
symmetric_difference_set = set1.symmetric_difference(set2)
print(union_set)
print(intersection_set)

print(difference_set)
print(symmetric_difference_set)

# 5.
def find_intersection():
    find_intersection = set1.intersection(set2)
    return find_intersection
print(f"Intersection is : {find_intersection()}")