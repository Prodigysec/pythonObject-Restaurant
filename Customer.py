import Review

class  Customer:
    instances = []

    def __init__(self,given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

        Customer.instances.append(self)
        
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.family_name} {self.given_name}"
    
    def all(self):
        return Customer.instances
    
    def restaurants(self):
        return list({review.restaurant() for review in self.reviews})
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)