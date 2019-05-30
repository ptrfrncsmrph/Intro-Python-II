class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"\nYou just picked up a {self.name}")
    def on_drop(self):
        print(f"\nYou just dropped a {self.name}")