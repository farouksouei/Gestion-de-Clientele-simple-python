users = [{
    'id': 1,
    'name': 'oussema',
    'password': '123',
    'email': 'oussema@gmail.com',
    'phone': '12345',
    'address': '123 ariana',
    'role': 'admin'
}]

products = [{
    'id': 1,
    'name': 'product1',
    'price': 100,
}, {
    'id': 2,
    'name': 'product2',
    'price': 200,
}, {
    'id': 3,
    'name': 'product3',
    'price': 300,
}]

prductsPurchase = [{
    'id': 1,
    'product': products[0],
    'user': 'oussema',
    'quantity': 3}, {
    'id': 2,
    'product': products[1],
    'quantity': 2,
    'user': 'oussema'}, ]

mailboxx = [{
    'id': 1,
    'from': 'farouk',
    'to': 'oussema',
    'subject': 'TESTER LE SUJET DU MAIL',
    'message': 'TESTER LE MESSAGE DU MAIL',
}, {
    'id': 2,
    'from': 'oussema',
    'to': 'farouk',
    'subject': 'TESTER LE SUJET DU MAIL',
    'message': 'TESTER LE MESSAGE DU MAIL',

}]
AvisEnAttente = [{
    'id': 1,
    'from': 'oussema',
    'message': 'test'}]


def Aide():
    print("")


def navBar(user):
    print("****************************************************************************************")
    print(
        f"** Paradis **|Chercher Un Produit (Taper 1)|** Bonjour : {user} |** Aide (Taper 2) |**|Panier (Taper 3)|")
    print("****************************************************************************************")


def find_product(id):
    for product in products:
        if product['id'] == id:
            print("produit found")
            break
        else:
            print("product not found")
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        find_product(id)


def find_product_name(name):
    i = True
    for product in products:
        if product['name'] == name:
            i = False
            print("produit found")
            break
    if i == True:
        print("product not found")
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        find_product(id)


def Panier(user):
    print("****************************************************************************************")
    print(f"**Panier de {user}**")
    print("****************************************************************************************")
    for product in prductsPurchase:
        if product['user'] == user:
            print(f"{product['product']['name']}")
            print(f"{product['product']['price']}")
            print(f"{product['quantity']}")
            print(
                "****************************************************************************************")
    print("****************************************************************************************")
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        Panier(user)


def Account(user):
    print("****************************************************************************************")
    print(f"***Compte de {user}***")
    print("****************************************************************************************")
    for userz in users:
        if userz['name'] == user:
            print(f"{userz['name']}")
            print(f"{userz['email']}")
            print(f"{userz['phone']}")
            print(f"{userz['address']}")
            print(f"{userz['role']}")
            print(
                "****************************************************************************************")
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        Account(user)


def MailBox(user):
    id = 1
    print("****************************************************************************************")
    print(f"***Boite De reception de {user}***")
    print("****************************************************************************************")
    for mail in mailboxx:
        if mail['to'] == user:
            print(f"email numero : {id}")
            print(f"{mail['from']}")
            print(f"{mail['subject']}")
            print(f"{mail['message']}")
            id += 1
            print(
                "****************************************************************************************")
    print("press 0 to return to dashbord")
    print("press 1 to send a mail")
    print("press 2 to see sent mail")
    u = input("")
    if u == '0':
        main()
    elif u == '1':
        send_mail(user)
    elif u == '2':
        sentMail(user)
    else:
        MailBox(user)


def send_mail(user):
    print("****************************************************************************************")
    print(f"***Envoyer un mail de {user}***")
    print("****************************************************************************************")
    print("***Entrer le nom du personne que vous voulez envoyer un mail***")
    name = input()
    print("***Entrer leur email***")
    email = input()
    print("***Entrer votre sujet***")
    subject = input()
    print("***Entrer votre message***")
    message = input()
    mailboxx.append({
        'id': len(mailboxx) + 1,
        'from': user,
        'email': email,
        'to': name,
        'subject': subject,
        'message': message
    })
    print("press 0 to return to dashbord")
    print("press 1 to send a mail")
    print("press 2 to see sent mail")
    u = input("")
    if u == '0':
        main()
    elif u == '1':
        MailBox(user)
    elif u == '2':
        sentMail(user)
    else:
        send_mail(user)


def sentMail(user):
    print("****************************************************************************************")
    print(f"***Boite De reception de {user}***")
    print("****************************************************************************************")
    for mail in mailboxx:
        if mail['from'] == user:
            print(f"email numero : {mail['id']}")
            print(f"{mail['from']}")
            print(f"{mail['subject']}")
            print(f"{mail['message']}")
            print(
                "****************************************************************************************")
    print("press 0 to return to dashbord")
    print("press 1 to send a mail")
    print("press 2 to see the mailbox")
    u = input("")
    if u == '0':
        main()
    elif u == '1':
        send_mail(user)
    elif u == '2':
        MailBox(user)
    else:
        sentMail(user)


def show_avis():
    print("****************************************************************************************")
    print("***Avis en attente***")
    print("****************************************************************************************")
    for avis in AvisEnAttente:
        print(f"{avis['from']}")
        print(f"{avis['message']}")
        print(
            "****************************************************************************************")
    print("press 0 to return to dashbord")
    print("press 1 to send avis")
    u = input("")
    if u == '0':
        main()
    else:
        show_avis()


def send_avis(user):
    print("****************************************************************************************")
    print(f"***Envoyer un avis a {user}***")
    print("****************************************************************************************")
    print("***Entrer votre avis***")
    message = input()
    AvisEnAttente.append({
        'id': len(AvisEnAttente) + 1,
        'from': user,
        'message': message
    })
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        send_avis(user)


def facture(user):
    print("****************************************************************************************")
    print(f"***Facture de {user}***")
    print("****************************************************************************************")
    montant_total = 0
    for product in prductsPurchase:
        if product['user'] == user:
            print(f"Nom du produit : {product['product']['name']}")
            print(f"prix du produit = {product['product']['price']}")
            print(f"Quantité du = {product['quantity']}")
            montant = product['product']['price'] * product['quantity']

            montant_total += montant
            print(
                f"montant = {montant} DT")
            print(
                "****************************************************************************************")
    print("****************************************************************************************")
    print(f"montant total = {montant_total} DT")
    print("facture généree avec succes")
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        facture(user)


def modify_password(user):
    print("****************************************************************************************")
    print(f"***Modifier votre mot de passe a {user}***")
    print("****************************************************************************************")
    print("***Entrer votre nouveau mot de passe***")
    password = input()
    i = 0
    for userz in users:
        if userz['name'] == user:
            users[i]['password'] = password
        else:
            i += 1
    print("press 0 to return to dashbord")
    u = input("")
    if u == '0':
        main()
    else:
        modify_password(user)


def userDashboard():
    print("****************************************************************************************")
    print("***Pour voir Votre Compte taper 4***")
    print("****************************************************************************************")
    print("***Pour voir Votre Boite De reception taper 5***")
    print("****************************************************************************************")
    print("***Pour voir Les Avis en attente taper 6***")
    print("****************************************************************************************")
    print("***Pour voir Votre Facture taper 7***")
    print("****************************************************************************************")
    print("***Pour Modifer votre mot de passe taper 8***")
    print("****************************************************************************************")
    print("***Pour Quitter taper 0***")
    print("****************************************************************************************")


def main():
    print(prductsPurchase[0]['product']['id'])
    while True:
        print("****************************************************************************************")
        print("***Pour vous inscrire taper 1***")
        print("****************************************************************************************")
        print("***Pour vous connecter taper 2***")
        print("****************************************************************************************")
        print("***Pour quitter taper 0***")
        print("****************************************************************************************")
        choice = input()
        if choice == "1":
            print(
                "****************************************************************************************")
            print("***Entrer votre nom***")
            name = input()
            print("***Entrer votre email***")
            email = input()
            print("***Entrer votre telephone***")
            phone = input()
            print("***Entrer votre adresse***")
            address = input()
            print("***Entrer votre mot de passe***")
            password = input()
            users.append({
                'id': len(users) + 1,
                'name': name,
                'email': email,
                'phone': phone,
                'address': address,
                'password': password
            })
            print(
                "****************************************************************************************")
            print("inscription avec succes")
            print(
                "****************************************************************************************")
        elif choice == "2":
            print(
                "****************************************************************************************")
            print("***Entrer votre nom***")
            name = input()
            print("***Entrer votre mot de passe***")
            password = input()
            for user in users:
                if user['name'] == name and user['password'] == password:
                    print(
                        "****************************************************************************************")
                    print("connexion avec succes")
                    print(
                        "****************************************************************************************")
                    navBar(name)
                    userDashboard()
                    while True:
                        choice = input()
                        if choice == "1":
                            produit = input(
                                "entrez que vous voulez chercher \n")
                            find_product_name(produit)
                        if choice == "2":
                            Aide()
                        if choice == "3":
                            Panier(name)
                        if choice == "4":
                            Account(name)
                        elif choice == "5":
                            MailBox(name)
                        elif choice == "6":
                            show_avis()
                        elif choice == "10":
                            send_mail(name)
                        elif choice == "7":
                            facture(name)
                        elif choice == "8":
                            modify_password(name)
                        elif choice == "0":
                            print(
                                "****************************************************************************************")
                            print("Au revoir")
                            print(
                                "****************************************************************************************")


main()
