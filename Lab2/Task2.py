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

    def find_elements(self, *args):
        found = False
        for arg in args:
            if arg in self.container:
                print(f"{arg} found in the container")
                found = True
        if not found:
            print("No such elements")

    def list_elements(self):
        print("Container elements:")
        for elem in self.container:
            print(elem)

    def grep_elements(self, regex):
        pattern = re.compile(regex)
        found = False
        for elem in self.container:
            if pattern.search(elem):
                print(elem)
                found = True
        if not found:
            print("No such elements")

    def save_container(self, filename):
        with open(filename, "w") as f:
            json.dump(list(self.container), f)
        print(f"Container saved to {filename}")

    def load_container(self, filename):
        with open(filename, "r") as f:
            self.container = set(json.load(f))
        print(f"Container loaded from {filename}")