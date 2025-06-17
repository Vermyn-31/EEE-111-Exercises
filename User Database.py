import hashlib

def password_hash(txt):
    if type(txt) is not str:
        raise TypeError('String is required for function password_hash')

    return hashlib.sha256(txt.encode()).hexdigest()

def main():
        # TODO: Write the dic that will store the
        # username-password pair here
    username_password_pair = {}
    while True:
        data = input()


        if(data == 'create'):
                username = input()
                password = input()
    
                if username not in username_password_pair.keys():
                    password = password_hash(password)
                    username_password_pair.update({username:password})
                    print('created')
                else:
                    print('duplicate user')
            
                

        elif(data == 'login'):
            username = input()
            password = input()

            if username in username_password_pair.keys():
                password = password_hash(password)
                password_to_compare = username_password_pair[username]
                if password == password_to_compare:
                    print('success')
                else:
                    print('fail')                                 
            
            else:
                print('user not found')
     
        elif(data == 'delete'):
            username = input()
            password = input()
            
            if username in username_password_pair.keys():
                password = password_hash(password)
                password_to_compare = username_password_pair[username]
                if password == password_to_compare:
                    username_password_pair.pop(username)
                    print('deleted')
                else:
                    print('fail')
            else:
                print('user not found')


            # TODO: Add delete routine here
            #       Check first whether username exists in the
            #       database. Then try to match the hash of password
            #       with the hash of the password saved in the database
            #       corresponding to the username. Delete the pair
            #       if found.

        elif(data == 'exit'):
                # TODO: Add exit routine here
                #       Print the contents of the database.

            for username,password in username_password_pair.items():
                print(f"{username}:{password}")
 
            break
    
        else:
            print('invalid input')
if __name__ == '__main__':
    main()