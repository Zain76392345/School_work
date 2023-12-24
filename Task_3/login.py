#!/usr/bin/env python3

from getpass import getpass
# keys in a dictionary have to be unique


def no_white_space(string):
    string = string.strip(" ")
    string = " ".join(string.split())
    return string


def ROT_13(password):
    password = password.strip(" ")
    encrypted_password = []

    lower_list = []
    upper_list = []

    for i in range(0, 26):
        upper_list.append(chr(65 + i))
        lower_list.append(chr(97 + i))

    encrypted_password = []
    for letter in password:
        if letter in lower_list:
            if ord(letter) + 13 > ord("z"):
                encrypted_password.append(chr((ord(letter) + 13) - 26))
            else:
                encrypted_password.append(chr(ord(letter) + 13))
        elif letter in upper_list:
            if ord(letter) + 13 > ord("Z"):
                encrypted_password.append(chr((ord(letter) + 13) - 26))
            else:
                encrypted_password.append(chr(ord(letter) + 13))
        else:
            encrypted_password.append(letter)

    hashed = "".join(encrypted_password)

    return hashed


def login_function(username, password):
    file_contents = open("passwd.txt", "r")
    my_list = []
    for line in file_contents:
        my_list.append(line.split(":"))

    if len(my_list) != 0:
        for i in range(len(my_list)):
            credentials_dict.update({my_list[i][0]: my_list[i][2]})

    username = no_white_space(username)

    password = ROT_13(password)

    if username in credentials_dict:
        hashed_password = credentials_dict.get(username).strip("\n")
        if password == hashed_password:
            return True
        else:
            return False
    else:
        return False


credentials_dict = {

}

if __name__ == "__main__":
    username = input("User:            ")
    password = getpass("Password:        ")
    logged_in = login_function(username, password)

    if logged_in:
        print("Access granted.")
    else:
        print("Access denied.")
