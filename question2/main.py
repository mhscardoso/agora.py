import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

revendedores = pd.read_csv("data/revendedores.csv", sep=';', encoding='utf8')
fiscal = pd.read_csv("data/fiscalizacao.csv", sep=';', encoding='latin1')

st.write('''
Tabela de Revendedores
''')
st.dataframe(revendedores)

st.write('''
Tabela de Fiscalizações
''')
st.dataframe(fiscal)

branca = revendedores[["CNPJ", "BANDEIRA"]].loc[revendedores["BANDEIRA"] == "BANDEIRA BRANCA"]
n_branca = revendedores[["CNPJ", "BANDEIRA"]].loc[revendedores["BANDEIRA"] != "BANDEIRA BRANCA"]

n_bandeira_branca = branca.count()["CNPJ"]
n_enbandeirada = n_branca.count()["CNPJ"]

st.write(f'''
	Revendedores com Bandeira Branca: {n_bandeira_branca}
''')

st.write(f'''
	Revendedores Embandeirados: {n_enbandeirada}
''')

st.write(f'''
	Porcentagem de Embandeirados: {n_enbandeirada / (n_bandeira_branca + n_enbandeirada)}
''')

first_rows = fiscal[["CNPJ/CPF", "Número do Documento", "Data DF"]].groupby('Número do Documento').apply(lambda x: x.iloc[0]).reset_index(drop=True)

revend_info = revendedores[["CNPJ", "BANDEIRA"]]
merged = pd.merge(first_rows, revend_info, left_on="CNPJ/CPF", right_on="CNPJ", how="left")
merged = merged[["CNPJ/CPF", "Data DF", "BANDEIRA"]].dropna()

st.write(f'''
	Fiscalizaçoes e suas Bandeiras
''')

st.dataframe(merged.head(100))

st.dataframe(merged["BANDEIRA"].value_counts(normalize=True))