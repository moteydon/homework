username=input("enter username:")
password=input("enter password:")
for i in range(0,3):
    print("enter your credentials")
    username1=input("enter your username")
    password1=input("enter oyur password:")
    if username==username1 and password==password1:
        print("you are sucessfully logged.")
        break
    else:
        if(username!=username1 or password!=password1):
            print("invalid credentials")
else:
    print("3 attempt finished")
            
