# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    return pd.read_csv("survey_responses.csv")

def histo():
    print("It works!")
    #s = df['hhdedeyhg']
    #h = s.value_counts()
