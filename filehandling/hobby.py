def add_hobby(hobby):
    file = open('hobby.txt', 'a')
    file.write(hobby.strip() + '-')  
    file.close()
def check_hobby(hobby):
    file = open('hobby.txt', 'r')
    content = file.read()
    file.close()
    list_content = content.lower().strip('-').split('-')
    if hobby.lower().strip() in list_content:
        print('hobby is found')
    else:
      print('hobby is not found')
while True:
    print("1. Add a hobby\n 2.search for hobby\n 3.exit")
    choice = int(input('choose 1 to add hobby 2 to check hobbby and 3 for exit'))
    match choice:
        case 1:
            hobby = input('enter a hobby')
            add_hobby(hobby)
        case 2:
            hobby = input('enter a hobby to search')
            check_hobby(hobby)
        case 3:
            break
        case _:
            print('invalid input')
