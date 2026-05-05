x="india"
class ace:
    def give_details(self,a,b,c,d):
        self.tot=a+b+c
        self.name=d
    
    def display(self):
        print("1. NAME= ",self.name)
        print("2. MARK= ",self.tot)
        print("3. COUNTRY: ",x)
class bvrit:
    def give_details(self,a,b,c,d):
        self.tot=a+b+c
        self.name=d
    def display(self):
        print("1. NAME= ",self.name)
        print("2. MARK= ",self.tot)
        print("3. COUNTRY: ",x)
    
a=ace()
a.give_details(20,30,40,"vijay")
a.display()
b=bvrit()
b.give_details(40,50,60,"pavi")
b.display()
