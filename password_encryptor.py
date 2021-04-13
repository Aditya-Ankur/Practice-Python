import bcrypt

# user_pass = b"aditya123"

# pass_salt = bcrypt.gensalt()
# hashed_pass = bcrypt.hashpw(user_pass,pass_salt)
# print(hashed_pass)

check_pass = input("Enter your password : ")
uni_check_pass = bytes(check_pass,encoding="utf-8")
pass_salt = bcrypt.gensalt()
hashed_pass_user = bcrypt.hashpw(uni_check_pass,pass_salt)

# with open("password.txt","a") as fl:
#     fl.write(str(hashed_pass_user))
#     fl.close()

# print(hashed_pass_user)

# Password checker
# if hashed_pass == hashed_pass_user:
#     print("Your password is correct")
# else:
#     print("Invalid password")

