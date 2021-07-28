import  os

line=open("demo","rt")
print(line.readline()) #reading only one line

#to read the whole file:
for x in line:
    print(x)


fo=open("practice.txt","r")
print("this is the first time: ",fo.read())
print("this is the second time: ",fo.read()) #pointer isn't at position zero
# to change pointer position:;
fo.seek(0,0)
print("this is the third time: ",fo.read())
fo.close()

# os.rename("practice.txt","hello.txt")


# TO REMOVE A FILE:
#os.remove("demo")

#we can check the path of a file:
#os.path.exists("demo")
line.close()
