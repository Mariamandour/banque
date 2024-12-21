import os

        # Lecture du fichier 'users.txt' pour récupérer les utilisateurs
def connexion(login, password):
    with open("./bb/users.txt", "r") as f:
        for u in f:
            # On suppose que chaque ligne est de la forme "nom:login:password"
            # On utilise split(":") pour séparer les trois parties
            nom, log, pas = u.strip().split(":")
            
            # Vérification de la correspondance des identifiants
            if login == log and password == pas:
                return nom  # Si les identifiants sont corrects, retourner le nom
        return None  # Si aucun utilisateur ne correspond, retourner None

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def pause():
    input("appuyer sur une touche pour continuer ...")        

                  

        
              
