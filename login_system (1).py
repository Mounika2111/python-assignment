import os
import re


def is_user_exists(username):
    with open("users_list.txt", "r+") as file:
        users = file.readlines()
        user_names = [line.split("||")[0] for line in users]
        if username in user_names:
            return True
        else:
            return False

def get_user_password(username):
    with open("users_list.txt", "r+") as file:
        users = file.readlines()
        for user in users:
            email = user.strip().split("||")[0]
            pwd = user.strip().split("||")[1]
            if username == email:
                return pwd

def set_new_password(username,password):
    with open("users_list.txt", "r") as f:
        users = f.readlines()
    with open("users_list.txt", "w") as f:
        for user in users:
            if user.split("||")[0] != username:
                f.write(user)
            else:
                f.write(username + "||" + password + "\n")
    print("Password reset done")

def create_user(username, password):
    if is_user_exists(username):
        print("User already exists, Please login")
        return 0
    else:
        with open("users_list.txt", "a+") as file:
            file.write(username + "||" + password + "\n")
        print("Registration Successful")


def register():
    while True:
        print("Email/Username : ", end="")
        email = input()
        regex = '[A-Za-z]+[^@]*@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
        if (re.fullmatch(regex, email)):
            while True:
                print("Password : ", end="")
                password = input()
                regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,15}$'
                if (re.fullmatch(regex, password)):
                    create_user(email, password)
                    return
                else:
                    print("Invalid password")
        else:
            print("Invalid Email format")

def login():
    print("Email/Username : ", end="")
    username = input()
    if is_user_exists(username):
        print("Password : ", end="")
        password = input()
        if password == get_user_password(username):
            print("Hi ", username, " Greetings!")
            print("Returning to home screen")
            return
        else:
            print("Incorrect password , please choose from below: ")
            print("1.Retrive old password \t 2.Reset Password \t 3.Exit")
            ch = input("-->")
            if ch == '1':
                print("Old password:",get_user_password(username))
            elif ch == '2':
                while True:
                    print("New Password : ", end="")
                    password = input()
                    regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,15}$'
                    if (re.fullmatch(regex, password)):
                        set_new_password(username, password)
                        break
                    else:
                        print("Invalid password")
            elif ch == '3':
                return
            else:
                print("Incorrect input, please check again")

    else:
        print("User does not exist, Please register :  ")
        register()



if __name__=='__main__':
    if not os.path.exists("users_list.txt"):
        open("users_list.txt", 'a').close()

    while True:
        print("Choose any option : 1.Register \t 2.Login \t 3.Exit")
        ch = input("-->")
        if ch == '1':
            print("Registration Form ")
            register()
        elif ch == '2':
            print("Login Form")
            login()
        elif ch == '3':
            break
        else:
            print("Incorrect input, please check again")
