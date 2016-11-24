#question number 9

print("This program takes a single value, and then takes a list of values and replys true\
 if the value is a member of the list and returns false if it is not.")
for each in range(5):
    def is_member(x,a):
        if x in a:
            print ("true")
        else:
            print ("false")
        

    h = input("Enter a value: ")
    g = input("Enter a list of values: ")

    h = h.lower()
    g = g.lower()

    is_member(h,g)

#complete
