class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}. The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print('The restaurant is open')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print('Flavors:')
        for f in self.flavors:
            print(f"- {f}")

ics = IceCreamStand('Da Pino')
ics.flavors = ['chocolate', 'pistacchio']

ics.describe_restaurant()
ics.display_flavors()
