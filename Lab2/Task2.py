import re
import json


class UniqueElementsContainer:
    def __init__(self):
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
        if len(self.container) > 0:
            print("Container elements:")
            for elem in self.container:
                print(elem)
        else:
            print("Empty container")

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
        try:
            with open(filename, "w") as f:
                json.dump(list(self.container), f)
            print(f"Container saved to {filename}")
        except:
            print("Error in saving")

    def load_container(self, filename):
        a = self.container.copy()
        try:
            with open(filename, "r") as f:
                b = set(json.load(f))
                self.container = a.union(b)
            print(f"Container loaded from {filename}")
        except:
            print("Error in loading")

    """def switch_container(self):"""


class CLI:
    def __init__(self):
        self.containers = {}

    def run(self):
        print("Welcome to Perfect Unique Elements Container CLI!")
        while True:
            username = input("Please enter your username: ")
            if username not in self.containers:
                self.containers[username] = UniqueElementsContainer()
                print(f"New container created for user {username}")
                if input("Do you want to load any existing container? (y/n) ").strip().lower() == "y":
                    filenames = input("Enter file name  ")
                    self.containers[username].load_container(filenames)
            else:
                print(f"Container loaded for user {username}")

            while True:
                user_input = input(f"{username} >>> ")
                tokens = user_input.strip().split(" ")
                if tokens[0] == "add":
                    self.containers[username].add_elements(*tokens[1:])
                elif tokens[0] == "remove":
                    self.containers[username].remove_element(tokens[1])
                elif tokens[0] == "find":
                    self.containers[username].find_elements(*tokens[1:])
                elif tokens[0] == "list":
                    self.containers[username].list_elements()
                elif tokens[0] == "grep":
                    self.containers[username].grep_elements(tokens[1])
                elif tokens[0] == "save":
                    if len(tokens) > 1:
                        self.containers[username].save_container(tokens[1])
                    else:
                        print("Add filename to the command syntax")
                elif tokens[0] == "load":
                    if len(tokens) > 1:
                        self.containers[username].load_container(tokens[1])
                    else:
                        print("Add filename to the command syntax")
                elif tokens[0] == "switch":
                    if input("Do you want to save changes in this container? (y/n) ").strip().lower() == "y":
                        filename = input("Enter file name  ")
                        self.containers[username].save_container(filename)
                    self.containers.clear()
                    print("Switching user...")
                    break
                else:
                    print("Unknown command")
            if input("Would you like to exit? (y/n) ").strip().lower() == "y":
                break


cli = CLI()
cli.run()
