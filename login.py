while True :
    username = input("enter the username")
    password = input("enter the passsword")
    if username == 'admin' and password == 'password':
        print('✅login successful')
        break
    else : 
        print ('⚠️login failed')
         