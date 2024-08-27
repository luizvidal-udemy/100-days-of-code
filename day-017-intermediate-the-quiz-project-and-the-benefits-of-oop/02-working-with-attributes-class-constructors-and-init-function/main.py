class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0


user_1 = User("001", "Luiz Vidal")
print(user_1.followers)