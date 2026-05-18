# -*- coding: utf-8 -*-
"""
================================================================================
MODULE : file-manager / file_manager.py
================================================================================
Génère automatiquement des noms et chemins de fichiers horodatés.
Le dossier de sortie est créé dans dev/doc_history/<nom_script_appelant>/
================================================================================
"""

from pathlib import Path
from datetime import datetime


# =====================================================
# FONCTIONS PUBLIQUES
# =====================================================
def generer_nom_fichier(prefixe: str, extension: str) -> str:
    """
    Génère un nom de fichier avec horodatage.

    Exemple : generer_nom_fichier("rapport", "xlsx")
              → "rapport_20260518_143022.xlsx"
    """
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefixe}_{horodatage}.{extension}"


def generer_chemin_fichier(nom_fichier: str) -> Path:
    """
    Génère le chemin complet du fichier dans doc_history/<script_appelant>/.
    Crée le dossier automatiquement s'il n'existe pas.

    Exemple : generer_chemin_fichier("rapport_20260518.xlsx")
              → Path(".../dev/doc_history/com_isee/rapport_20260518.xlsx")
    """
    import inspect
    # Remonte la pile pour trouver le script qui appelle ce module
    appelant = Path(inspect.stack()[1].filename).stem

    # Racine = 3 niveaux au-dessus de ce fichier → dev/
    base    = Path(__file__).resolve().parent.parent.parent
    dossier = base / "doc_history" / appelant
    dossier.mkdir(parents=True, exist_ok=True)

    return dossier / nom_fichier
