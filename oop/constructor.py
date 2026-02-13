class employee:
    def __init__(self,name,salary):
        print("employee created")
        self.n=name
        self.s=salary
    def display(self):
        print("name",self.n)
        print("salary",self.s)
