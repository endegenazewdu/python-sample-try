class Student:
    def _init_(self,fn,ln):
      self.fname=fn
      self.lname=ln
    def sayhello(self):
       print("hello " + self.fname + " " + self.lname)
    def getfullnameineth(self):
       print("hello ","Ato " + self.fname + " " + self.lname)
    def getfullnameinwesten(self):
       print("hello ","Sr " + self.lname + " " + self.fname)
s1=Student()#("endegena","zewdu")
s1.fname="endegena"
s1.lname="zewdu"
s1.sayhello()
s1.getfullnameineth()
s1.getfullnameinwesten()



