# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime


def generer_nom_fichier(prefixe: str, extension: str) -> str:
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefixe}_{horodatage}.{extension}"


def generer_chemin_fichier(nom_fichier: str) -> Path:
    import inspect
    appelant = Path(inspect.stack()[1].filename).stem
    base = Path(__file__).parent.parent.parent
    dossier = base / "doc_history" / appelant
    dossier.mkdir(parents=True, exist_ok=True)
    return dossier / nom_fichier
