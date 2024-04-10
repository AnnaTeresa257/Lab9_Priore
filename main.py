def encode(password):
    new_list = []
    for i in password:
        new = int(i) + 3
        new_list.append(new)
    return new_list


