#advanced_data_types
#mutable vs immutable

#mutable ...can be edited during program lifecycle
# can add / remove elements

#immutable ...cannot be edited

# 1.list [] ....mutable->can be edited
friends = ["nicole","chebzy","grace"]
#or friends = []...for empty
#add ....append.() .extend.()
students = ["roni","grace"]
friends.append(students)
friends.extend(students)
#remove ....pop(),del()


# 2.tuples().....immutable->cannot be edited
stationaries = ("pen","ink","books","stapler","highlighter")
#replace whole tuple
stationaries = ("ruler","eraser","pencil")
for stationary in stationaries:
    print(stationary)
numbers = (1,2,3,4,5,6)
print()

# 3.dictionaries..dict
#uses key and value pair
student = {"name":"agnes","age":17}
print(student["name"])
print(student["age"])



#"name":"agnes" -> name..key  agnes..value