#!/usr/bin/env python3
import login


if __name__ == "__main__":

    file_contents = open("passwd.txt", "r+")
    my_list = []
    for line in file_contents:
        my_list.append(line.split(":"))

    usernames_list = []
    if len(my_list) != 0:
        for i in range(len(my_list)):
            usernames_list.append(my_list[i][0])
    else:
        pass

    username = input("User:            ")
    username = login.no_white_space(username)

    real_name = input("Enter real name: ")
    real_name = login.no_white_space(real_name)

    password = input("Password:        ")
    password = login.ROT_13(password)

    if username in usernames_list:
        print("Cannot add. Most likely username already exists.")
    else:
        if username == "" or password == "" or real_name == "":
            print("You must fill in every field!")
        else:
            file_contents.write(f"{username}:{real_name}:{password}\n")
            file_contents.close()
