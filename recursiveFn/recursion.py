def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

#Write a recursive function that prints numbers from 1 to N.
def counting(n):
    if n ==0:
        return 
    counting(n-1)
    print(n)
print(counting(10))
 
#Write a function that checks if a number is prime.
def prime(num):
    if num <=1:
       return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

num = 9
if prime(num):
    print("prime")
else:
    print("not")

