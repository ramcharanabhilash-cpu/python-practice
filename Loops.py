Stored_UserName= "Ramcharan"
Stored_Password="C9931"

for attempt in range(1,5):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == Stored_UserName and password ==Stored_Password:
        print('Login Successful')
        break
    else:
        if attempt==4:
            print("Account locked due to too many failed attempts.")
        else:
            print(f"Incorrect password. Attempts left: {3 - attempt}")

