import shutil
#wap to read a txt from a given mydata.txt nd find whether it contains the word live
# file=open("mydata.txt","r")
# data = file.read()
# data= data.lower()
# if "live" in data:
#     print("yes")
# else:
#     print("no")    
# file.close()

# with open("mydata2.txt","w") as f:
#     data = f.write("hiiiiiiiii")
#     print("file",data)

# with open("mydata.txt","r") as f:
#     line1 = f.readlines()

#     print("number of lines",len(line1))
    
#name class into a file
with open("mydata2.txt","a") as f:
   # name= input("enter your name")
   # f.write("shubhi\n")
   # class1=input("enter your class")
   # f.write("12th\n")
    shutil.copy("mydata.txt","mydata2.txt")
    f.write("completed\n")
    print(f)