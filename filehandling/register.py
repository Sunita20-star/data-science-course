def register(username):
    file = open('register.txt','a')
    file.write(username+'-')
    file.close()
    
def login(username):
    file = open('register.txt','r')
    content = file.read()
    file.close()
    list_content = content.split("-")
    if username in list_content:
        print("Login Successfull")
    else:
        print("Login Failed")
    
while True:
    choice = int(input("Enter 1 for register, 2 for login and 3 for exit: "))
    match choice:
        case 1:
            username = input("Enter your username: ")
            register(username)
        case 2:
            username = input("Enter your username: ")
            login(username)
        case 3:
            break
        case _:
            print("Invalid Input.")
print("Thank you for using our system.")