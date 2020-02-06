class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}. The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print('The restaurant is open')

restaurant1 = Restaurant('Mucca Pazza', 'Vegan')
restaurant2 = Restaurant('Mosquito', 'Asian')
restaurant3 = Restaurant('Bella Napoli', 'Pizza')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

