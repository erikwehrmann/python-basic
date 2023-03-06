def passCheck():
    password = 'erikiscool123'
    inputPass = input("Enter password: ")
    if inputPass == password:
        print("Logging in!")
    else:
        print("Wrong Password!")


passCheck()
