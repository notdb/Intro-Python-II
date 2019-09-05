# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name} \n Description: {self.description}"

    def n_to(self):
        return 1

    def s_to(self):
        return 1

    def e_to(self):
        return 1

    def w_to(self):
        return 1   
