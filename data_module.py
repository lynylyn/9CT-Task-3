# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv("survey_responses.csv")

def print_data():
    df = get_data()
    for name, series in df.iterrows():
        print(series.tail(-2).to_string())
        print("\n")

def histo(index):
    df = get_data()
    h = df[df.columns[index]].value_counts().sort_index()
    ax = h.plot.bar()
    ax.set_title(df.columns[index])
    ax.set_xlabel("")
    plt.show()

def scatter():
    df = get_data()
    df.plot.scatter(8, 9)
    plt.show()

def line():
    pass

def filter_data():
    pass