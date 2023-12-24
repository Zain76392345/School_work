#!/usr/bin/env python3
from getpass import getpass
import login


def set_new_passwd(username, password):
    new_password = getpass("New Password: ")
    new_password = login.ROT_13(new_password)

    confirm = getpass("Confirm: ")
    confirm = login.ROT_13(confirm)

    if new_password == confirm:
        original_lines = []
        file_content = open("passwd.txt", "r+")

        for line in file_content:
            if len(line) > 1:
                original_lines.append(line.split(":"))

        file_content = open("passwd.txt", "w")

        for line in original_lines:
            if username == line[0]:
                file_content.write(f"{line[0]}:{line[1]}:{new_password}\n")
            else:
                file_content.write(f"{line[0]}:{line[1]}:{line[2]}")

        file_content.close()
    else:
        print("The passwords don't match!")


if __name__ == "__main__":
    username = input("User:            ")
    password = getpass("Password:        ")
    logged_in = login.login_function(username, password)

    if logged_in:
        set_new_passwd(username, password)
    else:
        print("Access denied.")
