class fruits:
    def __init__(self,type,price,color):
        self.type=type
        self.price=price
        self.color=color

    def show(self):
        print(f"i like eating {self.type} and it costs{self.price}, color being {self.color}")

myobj = fruits("banana"," 20 ksh","yellow")
myobj.show()