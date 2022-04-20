testeur = True
prduits = ("Espadris", "Chausettes")
users = {
    "oussema": "dardari"
}

Admins = {
    "oussema": "admin"
}

userEmail = {
    "oussema": "oussema@oussema.com"
}

userAdress = {
    "oussema": "Ariana"
}


def rechercheProduit():
    print("Hello World!\n")


def login(user, mdp):
    for key, value in users.items():
        if key == user and value == mdp:
            print("login succesful\n")
        elif key == user and value != mdp:
            print("wrong password !")
            exit()
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


def printAllUserAdresses():
    for key, value in userAdress.items():
        print(key, ' : ', value)


def printAllUsersEmails():
    for key, value in userEmail.items():
        print(key, ' : ', value)


def userIsAdmin(user):
    for key, value in users.items():
        if key == user:
            return True
        else:
            return False


def getUserAdress(user):
    for key, value in userAdress.items():
        if key == user:
            return value
        else:
            return "erreur"


def getUserEmail(user):
    for key, value in userEmail.items():
        if key == user:
            print(value)
            return value
        else:
            return "erreur"


def userDashboardNavBar(user):
    print("*************_________________________________******______________________*********__________________"
          "******____________________*")
    print(
        f"**PARADIS***| Rechercher Un Produit (taper 1) |****| utulisateur : {user} |*******| aide (taper 2) |******| "
        f"panier (taper 3) |*")
    print("*************---------------------------------******----------------------*********------------------"
          "******--------------------*")
    if userIsAdmin(user):
        print("user is admin")


def userDashboardProfile(user,email,adress):
    if email == "" and adress =="":
        email = getUserEmail(user)
        adress = getUserAdress(user)
    print("***************************                                 ******************************")
    print("* information personelle  *                                 *  adress                    *")
    print("***************************                                 ******************************")
    print(f"* username : {user}                                         user adress : {adress}  ")
    print(f"* email : {email}                                                                ")
    print("*                         *                                                               ")
    print("***************************                                 ******************************")


if __name__ == "__main__":
    print("Enter 1 to Register if you don't have an account\n")
    print("Enter 2 to Login if you have an account\n")
    while (testeur == True):
        var = input("enter your choice \n")
        if var == "1":
            user = input("Enter your new username :\n")
            mdp = input("Enter your new password :\n")
            email = input("enter your email :\n")
            userEmail[user] = email
            adress = input("enter your adress :\n")
            userAdress[user] = adress
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
userDashboardNavBar(user)
userDashboardProfile(user,email,adress)
print(user)
printAllUsersEmails()
printAllUserAdresses()
