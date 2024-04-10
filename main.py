import sys


def print_menu():
    print("Menu"
          "\n-------------"
          "\n1. Encode"
          "\n2. Decode"
          "\n3. Quit"
          "\n")


def decode(encoded):
    decoded = []
    for i in encoded:
        newDecode = i - 3
        if newDecode < 0:
            newDecode *= -1
        decoded.append(newDecode)
    return decoded

def encode(password):
    new_list = []
    for i in password:
        new = int(i) + 3
        new_list.append(new)
    return new_list


def main():
    while True:
        print_menu()
        menu_option = input("Please enter an option: ")
        if menu_option == "3":
            sys.exit()

        if menu_option == "1":
            password = input("Please enter a password to encode: ")
            encoded = encode(password)
            print("You password has been encoded and stored!")
            print()
        if menu_option == "2":
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
            print()


if __name__ == "__main__":
    main()
