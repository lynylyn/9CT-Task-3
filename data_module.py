# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv("survey_responses.csv")

def histo(index):
    df = get_data()
    h = df[df.columns[index]].value_counts().sort_index()
    ax = h.plot.bar()
    ax.set_title(df.columns[index])
    plt.show()

def scatter():
    pass

def line():
    pass

def filter_data():
    pass