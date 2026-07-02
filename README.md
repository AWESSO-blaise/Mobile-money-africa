# Mobile Money Africa — Détection de fraude

Projet d'apprentissage en data science / machine learning visant à détecter des transactions frauduleuses de mobile money à partir du dataset [PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1).

## Dataset

- ~6,36 millions de transactions, 11 colonnes (type, montant, soldes avant/après, indicateur de fraude, ...)
- ~0,13 % des transactions sont frauduleuses
- Les fraudes n'apparaissent que sur les types `CASH_OUT` et `TRANSFER`
- Le fichier CSV n'est pas versionné (voir `.gitignore`) : placer `PS_20174392719_1491204439457_log.csv` dans `data/` avant de lancer le notebook

## Structure du projet

```
.
├── exploration.ipynb   # Analyse exploratoire, visualisations, préparation du modèle
├── notes.md            # Journal d'apprentissage (concepts découverts jour par jour)
├── data/                # Dataset (non versionné)
└── requirements.txt
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Utilisation

```bash
jupyter notebook exploration.ipynb
```

## Avancement

Le détail des concepts appris et des analyses réalisées est tenu à jour dans [notes.md](notes.md).

- **Jour 1** — Exploration du dataset, analyse des fraudes par type, par montant et par comportement de solde
- **Jour 2** — Nettoyage des données, encodage, split train/test, entraînement d'un modèle Random Forest
