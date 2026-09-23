# Mobile Money Africa — Détection de fraude

Projet personnel de data science : détection automatique de transactions frauduleuses dans le mobile money en Afrique de l'Ouest, à partir d'un dataset réel de 6,3 millions de transactions.

Réalisé dans le cadre de ma spécialisation IA à Junia ISEN Lille, comme projet fil rouge d'apprentissage durant l'été 2025.

## Contexte

Le mobile money est un moyen de paiement massivement utilisé en Afrique de l'Ouest. Avec sa croissance rapide, la détection de fraude devient un enjeu majeur pour protéger les utilisateurs. Ce projet vise à construire un modèle capable d'identifier automatiquement les transactions suspectes.

## Dataset

- 6 362 620 transactions
- 11 colonnes : type, montant, soldes avant/après, indicateur de fraude...
- Seulement 0,13% de fraudes → dataset fortement déséquilibré

## Démarche

1. **Exploration** — analyse des patterns de fraude
2. **Visualisation** — histogrammes, boxplots, heatmap de corrélation
3. **Nettoyage** — encodage des variables catégorielles, sélection des features
4. **Feature Engineering** — création de `compte_vide` et `difference_solde`
5. **Modélisation** — Random Forest + SMOTE pour gérer le déséquilibre des classes
6. **Dashboard** — application Streamlit pour tester des transactions en temps réel

## Résultats clés

- Les fraudes se concentrent exclusivement sur les types `CASH_OUT` et `TRANSFER`
- Les montants frauduleux sont en moyenne 8x plus élevés que la normale
- 98% des fraudes vident complètement le compte de l'envoyeur
- Modèle final : **recall de 98%**, precision de 67%

| Modèle | Precision | Recall | F1-score |
|---|---|---|---|
| Random Forest seul | 0.97 | 0.79 | 0.87 |
| Random Forest + SMOTE | 0.64 | 0.97 | 0.77 |
| Random Forest + SMOTE + Feature Engineering | 0.67 | 0.98 | 0.80 |

## Stack technique

- **Langage** : Python
- **Data** : Pandas, NumPy
- **Visualisation** : Matplotlib, Seaborn
- **Machine Learning** : Scikit-learn, Imbalanced-learn (SMOTE)
- **Interface** : Streamlit
- **Outils** : Git, Jupyter Notebook

## Structure du projet
mobile-money-africa/
├── data/ # dataset (non versionné, trop volumineux)
├── exploration.ipynb # notebook d'exploration et de modélisation
├── app.py # dashboard Streamlit
├── modele_final.pkl # modèle entraîné sauvegardé
├── notes.md # notes d'apprentissage
└── README.md

## Installation et utilisation

```bash
# cloner le projet
git clone https://github.com/AWESSO-blaise/Mobile-money-africa.git
cd mobile-money-africa

# créer l'environnement virtuel
python -m venv venv
venv\Scripts\activate

# installer les dépendances
pip install pandas matplotlib seaborn scikit-learn imbalanced-learn streamlit joblib

# lancer le dashboard
streamlit run app.py
```

## Dataset source

Dataset PaySim disponible sur [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1).

## Auteur

**Blaise Awesso** — Élève ingénieur Data & IA à Junia ISEN Lille
[LinkedIn](https://www.linkedin.com/in/blaise-awesso/) · [GitHub](https://github.com/AWESSO-blaise)