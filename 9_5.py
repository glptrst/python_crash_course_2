class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User's first name: {self.f_name}\nUser's last name: {self.l_name}")

    def greet_user(self):
        print(f"Welcome {self.f_name} {self.l_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

gianni = User('Gianni', 'Storti')

print(gianni.login_attempts)

gianni.increment_login_attempts()

print(gianni.login_attempts)
        
gianni.increment_login_attempts()
    
print(gianni.login_attempts)

gianni.reset_login_attempts()

print(gianni.login_attempts)
