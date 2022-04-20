testeur = True
prduits = ("Espadris", "Chausettes")
users = {
    "oussema": "dardari"
}

Admins = {
    users["oussema"] : "admin"
}



def rechercheProduit():
    print("Hello World!\n")


def login(user, mdp):
    for key, value in users.items():
        if key == user and value == mdp:
            print("login succesful\n")
        elif key == user & value != mdp:
            print("wrong password !")
        else:
            print("user is not registered ")
            exit()




def register(user, mdp):
    users[user] = mdp
    print("are you an admin user ? \n")
    testeur = True
    while (testeur == True):
        var = input("answer by yes or no")
        if var == "yes":
            Admins[user] = "admin"
            print("admin user added !")
            testeur = False
            break
        elif var == "no":
            print("normal user added !")
            testeur = False
            break
        else:
            print("Input invalid !!")

    print("register succesfull !!\n")


def printAllUsers():
    for key, value in users.items():
        print(key, ' : ', value)

def userDashboard(user):
    print("***********__________________________________*****________________________*******__________________"
          "******____________________****")
    print(f"**PARADIS** | Rechercher Un Produit (taper 1) | ****| utulisateur : {user} |*******| aide (taper 2) |******| "
          f"panier (taper 3) |*")
    print("***********----------------------------------*****------------------------*******------------------"
          "******--------------------****")


if __name__ == "__main__":
    print("Enter 1 to Register if you don't have an account\n")
    print("Enter 2 to Login if you have an account\n")
    while (testeur == True):
        var = input("enter your choice \n")
        if var == "1":
            user = input("Enter your new username \n")
            mdp = input("Enter your new password \n")
            register(user, mdp)
            testeur = False
            break
        elif var == "2":
            user = input("Enter your username \n")
            mdp = input("Enter your password \n")
            login(user, mdp)
            break
        else:
            print("Input invalid")
userDashboard(user)

