import datetime
import time

name = input("Please enter your name: ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon", name)
if 17 <= presentHour <= 20:
    print("Good Evening", name)
else:
    print("Good Night", name)            
   

print("Namaste! Welcome to the Rule-Based Chat Assistant.")
print("You can ask me simple questions and type 'bye' to exit.")

responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you?": "I'm doing well, thank you! How about you?",
    "i am fine": "That's great to hear! How can I help you?",
    "what is your name?": "I am a rule-based chat assistant",
    "what can you do?": "I can answer simple questions based on predefined rules.",
    "bye": "Goodbye! Have a great day!"
}

#methdod to get response from bot
def getResponseOfBot(userQuestion):
    userQuetion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuetion:
            return responses[eachKey]
    return "i am not able to tell you the answer of this question, please ask something else"    

#take user input
while True:
    userInput= input("please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot:", reply)
    
    if "bye" in userInput.lower():
        break 