class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}. The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print('The restaurant is open')

    def set_number_served(self, n):
        self.number_serverd = n

    def increment_number_served(self, n):
        self.number_serverd += n
    
restaurant = Restaurant('Mucca Pazza', 'vegan')

print(restaurant.number_serverd)

restaurant.number_serverd = 2
    
print(restaurant.number_serverd)

restaurant.set_number_served(5)

print(restaurant.number_serverd)

restaurant.increment_number_served(10)

print(restaurant.number_serverd)
