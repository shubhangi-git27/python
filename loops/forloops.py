#Write a program to print numbers from 1 to 50, but print "Saumya Singh" instead of numbers that are multiples of 5.
for i in range(1,51,1):
    if(i%5==0):
        print("shubhi")
    else:
        print(i)    

#10.Write a program to print the square of each number from 1 to 10 using a for loop.
for i in range(1,11,1):
    print(i*i)

#Write a program that prints the multiplication table of any number entered by the user using a for loop.
# num = int(input("enter a no: "))
# for i in range (1,11,1):
#     print(f"{num} * {i} = {num*i} ")

#Write a program that prints all numbers from 100 to 1 using for and range().
# for i in range(20,0,-1):
#     print(i)

#print her username five times in uppercase letters.
for i in range(1,6,1):
    print("shubhisingh".upper())

#15.Saumya has created a tuple of countries she has already traveled to. Write a Python program to print each country using a for loop. 
countries = ("Malaysia", "Vietnam", "Switzerland", "Italy", "Bhutan")
for i in countries:
    print(i)
