class abc:
    def set_dim(self,a,b):
        self.total=a+b
    def display(self):
        print("addition is ",self.total)
a=abc()
b=abc()
a.set_dim(20,30)
b.set_dim(32,8)
a.display()
b.display()
