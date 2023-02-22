names = [ "john","lynn","agnes","lucy","roni"]
#accessing items in a listpyt
print(names)
print (names[0])
print (names[1])
print (names[2])
print (names[0:4])
fruits = ["mangoes","grapes","bananas","apples","kiwi","oranges","guavas"]
print (fruits[0:-1])
print(fruits[3])
print("my favourite fruit is;", fruits [0].upper())
# Adding two lists
vegetables = ["kales","cabbage","onions","spinach"]
stationary = ["pens","ink","pencils","glue","stapler","staples"]
shoppings = vegetables + stationary
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping) 
print("my name is " +  names[2]  +  " and my favourite fruit is " + fruits[0])


