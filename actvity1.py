#write a program to create a class  with student and perform the following tasks .
# create a constructor and destructor .
#  then ,create an orject  for that  class and delete the object.

class employee:
    #constructor 
    def __init__(self,name):
        self.name=name

    #destructor 
    def __del__(self):
        print("destructor  called .object deleted")


emp1=employee("mahi singh")
print(emp1.name,"is passionate about nature ")
del emp1 
