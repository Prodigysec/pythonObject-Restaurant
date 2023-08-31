
class Restaurant:
    instances = []
    def __init__(self, name):
        self.name = name
        Restaurant.instances.append(self)
        self.reviews = []

    def name(self):
        return self.name
    
    def reviews(self):
        return self.reviews
    
    def customers(self):
        return list({review.customer() for review in self.reviews})
