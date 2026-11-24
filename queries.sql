-- ======================================
-- Projet BookWorld
-- Requêtes d'extraction SQLite
-- ======================================

-- 1. Pays actifs

SELECT *
FROM countries
WHERE is_active = 1;

-- 2. Informations pays pour enrichissement

SELECT
    country_code,
    country_name,
    currency_code,
    vat_rate,
    region
FROM countries;

-- 3. Canaux de vente actifs

SELECT
    channel_code,
    channel_name,
    acquisition_cost_gbp,
    channel_group
FROM channels
WHERE is_active = 1;

-- 4. Catégories stratégiques

SELECT
    category_name,
    margin_rate,
    default_channel_code
FROM category_rules
WHERE strategic_flag = 1;