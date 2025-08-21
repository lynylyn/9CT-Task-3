import pandas as pd
import matplotlib.pyplot as plt

from data_module import (
    get_data,
    histo,
    scatter,
    line,
    filter_data
)

def main_menu():
    while True:
        print("\n=== Welcome to the data viewer interface! ===")
        print("== Please select from the menu what you'd like to do. ==")
        print("1. View full dataset")
        print("2. View visualisations")
        print("3. Filter data")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            print("You have selected to view the full dataset.")
            print(get_data())
        elif choice == '2':
            print("\n=== Please select a visualisation. ===")
            print("Option 1: histogram")
            print("Option 2: scatter plot")
            print("Option 3: line graph")
            choicevis = input("Select an option (1-3): ")
            if choicevis == '1':
                histo()
            elif choicevis == '2':
                scatter()
            elif choicevis == '3':
                line()
            else:
                print("That's not a valid selection! Please choose a number between 1 and 3.")

        elif choice == '3':
            print("You have selected to filter the data.")
            filter_data()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("That's not a valid selection! Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()