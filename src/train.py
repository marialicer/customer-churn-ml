# %%
# =========================
# IMPORTAR BIBLIOTECAS
# =========================

# pandas > manipulação de dados (ler CSV, limpar, transformar tabelas)
import pandas as pd

# sklearn.tree > algoritmos de árvore de decisão
# sklearn.model_selection > separar treino e teste (train_test_split, validação)
# sklearn.ensemble > modelos ensemble como Random Forest
# sklearn.pipeline > criar pipeline de pré-processamento + modelo
# sklearn.metrics > métricas de avaliação (accuracy, recall, f1-score)

from sklearn import tree
from sklearn import model_selection
from sklearn import ensemble
from sklearn import pipeline
from sklearn import metrics


# feature_engine > biblioteca para engenharia de features
# (encoding, discretização, transformações de variáveis)
# ATENÇÃO! Antes de usar:
# pip install feature-engine no terminal

from feature_engine import discretisation, encoding

# matplotlib > criação de gráficos para análise exploratória

import matplotlib.pyplot as plt


# =========================
# CONFIGURAÇÕES DE VISUALIZAÇÃO
# =========================

# mostrar mais colunas e linhas ao exibir o DataFrame

pd.options.display.max_columns = 500
pd.options.display.max_rows = 500


# =========================
# CARREGAR DADOS (ABT)
# =========================

# leitura do arquivo CSV
# ".." significa voltar uma pasta (porque o script está dentro de /src)

df = pd.read_csv("../data/raw/abt_churn_telco.csv")

# visualizar as 5 primeiras linhas para checar estrutura dos dados
df.head()
# %%
