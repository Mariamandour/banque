
def creer_clients(id_clients, nom):
    client = [id_clients, nom]
    print(f"Clients {nom} créé avec succès avec l'ID {id_clients}.")
creer_clients()



def demander_pret(id_clients, montant, date_debut):
    
    clients = None
    for c in clients:
        if c[0] == id_clients:
            client = c
            break
         
    if clients is None:
        print(f"Client avec ID {id_clients} non trouvé.")
        return
     
    if clients is None:
        print(f"Client avec ID {id_clients} non trouvé.")
        return
    


    for pret in clients[2]:
        if pret[3] == "en cours":
            print(f"Le client {clients[1]} a déjà un prêt en cours.")
            return
    
   
    taux_interet = 0.12
    montant_total = montant * (1 + taux_interet)  
    clients[2].append([montant, montant_total, date_debut, "en cours", [], 0])  
    print(f"Prêt de {montant}  accordé au clients {client[1]} avec un montant total de {montant_total} .")


def ajouter_versement(id_clients, montant, index_pret):
    
      clients = None
      for c in clients:
        if c[0] == id_clients:
            clients = c
            break
    
      if clients is None:
        print(f"Client avec ID {id_clients} non trouvé.")
        return

    
      pret = clients[2][index_pret]

    
      if pret[3] == "termine":
        print(f"Le prêt du client {clients[1]} est déjà terminé.")
        return
      if len(pret[4]) < 12:
        pret[4].append(montant)  
        pret[5] += montant
        print(f"Versement de {montant}  ajouté au prêt.")
      else:
        print("Le nombre maximum de versements (12) a été atteint.")

      if pret[5] >= pret[1]: 
        pret[3] = "termine"  
        print(f"Le prêt du clients {clients[1]} est maintenant terminé.")
def afficher_clients(id_clients):
    
    clients = None
    for c in clients:
        if c[0] == id_clients:
            clients = c
            break
    
    if clients is None:
        print(f"Clients avec ID {id_clients} non trouvé.")
        return

    
    print(f"Clients: {clients[1]} (ID: {clients[0]})")
    for i, pret in enumerate(clients[2]):
        print(f"  Prêt {i+1}: {pret[0]} , Montant total avec intérêt: {pret[1]} , Statut: {pret[3]}")
        print(f"    Versements: {pret[4]}")
        print(f"    Montant payé: {pret[5]} ")
        print()



