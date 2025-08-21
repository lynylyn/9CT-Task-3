import pandas as pd
import matplotlib.pyplot as plt

from data_module import (
    get_data,
    print_data,
    histo,
    scatter,
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
            print_data()
        elif choice == '2':
            print("\n=== Please select a visualisation. ===")
            print("Option 1: histogram")
            print("Option 2: scatter plot")
            choicevis = input("Select an option (1-2): ")
            if choicevis == '1':
                usercolumn = input("\nWhich column would you like to display a histogram of? Choose between: \n - '1' (how much does the music you're listening to depend on what you're doing) \n - '2' (how much does listening to music help you focus) \n - '3' (how confident are you in your academic performance)\nPlease select a number between 1 and 3: ")
                if usercolumn == '1':
                    histo(6)
                elif usercolumn == '2':
                    histo(9)
                elif usercolumn == '3':
                    histo(10)
                else:
                    print("That's not a valid selection! Please choose a number between 1 and 3.")
            elif choicevis == '2':
                scatter()
            else:
                print("That's not a valid selection! Please choose a number between 1 and 2.")

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