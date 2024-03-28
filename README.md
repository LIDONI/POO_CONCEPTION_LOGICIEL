Ce projet vise à créer un système de gestion bancaire utilisant des principes de programmation orientée objet (POO). 
Les principales entités incluent les opérations bancaires, les comptes bancaires, les clients, les institutions bancaires, et une base de données pour stocker ces informations.
Le système permet de créer et de gérer des opérations bancaires, différents types de comptes (épargne et courant), des clients avec des attributs tels que le salaire et les dépenses mensuelles, et des institutions bancaires.
Les classes sont structurées avec des relations d'héritage (CompteEpargne et CompteCourant héritent de CompteBancaire), d'association (entre InstitutionBancaire et Client), et d'agrégation (entre CompteBancaire, CompteEpargne, CompteCourant et OperationBancaire).
La méthode super() est utilisée pour initialiser les attributs communs dans les sous-classes avant d'ajouter des attributs spécifiques. 
Le diagramme UML illustre ces relations et montre les attributs privés (-) pour l'encapsulation.
