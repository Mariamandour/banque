
from function import connexion,clear
from consts import*

def header(title, subtitle,motif="-"):   
   clear()
   print("*"*screen)
   print(title.center(screen,motif))
   print("{:*>60}".format(subtitle)) 

def page_connexion():
      header(APP_NAME,'connexion',"*")
      login=input("login    :")
      password=input("Mot de passse :")
      return connexion(login,password)
      
      
def menu_general(user):   
      header(APP_NAME,user, '+')
      print( "1 creer un compte")
      print("2 faire un pret")
      print(" 3 faire versement")
      print("4 quitter")
      choix= input("entre votre choix")
      return choix

