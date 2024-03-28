class OperationBancaire:
    def __init__(self, type_operation, montant, date_operation):
        self.type_operation = type_operation
        self.montant = montant
        self.date_operation = date_operation

class CompteBancaire:
    def __init__(self, numero_compte, type_compte):
        self.numero_compte = numero_compte
        self.type_compte = type_compte
        self.operations = []

    def ajouter_operation(self, operation):
        self.operations.append(operation)
        print(f"Opération {operation.type_operation} de montant {operation.montant} ajoutée au compte {self.numero_compte}.")

class CompteEpargne(CompteBancaire):
    def __init__(self, numero_compte, type_compte, solde, taux_interet, date_ouverture):
        super().__init__(numero_compte, type_compte)
        self.solde = solde
        self.taux_interet = taux_interet
        self.date_ouverture = date_ouverture

class CompteCourant(CompteBancaire):
    def __init__(self, numero_compte, type_compte, solde, decouvert_autorise, frais_gestion):
        super().__init__(numero_compte, type_compte)
        self.solde = solde
        self.decouvert_autorise = decouvert_autorise
        self.frais_gestion = frais_gestion

class Client:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.comptes_bancaires = []
        self.salaire = 0
        self.depenses_mensuelles = 0

    def ajouter_compte(self, compte):
        if compte not in self.comptes_bancaires:
            self.comptes_bancaires.append(compte)
            compte.client = self
            print(f"Le compte {compte.numero_compte} a été ajouté avec succès au client {self.nom} {self.prenom}.")
        else:
            print(f"Le compte {compte.numero_compte} est déjà associé au client {self.nom} {self.prenom}.")

    def retirer_compte(self, compte):
        if compte in self.comptes_bancaires:
            self.comptes_bancaires.remove(compte)
            compte.client = None
            print(f"Le compte {compte.numero_compte} a été retiré avec succès du client {self.nom} {self.prenom}.")
        else:
            print(f"Le compte {compte.numero_compte} n'appartient pas au client {self.nom} {self.prenom}.")

    def calculer_montant_pret(self):
        montant_pret = self.salaire * 3 - self.depenses_mensuelles
        return max(0, montant_pret)

    def calculer_taux_interet(self):
        taux_interet = 0.05  # 5%
        return taux_interet

class InstitutionBancaire:
    def __init__(self, nom):
        self.nom = nom
        self.clients = []

    def ajouter_client(self, client):
        if client.adresse == "Lyon":
            self.clients.append(client)
            client.institution_bancaire = self
            print(f"Le client {client.nom} {client.prenom} a été ajouté avec succès à l'institution {self.nom}.")
        else:
            print(f"Le client {client.nom} {client.prenom} n'a pas une adresse à Lyon. Impossible de l'ajouter.")

    def retirer_clients_non_lyonnais(self):
        clients_a_retirer = [client for client in self.clients if client.adresse != "Lyon"]
        for client in clients_a_retirer:
            self.retirer_client(client)

    def retirer_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            print(f"Le client {client.nom} {client.prenom} a été retiré avec succès de {self.nom}.")
        else:
            print("Le client n'appartient pas à cette institution bancaire.")

class Database:
    def __init__(self):
        self.institutions = []
        self.clients = []

    def ajouter_institution(self, institution):
        self.institutions.append(institution)

    def ajouter_client(self, client):
        self.clients.append(client)

# Exemple d'utilisation :
banque_database = Database()

institution_bnp = InstitutionBancaire("BNP")
banque_database.ajouter_institution(institution_bnp)

client1 = Client("AFO", "Lina", "Lyon")
client1.salaire = 5000
client1.depenses_mensuelles = 2000
client2 = Client("JEAN", "Joseph", "Paris")
client2.salaire = 6000
client2.depenses_mensuelles = 2500

institution_bnp.ajouter_client(client1)
institution_bnp.ajouter_client(client2)

compte1 = CompteEpargne("12345", "Epargne", 1000, 0.02, "01/01/2023")
compte2 = CompteCourant("67890", "Courant", 500, 1000, 10)

client1.ajouter_compte(compte1)
client1.ajouter_compte(compte2)

operation1 = OperationBancaire("Dépôt", 1000, "01/01/2023")

montant_pret_client1 = client1.calculer_montant_pret()
taux_interet_client1 = client1.calculer_taux_interet()

print(f"Montant du prêt pour {client1.nom} {client1.prenom}: {montant_pret_client1}")
print(f"Taux d'intérêt pour {client1.nom} {client1.prenom}: {taux_interet_client1}")