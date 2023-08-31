
class  Customer:
    def __init__(self,given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.family_name} {self.given_name}"