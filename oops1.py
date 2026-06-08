#  initiate a class
class employee:
    #  dunder method - constructor
    def __init__(self):
        self.id=123
        self.salary=5000
        self.designation="SDE"


    def travel(self, destination):
        print(f"employee is in {destination}")



#  create an obj/instance of the class

sam = employee()

sam.travel("kerala")