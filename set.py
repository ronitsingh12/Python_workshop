employees = ['Corey','Jim','Steven','April','judy','Jenn','John','Jane']

gym_members = ['April','John','Corey']

developers = ['judy','Corey','Steven','Jane','April']

set_developers = set(developers)
set_gym_members = set(gym_members)
result = set_gym_members.intersection(set_developers)
result1 = result.intersection(employees)
print("Intersection is :- ",result1)