# 📁 file_manager

Module Python utilitaire pour la gestion automatique des fichiers de sortie.
Conçu pour être utilisé dans tous les scripts du projet **Quincaillerie NC**.

---

## 📦 Structure

```
modules/
└── file_manager/
    ├── __init__.py
    └── file_manager.py
```

---

## ⚙️ Fonctionnement

Le module détecte automatiquement le nom du script appelant et crée un dossier dédié dans `doc_history/`.

```
dev/
└── doc_history/
    └── nom_du_script_appelant/
        └── fichier_genere.xlsx
```

Aucun nom de dossier à passer en dur. Le dossier est créé automatiquement selon le script qui appelle le module.

---

## 🚀 Installation

### 1. Cloner le repo

```bash
git clone https://github.com/quincaillerie-nc/file_manager.git
cd file_manager
```

### 2. Placer le module dans le projet

```
dev/
└── modules/
    └── file_manager/
        ├── __init__.py
        └── file_manager.py
```

### 3. Aucune dépendance externe

Le module utilise uniquement des librairies natives Python 3 :
- `pathlib`
- `datetime`
- `inspect`

---

## 🧩 Utilisation

### Import

```python
from modules.file_manager import generer_chemin_fichier, generer_nom_fichier
```

### Générer un nom de fichier horodaté

```python
from modules.file_manager import generer_nom_fichier

nom = generer_nom_fichier("rapport", "xlsx")
print(nom)
# → rapport_20250518_143022.xlsx
```

### Générer un chemin de fichier automatique

```python
from modules.file_manager import generer_chemin_fichier, generer_nom_fichier

nom = generer_nom_fichier("export", "csv")
chemin = generer_chemin_fichier(nom)
print(chemin)
# → /home/user/dev/doc_history/mon_script/export_20250518_143022.csv
```

Le dossier `doc_history/mon_script/` est créé automatiquement s'il n'existe pas.

---

## 📋 Référence des fonctions

### `generer_nom_fichier(prefixe: str, extension: str) -> str`

| Paramètre   | Type  | Description                        |
|-------------|-------|------------------------------------|
| `prefixe`   | `str` | Nom de base du fichier             |
| `extension` | `str` | Extension sans point (`xlsx`, `pdf`, `csv`) |

**Retourne** : `str` — nom du fichier avec horodatage

---

### `generer_chemin_fichier(nom_fichier: str) -> Path`

| Paramètre    | Type  | Description              |
|--------------|-------|--------------------------|
| `nom_fichier`| `str` | Nom du fichier à créer   |

**Retourne** : `Path` — chemin complet vers le fichier

Le dossier de destination est automatiquement résolu selon le script appelant.

---

## ✅ Exemple complet

```python
from modules.file_manager import generer_chemin_fichier, generer_nom_fichier

nom = generer_nom_fichier("commande", "xlsx")
chemin = generer_chemin_fichier(nom)

# Utilisation avec openpyxl
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws["A1"] = "Test"
wb.save(chemin)

print(f"Fichier sauvegardé : {chemin}")
```

---

## 🖥️ Compatibilité

| OS      | Statut |
|---------|--------|
| Windows | ✅     |
| Ubuntu  | ✅     |
| macOS   | ✅     |

---

## 👤 Auteur

**Quincaillerie NC**
Scripts & Automatisation — Usage interne
