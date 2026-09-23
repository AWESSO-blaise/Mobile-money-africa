# on importe streamlit pour créer l'interface web
import streamlit as st
import joblib
import pandas as pd

# on charge le modèle déjà entraîné
modele = joblib.load('modele_final.pkl')

# on affiche un titre
st.title("Détection de fraude Mobile Money")

# on crée un champ pour saisir le montant
montant = st.number_input("Montant de la transaction", min_value=0.0)

# on demande le solde avant et après la transaction
solde_avant = st.number_input("Solde avant la transaction", min_value=0.0)
solde_apres = st.number_input("Solde après la transaction", min_value=0.0)

# on demande le type de transaction
type_transaction = st.selectbox("Type de transaction", 
                                  ["CASH_OUT", "TRANSFER", "PAYMENT", "CASH_IN", "DEBIT"])

# on ajoute un bouton pour lancer la prédiction
if st.button("Analyser la transaction"):
    # on calcule les features dérivées
    compte_vide = 1 if solde_apres == 0 else 0
    difference_solde = solde_avant - solde_apres
    
    # on crée les colonnes du type (0 partout sauf le type choisi)
    type_cash_in = 1 if type_transaction == "CASH_IN" else 0
    type_cash_out = 1 if type_transaction == "CASH_OUT" else 0
    type_debit = 1 if type_transaction == "DEBIT" else 0
    type_payment = 1 if type_transaction == "PAYMENT" else 0
    type_transfer = 1 if type_transaction == "TRANSFER" else 0
    
        # on assemble toutes les features dans le bon ordre pour le modèle
    donnees = pd.DataFrame([[montant, solde_avant, solde_apres, 0, 0,
                              type_cash_in, type_cash_out, type_debit, 
                              type_payment, type_transfer,
                              compte_vide, difference_solde]],
                            columns=['amount', 'oldbalanceOrg', 'newbalanceOrig', 
                                     'oldbalanceDest', 'newbalanceDest',
                                     'type_CASH_IN', 'type_CASH_OUT', 'type_DEBIT',
                                     'type_PAYMENT', 'type_TRANSFER',
                                     'compte_vide', 'difference_solde'])
    
    # on fait la prédiction
    prediction = modele.predict(donnees)[0]
    
    if prediction == 1:
        st.error("⚠️ FRAUDE DÉTECTÉE")
    else:
        st.success("✅ Transaction normale")