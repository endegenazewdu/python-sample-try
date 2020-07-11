#this is list you can change it
student=["endegena","nathan","alem"]
student[0]="kid"#you can change'cust'
print(student[0])

#this is tuple you can't change
student=("endegena","nathan","alem")
print(student[0])

#this is set un orderd and didn't allow dublicat
student={"endegena","nathan","alem"}
print(student)

 #this is dictenary
student={"first name":"endegena",
         "father name":"nathan",
         "grand father name":"alem",
         "age":34}
student.pop("age") #you can crop   
student["gender"]="male"   #you can add
#print(student["father name"]) you can chouse which one to print
print(student)