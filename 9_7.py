class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def describe_user(self):
        print(f"User's first name: {self.f_name}\nUser's last name: {self.l_name}")

    def greet_user(self):
        print(f"Welcome {self.f_name} {self.l_name}!")

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ["can add post" , "can delete post" , "can ban user"]

    def show_privileges(self):
        print(f"{self.f_name}'s privileges:")
        for p in self.privileges:
            print(p)

neo = Admin('neo', 'the one')
neo.show_privileges()


neo.describe_user()
    
