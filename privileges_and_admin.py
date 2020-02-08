from user import User

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
