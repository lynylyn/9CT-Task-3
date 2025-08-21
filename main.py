import pandas as pd
import matplotlib.pyplot as plt

from data_module import (
    read_csv,
    histo
)

def main_menu():
    while True:
        print("\n=== Welcome to the data viewer interface! ===")
        print("\n== Please select from the menu what you'd like to do. ==")
        
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print("Option 1 ")
        elif choice == '2':
            print("Option 1")
        elif choice == '3':
            print("Option 1")
        elif choice == '4':
            print("Option 1")
        elif choice == '5':
            print("Option 1")
        elif choice == '6':
            print("Option 1")
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")