#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
dict1={}
n=int(input("Enter number of items you want to enter in dictionary "))
for i in range(n):
    key=input("Enter key ")
    val=input("Enter value ")
    dict1[key]=val
print("The dictionary is: ",dict1)
val=input("Enter value whose key you want to find ")
for i,j in dict1.items():
    if(j==val):
        print("Key of value",val,"is",i)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject 
#wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.
dict1={}
n=int(input("Enter number of students whose information you want to store "))
for i in range(n):
    name=input("Enter name ")
    dict2={}
    marks1=int(input("Enter marks in English "))
    marks2=int(input("Enter marks in Hindi "))
    marks3=int(input("Enter marks in Maths "))
    dict2['English']=marks1
    dict2['Hindi']=marks2
    dict2['Maths']=marks3
    dict1[name]=dict2
print("The dictionary is :",dict1)
name=input("Enter name of student whose marks you want to see ")
print(dict1[name])
                   
        
        
                   
