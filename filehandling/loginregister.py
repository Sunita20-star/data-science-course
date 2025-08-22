import json
def register(username,password):
  dict_credential={username:password}
  json_credential=json.dumps(dict_credential)
  file=open('credentials.txt','a')
  file.write(json_credential+'-')#we use json here cuz we can convert json into dict 
  file.close()
def login(username,password):
  file=open('credentials.txt','r')
  content=file.read()
  file.close()
  list_credentials=content.split('-')
  print(list_credentials)
  for i in list_credentials:
    if i!="":
      dict_credential=json.loads(i)
      if username in dict_credential and dict_credential[username]==password:
        print('login success')
        break
  else:
      print('login failed') 
      #for-else=executes the code of for block until the break encounters
      #if break doesnot encounters then it executes the code of else block 
choice=input('enter r for register and l for login :').lower()
match choice:
  case 'r':
    username=input('enter your username')
    password=input('enter your password')
    register(username,password)
  case 'l':
    username=input('enter your username')
    password=input('enter your password')
    login(username,password)
  case _:
    print('invalid choices')
print('thank you')