#Write a function that takes a string and returns the count of vowels and consonants separately.
def count(userInput):
    #define vowels
    vowels="aeiouAEIOU"

    countVowels=0
    countConsonants=0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
               countVowels=countVowels+1
            else:   
               countConsonants=countConsonants+1

    return countVowels, countConsonants     #stored value

#function call
vowels, consonants= count("shubhangi singh") #stored vslue in a var
print(vowels,consonants) #print the value