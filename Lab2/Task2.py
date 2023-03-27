import re
import json

class UniqueElementsContainer:
    def init(self):
        self.container = set()

    def add_elements(self, *args):
        for arg in args:
            if arg not in self.container:
                self.container.add(arg)
                print(f"{arg} added to the container")
            else:
                print(f"{arg} already exists in the container")

    def remove_element(self, key):
        if key in self.container:
            self.container.remove(key)
            print(f"{key} removed from the container")
        else:
            print(f"{key} does not exist in the container")


