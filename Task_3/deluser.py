#!/usr/bin/env python3


if __name__ == "__main__":
    username = input("Enter username: ")
    file_content = open("passwd.txt", "r+")

    my_list = []
    for line in file_content:
        my_list.append(line.split(":"))

    found = False
    for i in range(len(my_list)):
        if username == my_list[i][0]:
            found = True

            my_list.remove(my_list[i])
            file_content = open("passwd.txt", "w")
            for details in my_list:
                string = ":".join(details)
                file_content.write(string)
            break
        else:
            pass

    if found:
        print("User Deleted.")
    else:
        print("Enter a Valid Username.")

    file_content.close()
