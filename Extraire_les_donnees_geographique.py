import pandas as pd
import requests
import requests
import csv
import time

# --- 1. Récupération de tous les départements ---
url_departements = "https://geo.api.gouv.fr/departements"
departements = requests.get(url_departements).json()

print(f"{len(departements)} départements trouvés.")

# --- 2. Préparer le fichier CSV ---
fichier_csv = "communes_france.csv"

# Définir les en-têtes du fichier
entetes = ["code_commune", "nom_commune", "code_departement", "nom_departement"]

with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(entetes)

    # --- 3. Boucler sur chaque département ---
    for dep in departements:
        code_dep = dep["code"]
        nom_dep = dep["nom"]
        print(f"→ Récupération des communes du département {nom_dep} ({code_dep})")

        url_communes = f"https://geo.api.gouv.fr/departements/{code_dep}/communes"
        communes = requests.get(url_communes).json()

        # --- 4. Écrire chaque commune dans le CSV ---
        for c in communes:
            writer.writerow([c["code"], c["nom"], code_dep, nom_dep])

        # Petite pause pour ne pas surcharger le serveur
        time.sleep(0.3)

print(f"✅ Fichier '{fichier_csv}' créé avec succès !")
