from user import User

class Admin(User):
    def __init__(self, name):
        super().__init__(name)