import sys


def print_menu():
    print("Menu"
          "\n -------------"
          "\n 1. Encode"
          "\n 2. Decode"
          "\n 3. Quit"
          "\n")


def encode(password):
    new_list = []
    for i in password:
        new = int(i) + 3
        new_list.append(new)
    return new_list


def main():
    print_menu()
    menu_option = int(input("Please enter an option: "))
    if menu_option == "1":
        password = input("Please enter a password to encode: ")
        encoded = encode(password)
        print_menu()
    if menu_option == "2":
        print(f"The encoded password is {encoded}, and the original password is {password}.")
        print_menu()
    if menu_option == "3":
        sys.exit()


if __name__ == "__main__":
    main()
