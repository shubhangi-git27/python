#Write a program to print the multiplication table of any number using a while loop.
n=int(input("enter no "))
i=1
while(i<=10):
    print(f"{n}*{i} = {n*i}")
    i=i+1