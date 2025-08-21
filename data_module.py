# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (replace with your own file path)
DATA_FILE = "survey_responses.csv"
df = pd.read_csv(DATA_FILE)

def display_dataset_preview():
    """Show the first 5 rows of the dataset"""
    print("\n--- Dataset Preview ---")
    print(df.head())

def display_visualisation():
    """Example: plot a histogram of a numeric column"""
    print("\nAvailable columns:", list(df.columns))
    col = input("Enter column name to plot: ").strip()

    if col in df.columns:
        df[col].plot(kind="hist", bins=10, edgecolor="black")
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Column not found in dataset.")

def search_data():
    """Filter dataset by a column value"""
    print("\nAvailable columns:", list(df.columns))
    col = input("Enter column to search: ").strip()

    if col in df.columns:
        value = input(f"Enter value to search in '{col}': ").strip()
        results = df[df[col].astype(str).str.contains(value, case=False, na=False)]
        print("\n--- Search Results ---")
        print(results if not results.empty else "No matches found.")
    else:
        print("Column not found.")

def update_data_entry():
    """Update a row in the dataset"""
    try:
        row_index = int(input("Enter the row index to update: "))
        if 0 <= row_index < len(df):
            print("\nCurrent row values:")
            print(df.iloc[row_index])

            col = input("Enter the column to update: ").strip()
            if col in df.columns:
                new_value = input(f"Enter new value for {col}: ").strip()
                df.at[row_index, col] = new_value
                print("Row updated successfully.")
            else:
                print("Column not found.")
        else:
            print("Invalid row index.")
    except ValueError:
        print("Please enter a valid integer index.")

def save_changes():
    """Save the dataset back to file"""
    df.to_csv(DATA_FILE, index=False)
    print(f"Dataset saved to {DATA_FILE}")