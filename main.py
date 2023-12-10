from verification import *
from hash import *
from data_management import *

choice = input("Tapez 1 pour voir les diffrents mot de passes enregistrés.\nTapez 2 pour ajouter un mot de passe\n: ")
if choice == '2':
    web = input("Entrez un nom de site web: ")
    username = input("Entrez un nom d'utilisateur: ")
    password = input("Veuillez entrer un mot de passe: ")

    isVerified = password_verification(password)

    if isVerified:
        print("Félicitations votre mot de passe est sûr")
        hashed_password = hash_password(password)
        save_password(web, [username,hashed_password])
    else: 
        print("Mot de passe invalide, veuillez entrer un nouveau mot de passe")
elif choice == '1':
    choice = input("Voulez vous afficher tous les mots de passes enregistrés ou rechercher?")
    data = open_json()
    for i in data:
        print(f'* {i} - username: {data[i][0]} - password: {data[i][1]}')
else:
    print("Chiffre incorrect")