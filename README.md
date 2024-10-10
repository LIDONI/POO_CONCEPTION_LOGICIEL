# POO_CONCEPTION_LOGICIEL : Gestion de Comptes Bancaires

## Description du projet
Ce projet est une application de gestion de comptes bancaires, développée en Python en appliquant les principes de la programmation orientée objet (POO). Il permet de simuler des opérations bancaires courantes telles que la création de comptes, la gestion des clients, les opérations sur les comptes (dépôts, retraits), ainsi que la gestion des institutions bancaires et des prêts.

## Fonctionnalités principales

1. Gestion des clients
Ajouter un client avec des informations personnelles (nom, prénom, adresse).
Lier un ou plusieurs comptes bancaires (courants et épargne) à un client.
Calculer le montant de prêt disponible pour un client en fonction de son salaire et de ses dépenses mensuelles.
Filtrer les clients selon leur adresse (par exemple, uniquement ceux situés à Lyon pour certaines institutions bancaires).
2. Gestion des comptes bancaires
Types de comptes disponibles :
Compte courant avec découvert autorisé et frais de gestion.
Compte épargne avec solde initial, taux d’intérêt et date d’ouverture.
Ajouter des opérations bancaires (dépôts, retraits) sur les comptes.
Afficher les opérations effectuées sur un compte.
3. Gestion des institutions bancaires
Ajouter une institution bancaire (ex : BNP, Société Générale).
Associer des clients à une institution en fonction de leur adresse.
Retirer automatiquement les clients non localisés à Lyon d'une institution bancaire.
4. Base de données
La classe Database permet de gérer une collection d'institutions bancaires et de clients.

## Structure du projet

OperationBancaire : Représente une opération (ex : dépôt, retrait) avec un type, un montant et une date.
CompteBancaire : Représente un compte bancaire général, pouvant être un compte courant ou un compte épargne.
CompteEpargne : Un type spécifique de compte bancaire avec un taux d’intérêt.
CompteCourant : Un compte bancaire avec possibilité de découvert et frais de gestion.
Client : Représente un client avec des informations personnelles, des comptes bancaires associés, un salaire et des dépenses mensuelles.
InstitutionBancaire : Représente une banque qui gère plusieurs clients.
Database : Gère une base de données des institutions bancaires et des clients.

## Exemple d'utilisation
Voici un exemple de scénario d’utilisation du projet :

# Création de la base de données
banque_database = Database()

# Ajout d'une institution bancaire
institution_bnp = InstitutionBancaire("BNP")
banque_database.ajouter_institution(institution_bnp)

# Création de clients
client1 = Client("AFO", "Lina", "Lyon")
client1.salaire = 5000
client1.depenses_mensuelles = 2000

client2 = Client("JEAN", "Joseph", "Paris")
client2.salaire = 6000
client2.depenses_mensuelles = 2500

# Ajout des clients à l'institution bancaire
institution_bnp.ajouter_client(client1)  # Client de Lyon accepté
institution_bnp.ajouter_client(client2)  # Client de Paris refusé

# Création de comptes bancaires pour le client1
compte1 = CompteEpargne("12345", "Epargne", 1000, 0.02, "01/01/2023")
compte2 = CompteCourant("67890", "Courant", 500, 1000, 10)

client1.ajouter_compte(compte1)
client1.ajouter_compte(compte2)

# Ajout d'une opération sur un compte
operation1 = OperationBancaire("Dépôt", 1000, "01/01/2023")
compte1.ajouter_operation(operation1)

# Calcul du montant de prêt disponible pour le client1
montant_pret_client1 = client1.calculer_montant_pret()
print(f"Montant du prêt pour {client1.nom} {client1.prenom}: {montant_pret_client1}")
