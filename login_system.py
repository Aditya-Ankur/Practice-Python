import linecache
import bcrypt

# salt = bcrypt.gensalt()
# print(salt)
salt = b'$2b$12$o7jhVXcfG3OofEGn8UsCn.'

print("\n\nThis is a login system")
print("Type c to create account \nType l to login\n")

def login_systems():
    
    '''This will log in to the account of the user and will also create account if needed'''

    user_input = input("Type your answer : ")
    
    # Create Account code
    if user_input == "c":
        with open("login_systems.txt","a") as fl:
            
            # User name code
            user_name = input("Enter your name : ")
            fl.write(f"\t\t\t\t\t\t\t{user_name}\n\n")
            fl.write(f"Name : {user_name}\n")

            # User mobile number code
            user_phone = int(input("Enter your phone number : "))
            fl.write(f"Phone : {user_phone}\n")

            # User email code
            user_email = input("Enter your email : ")
            fl.write(f"Email : \n{user_email}\n")

            # password code
            
            def password_make():

                '''This checks the hash codes of the passwords match or not'''

                # first time password and its encryption
                user_pass = input("Enter a new password : ")
                byte_pass = bytes(user_pass,encoding="utf-8")
                global hashed_pass
                hashed_pass = bcrypt.hashpw(byte_pass,salt)

                # confirmation password and its encryption
                conf_user_pass = input("Re enter the password : ")
                conf_byte_pass = bytes(conf_user_pass,encoding="utf-8")
                global conf_hashed_pass
                conf_hashed_pass = bcrypt.hashpw(conf_byte_pass,salt)
            password_make()
            
            # password check
            if hashed_pass == conf_hashed_pass:
                fl.write(f"Password : \n{str(hashed_pass)}")
            else:
                password_make()
        print("Account Created Successfully")
        fl.close()
    
    # Login code
    elif user_input == "l":
        # collection of info and encryption
        log_email = input("Enter your email : ")
        log_pass = input("Enter your password : ")
        byte_log_pass = bytes(log_pass,encoding="utf-8")
        hashed_log_pass = bcrypt.hashpw(byte_log_pass,salt)

        # fetching email and passwords from txt file
        get_email = linecache.getline("login_systems.txt",6)
        get_pass = linecache.getline("login_systems.txt",8)
        get_pass.replace("\n","")
        get_pass.encode("utf-8")
        
        # checking email and passwords
        if str(hashed_log_pass) == str(get_pass) and str(log_email) == str(get_email):
            print("You logged in!")
        else:
            print("Invalid Username or password")
            print(hashed_log_pass)
            print(get_pass)
            print(log_email)
            print(get_email)
    
login_systems()


