class Laptops():
    def Specs(self,m,n):
        self.model=m
        self.Ram=n

    def Fun(self):
        print("hi")

ob1=Laptops()
ob2=Laptops()

ob1.Specs("hp","8GB")
print(ob1.model)
ob2.Specs("Lenovo","8GB")
print(ob2.model)