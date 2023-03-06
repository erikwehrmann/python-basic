def passValidator():
    password = input("Enter password: ")
    confirmPassword = input("Confirm password: ")
    if len(password) > 7:
        if confirmPassword == password:
            print("Password validated!")
        else:
            print("Passwords do not match!")
    else:
        print("Password too short!")


passValidator()
