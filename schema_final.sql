-- ======================================
-- Projet BookWorld
-- Schéma de la base finale
-- ======================================

DROP TABLE IF EXISTS sales_by_country;

CREATE TABLE sales_by_country (
    country_code TEXT,
    country_name TEXT,
    total_orders INTEGER,
    total_quantity INTEGER,
    total_revenue_gbp REAL,
    total_revenue_eur REAL
);
