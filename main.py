from verification import *
from hash import *
from data_management import *
from generator import *

choice = input("Tapez 1 pour voir les diffrents mot de passes enregistrés.\nTapez 2 pour ajouter un mot de passe.\nTapez 3 pour générer un mot de passe aléatoire.\n: ")
if choice == '2':
    web = input("Entrez un nom de site web: ")
    username = input("Entrez un nom d'utilisateur: ")
    password = input("Veuillez entrer un mot de passe: ")

    isVerified = password_verification(password)

    if isVerified:
        print("Félicitations votre mot de passe est sûr")
        hashed_password = hash_password(password)
        if is_same_password(hashed_password):
            print("Vous avez deja rentré ce mot de passe, veuillez entrer un nouveau mot de passe")
        else: 
            save_password(web, [username,hashed_password])
    else: 
        print("Mot de passe invalide, veuillez entrer un nouveau mot de passe")
elif choice == '1':
    data = open_json()
    for i in data:
        print(f'* {i} - username: {data[i][0]} - password: {data[i][1]}')
elif choice == '3':
    web = input("Entrez un nom de site web: ")
    username = input("Entrez un nom d'utilisateur: ")
    password = generate_random_password()
    if not is_same_password(password):
        print("Le mot de passe généré est")
        hashed_password = hash_password(password)
        save_password(web, [username,password])
else:
    print("Chiffre incorrect")