from src.user import User

class Viewer(User):
    def __init__(self, name):
        super().__init__(name)