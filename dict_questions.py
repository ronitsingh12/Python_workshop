# dict={0:10,1:20}
# dict[2] = 30
# print(dict)


# 2.
# dict1 = {1:10,2:20}
# dict2 = {3:30,4:40}
# dict3 = {5:50,6:60}

# # to concatenate 2 dictionaries, we use update function 
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)

# 3.

# for key,value in student.items():
#     print(f"{key} : {value}")

# 4.

# n = int(input("Enter :- "))
# d = {x : x*x for x in range(1,n+1)}
# print(d)

# 5.
# n = int(input("Enter :- "))
# d = {x : x*x for x in range(1,n+1)}
# print(d)

# 8.
# my_dict={'data1':100,'data2':-54,'data3':247}
# my_dict1 = my_dict["data1"] + my_dict["data2"] + my_dict["data3"]
# print(my_dict1)
#          or
# print(sum(my_dict.values()))

#12.



#Write a python script to check whether given key already key exists in a dictionary
# d = {1:10,2:20,3:30,4:40,5:50,6:60}
# d = {1:10,2:20,3:30,4:40,5:50,6:60}
# n = int(input("Enter :- "))

# if n in d.keys():
#     print("yes")
# else:
#     print("No")



# Write a program to get a dictionary from an object's fields

a = {"name","age","Current_year"}
b = {"Ronit",17,2023}
c = a.update(b)
print(c)