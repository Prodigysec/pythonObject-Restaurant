
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
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating() for review in self.reviews)
        return total_rating / len(self.reviews)
