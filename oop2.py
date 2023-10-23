class students:
    def __init__(self,name,course,gender,age):
        self.name=name
        self.course=course
        self.gender=gender
        self.age=age

    def show(self):
        print(" name : %s \n course: %s \n gender : %s \n age : %d"
              %(self.name, self.course,self.gender,self.age))

obj1= students("joseph","computer science","male",19)
obj1.show()
obj2=students("sam","computer science","male",29)
obj2.show()
obj3= students("Theuri","computer science","male",19)
obj3.show()