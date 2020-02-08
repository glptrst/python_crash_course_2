class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def describe_user(self):
        print(f"User's first name: {self.f_name}\nUser's last name: {self.l_name}")

    def greet_user(self):
        print(f"Welcome {self.f_name} {self.l_name}!")
