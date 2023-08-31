
class Restaurant:
    instances = []
    def __init__(self, name):
        self.name = name
        Restaurant.instances.append(self)
        self.reviews = []

    def name(self):
        return self.name
    
