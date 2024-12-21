from views import menu_general, page_connexion

from function import *

while True:
    connected_user = page_connexion()
    if connected_user is not None:
        break

# Cette boucle sera exécutée uniquement si un utilisateur est connecté.
while True:
    choix = menu_general(connected_user)
    
    if choix == "1":
        print("Création d'un compte")
        pause()

    elif choix == "2":
        print("Faire un prêt")
    
    elif choix == "3":
        print("Faire un versement")
    
    elif choix == "4":
        print("Quitter")
        break  # On sort de la boucle si l'utilisateur choisit de quitter
    
    else:
        print("Choix indisponible")

 
     



        


