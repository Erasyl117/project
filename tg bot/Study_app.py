class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def raise_age(self):
        self.age += 1
        
    def introduce(self):
        print("Привет мое имя", self.name, self.age)
person1=person("Beka",18)
person2=person("era",17)
person1.raise_age()
person2.raise_age()
person1.introduce() 
person2.introduce()