# Projet Mobile Money - Notes d'apprentissage

## Jour 1

### Ce que j'ai appris
- Python seul ne sait pas manipuler des tableaux — il faut importer pandas
- Python ne sait pas utiliser les graphiques donc on utilise la librairie matplotlib 
- `import pandas as pd` — pd est juste un surnom raccourci
- `pd.read_csv('chemin/fichier.csv')` — charge un fichier CSV en mémoire
- `df` = DataFrame = tableau de données (comme un Excel en mémoire)
- `df.shape` — affiche (lignes, colonnes)

### Mon dataset
- 6 362 620 lignes = 6 millions de transactions mobile money
- 11 colonnes = 11 infos par transaction

### Questions ouvertes
- C'est quoi la différence entre une liste Python et un DataFrame ?

### Mon tableau de données
- On recupere les 11 infos par transactions via print(df.columns.tolist())
- On recupere par defaut les 5 premieres lignes ( les 5 premieres transactions des 6 millions) avec print(df.head())

### Analyse des données
- `df[df['isFraud'] == 1].shape[0]` — compter les lignes qui respectent une condition
- `==` sert à comparer, `=` sert à assigner une variable
- 8213 transactions frauduleuses sur 6 362 620 soit 0.13%
- Une fraude typique : un compte qui se vide intégralement en une seule transaction

### Types de transactions
- 5 types : CASH_OUT, PAYMENT, CASH_IN, TRANSFER, DEBIT
- CASH_OUT est le plus fréquent (2.2M transactions)
- Les fraudes n'apparaissent que dans 2 types : CASH_OUT et TRANSFER
- Conclusion : le type de transaction est un indicateur fort de fraude

### Analyse temporelle des fraudes
- Les fraudes sont réparties uniformément sur les 720 heures (30 jours)
- Pas de pic nocturne comme on aurait pu l'intuiter
- Conclusion : l'heure seule n'est pas un bon indicateur de fraude
- Leçon : toujours vérifier ses intuitions avec les données

### Analyse des montants
- Montant moyen transaction normale : ~178 000
- Montant moyen transaction frauduleuse : ~1 468 000
- Les fraudes ciblent des montants 8x plus élevés que la moyenne
- Conclusion : le montant est un indicateur fort de fraude
- Leçon : nos intuitions peuvent être fausses, les données ont toujours raison

### Comportement du solde dans les fraudes
- 8053 fraudes sur 8213 ont un solde final à 0 (98%)
- Presque toutes les fraudes vident complètement le compte
- newbalanceOrig == 0 est un indicateur presque parfait de fraude
- Feature engineering futur : créer une colonne 'compte_vide' (0 ou 1) 

### Visualisation des montants
- Boxplot : la boîte des fraudes est plus haute et plus grande que les normales
- Les montants frauduleux sont plus élevés ET plus dispersés
- Les outliers (cercles) = transactions avec des montants extrêmes
- plt.ylim(min, max) permet de zoomer sur une partie du graphique
- Nouveau concept : distribution large = valeurs très dispersées

