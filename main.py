testeur = True
prduits = ("Espadris","Chausettes")
users = {
    "oussema":"dardari"
}

def rechercheProduit():
    print("Hello World!\n")

def login(user,mdp):
    print("login succesful\n")

def register(user,mdp):
    users[user] = mdp
    print("register succesfull !!\n")


if __name__ == "__main__":
    print("Enter 1 to Register if you don't have an account\n")
    print("Enter 2 to Login if you have an account\n")
    while(testeur == True):
        var = int(input("enter your choice"))
        if var == 1:
            user = input("Enter your new username")
            mdp = input("Enter your new password")
            register(user,mdp)
            testeur = False
            break
        elif var == 2:
            user = input("Enter your username")
            mdp = input("Enter your password")
            login(user,mdp)
        else:
            print("Input invalid")
for key, value in users.items():
    print(key, ' : ', value)
