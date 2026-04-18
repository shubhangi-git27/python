#Create a set of numbers and show union and intersection with another set
set1={2,3,5,9}
set2={1,4,7,9}
set1.add(8.0)
set1.add('8')
print(set1)
result=set1.union(set2)
result2=set1.intersection(set2)
print(result)
print(result2)

# Try to add both integer 9 and float 9.0 to a set and observe what happens
