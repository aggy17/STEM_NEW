age = 16
gender = "male"

if (age < 18):
    print("you are still young")

else:
    print("get an id")

#compound / multiple conditions
if ((age > 30) & (gender == "male")):
    print("you qualify for a loan")
else:
    print("no loan for you")

fav_color = "grey" 
age = 20
if (fav_color == "grey") | (age <= 20):
    print("happy birthday to you") 
else:
    print("no birthday present for you yet")  
