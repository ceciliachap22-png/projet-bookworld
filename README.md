Projet BookWorld
Objectif

BookWorld est une entreprise fictive spécialisée dans la vente de livres en ligne.

L'objectif de ce projet est de construire un pipeline de données permettant de :

collecter des données depuis plusieurs sources ;
nettoyer et enrichir les données ;
produire une agrégation des ventes par pays ;
stocker les résultats dans une base SQLite finale ;
exposer les données via une API REST sécurisée par token.
Technologies utilisées
Python
Pandas
SQLite
Requests
BeautifulSoup
Flask
API Frankfurter
Sources de données
Fichier CSV

Le fichier sales_raw.csv contient les commandes BookWorld :

identifiant de commande ;
date de commande ;
pays ;
canal de vente ;
quantité ;
remise appliquée ;
informations client ;
nom du livre.
Base SQLite

Le fichier bookworld_reference.db contient les tables de référence :

countries

Informations sur les pays :

code pays ;
nom du pays ;
devise ;
taux de TVA ;
région.
channels

Informations sur les canaux de vente :

site web ;
application mobile ;
marketplace.
category_rules

Règles métier associées aux catégories de livres.

Scraping Web

Les informations du catalogue sont récupérées depuis la première page du site :

https://books.toscrape.com/

Les données récupérées sont :

titre du livre ;
prix en livres sterling (GBP).
API Frankfurter

L'API Frankfurter est utilisée pour récupérer le taux de conversion GBP → EUR.

Lien :

https://api.frankfurter.app/

Traitements réalisés

Les traitements effectués dans le pipeline sont :

lecture du fichier CSV ;
extraction des données SQLite ;
scraping du catalogue BooksToScrape ;
récupération du taux de change GBP/EUR ;
suppression des données personnelles conformément au RGPD ;
vérification des doublons ;
vérification des valeurs manquantes ;
conversion des dates ;
enrichissement des ventes avec les données du catalogue ;
calcul du chiffre d'affaires en GBP ;
conversion du chiffre d'affaires en EUR ;
agrégation des ventes par pays.
RGPD

Les colonnes suivantes sont supprimées :

customer_first_name
customer_last_name

Ces informations ne sont pas nécessaires à l'objectif métier du projet et ne sont donc pas conservées dans la base finale, conformément au principe de minimisation des données du RGPD.

Installation des dépendances

Installer les bibliothèques nécessaires :

pip install pandas numpy matplotlib seaborn requests beautifulsoup4 flask
Exécution du pipeline

Ouvrir le notebook :


jupyter notebook

Puis exécuter :


CECILIAROGER_Projet_final_bookworld.ipynb

Le pipeline :

charge les données ;
réalise les traitements ;
produit l'agrégation finale ;
génère la base SQLite finale.
Base finale

Le pipeline génère :

bookworld_final.db

Cette base contient l'agrégation :

sales_by_country

avec les colonnes :

country_code
country_name
total_orders
total_quantity
total_revenue_gbp
total_revenue_eur
API REST

Le projet contient un fichier :


api.py

permettant d'exposer les données agrégées.

Lancer l'API
python api.py

L'API démarre localement sur :

http://127.0.0.1:5000
Authentification

L'accès à l'endpoint :

GET /sales-by-country
 

nécessite un token.

Token utilisé :

bookworld123

Exemple de header :

HTTP
Authorization: bookworld123
Endpoints disponibles
GET /health

Vérifie le fonctionnement de l'API.

Exemple :

JSON
{
"status": "ok",
"message": "API BookWorld opérationnelle"
}
GET /sales-by-country

Retourne les ventes agrégées par pays.

Authentification requise via le header :

HTTP
Authorization: bookworld123


Structure du projet


Projet_BookWorld/
│
├── Projet_bookworld.ipynb
├── queries.sql
├── schema_final.sql
├── api.py
├── README.md
├── sales_raw.csv
├── bookworld_reference.db
└── bookworld_final.db