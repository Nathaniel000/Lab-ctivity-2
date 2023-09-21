
name = (input("Please enter your name:"))
Id = (input("Please enter your Student ID:"))
Course = (input("Please enter your course:"))
Section = (input("Please enter your section:"))

print("Please enter your grades in the 4th quarter of these subjects:")

Grade1 = eval(input("Introduction to Computing:"))
Grade2 = eval(input("Programming I:"))
Grade3 = eval(input("Mathematics of the Modern World :"))
Grade4 = eval(input("Purposive Communication:"))

Average = (Grade1 + Grade2 + Grade3 + Grade4) / 4
if Average > 90:
    print("You Passed", Average)

else:
    print("Do better next time", Average)

print()
print(name)
print(Id)
print(Course)
print(Section)
print(Average)