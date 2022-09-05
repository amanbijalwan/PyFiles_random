
users = ["admin", "alpha", "chad", "dopeMan", "samuraiX"]

print("Hacking the database, welcome user..\n")

userx = input("Enter username to hack mr Hacker..\n")

if userx == "":
    print("User cannot be empty")
elif userx not in users:
    print("User not found, hack failed... aborting!")
elif userx in users:
    if userx == "admin":
        print("Welcome to the supersecret database mr admin.")
    elif userx in users:
        print("hi, another another standard user, welcome")
    
   # print("User is found initiating the hack protocol...\n")
   # print("All other account information found")
    # print(users)

