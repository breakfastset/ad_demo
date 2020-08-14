
class Student:
    def __init__(self):
        self.name = "Michael Jordan"
        self.number = 23

    def __str__(self):
        return "{} - {}".format(self.name, self.number)

