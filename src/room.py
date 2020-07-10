# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = item

    def __str__(self):
        if(self.item == None):
            return f"Room:\n{self.name}\nDescription:\n{self.description}\nNo Item"
        return f"Room:\n{self.name}\nDescription:\n{self.description}\n{self.item}"
