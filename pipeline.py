import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup

def extract_csv():
    """Lecture des ventes depuis sales_raw.csv"""
    print("Lecture du fichier sales_raw.csv")


def extract_sqlite():
    """Extraction des données de référence SQLite"""
    print("Lecture de la base bookworld_reference.db")


def scrape_books():
    """Scraping de la première page BooksToScrape"""
    print("Scraping de la première page BooksToScrape")


def get_exchange_rate():
    """Récupération du taux GBP -> EUR"""
    print("Récupération du taux GBP -> EUR")


def transform_data():
    """Nettoyage, enrichissement et agrégation"""
    print("Nettoyage, enrichissement et agrégation")


def load_final_database():
    """Création de la base finale"""
    print("Création de la base finale bookworld_final.db")
    def main():

    extract_csv()
    extract_sqlite()
    scrape_books()
    get_exchange_rate()
    transform_data()
    load_final_database()

    print("Pipeline BookWorld exécuté")


if __name__ == "__main__":
    main()