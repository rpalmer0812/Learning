class User:
    def __init__(object_name, first_name, last_name):
        object_name.first_name = first_name
        object_name.last_name = last_name
        object_name.login_attempts = 0

    def describe_user(asdf):
        print(f"\n{asdf.first_name} {asdf.last_name} is described here!")

    def greet_user(lkjh):
        print(f"\nHello {lkjh.first_name} {lkjh.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

if __name__ == "__main__":
    user1 = User('James', 'Chou')
    user1.describe_user()
    print(user1.login_attempts)

#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.increment_login_attempts()
#print(user1.login_attempts)

#user1.reset_login_attempts()
#print(user1.login_attempts)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"{self.first_name} {self.privileges[0]}, {self.privileges[1]} and {self.privileges[2]}.")


#admin1 = Admin('Alanna', 'Okuda')

#admin1.show_privileges()
