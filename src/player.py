# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, item=[]):
        self.name = name
        self.current_room = current_room
        self.item = item

    def pickup(self, item):
        for i in self.current_room.item:
            if(i.name == item):
                self.item.append(i)
                self.current_room.item.remove(i)
            else:
                print("No Item With That Name")

    def drop(self, item):
        pass

    def __str__(self):
        return f"{self.name} {self.current_room}"
