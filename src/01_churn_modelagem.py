import pandas as pd

from sklearn import tree
from sklearn import model_selection
from sklearn import ensemble
from sklearn import pipeline
from sklearn import metrics


import matplotlib.pyplot as plt

pd.options.display.max_columns = 500
pd.options.display.max_rows = 500

df = pd.read_csv("/data/abt_churn_telco.csv")

df.head()