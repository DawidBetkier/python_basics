""""Sheldon"""

def sheldon_knock(name):
        if name == "Asia":
            return print("Asia jest super")
        else:
            for i in range(10):
             print(f"{name}!")

if __name__ == '__main__':
    user_name = input("Please provide name: ")
    sheldon_knock(user_name)
