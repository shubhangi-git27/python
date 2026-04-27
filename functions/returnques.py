#Write a function square(num) that returns the square of a number.
def square(num=10):
    return (num * num)
print(square(3))

#Create a function full_name(fname, lname) that returns the full name joined with a space.
def full_name(fname,lname):
    return fname+" "+lname
print(full_name("shubhangi","singh"))

#Define a function convert_to_upper(word) that returns the uppercase version of the string.
def upper_case(word):
    return word.upper()
print(upper_case("shubhisingh"))

#2. Create a function login(username, password="1234") that prints the credentials.
def login(username,password="1234"):
    print("username",username)
    print("password",password)
login("subji")   