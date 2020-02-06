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
        self.privileges = Privileges(["can add post" , "can delete post" , "can ban user"])

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(p)


neo = Admin('neo', 'the one')
neo.privileges.show_privileges()

neo.describe_user()
    
