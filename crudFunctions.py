#crudFunctions.py
import pandas as pd

def queryById(file_path, idNumber):
    try:
        # Load the Excel file with openpyxl engine specified
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Convert idNumber column to string to ensure consistent data type
        df['idNumber'] = df['idNumber'].astype(str)
        
        # Attempt to match the provided idNumber (also ensuring it's a string)
        matching_row = df[df['idNumber'] == str(idNumber).strip()]
        
        if not matching_row.empty:
            print("Record Found:")
            # Display the matching row without the index
            print(matching_row.to_string(index=False))
        else:
            print(f"No record found with the idNumber: {idNumber}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
