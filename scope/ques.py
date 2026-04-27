#1. Write a program with a local variable score inside a function and a global one outside.
score = 10
def game():
    score=20
    print("inside fn",score)
game()
print("outisde fn",score)

#Create a program using global keyword to modify a variable from inside a function.
x =10
def num():
    global x
    x = x+2
num()    
print("global",x)