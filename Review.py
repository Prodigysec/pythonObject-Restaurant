
class Review:
    instances = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.instances.append(self)

    def rating(self):
        return self.rating  
    
    def all(self):
        return Review.reviews
    
    def customer(self):
        return self.customer
    
    def restaurant(self):
        return self.restaurant