import os
import pandas as pd
from functions.functions import process_file
from functions.create_email import create_email_list

# generate file path to the excel file
def main():
    input_excel_path = 'data/Test Files.xlsx'
    output_csv_path = 'data/Student_emails.csv'

    # student_names =["Njoroge, George Stephen"]
    unique_emails = create_email_list(input_excel_path)
    # Create a DataFrame with an index
    df_output = pd.DataFrame({'Email Addresses': unique_emails}, index=range(1, len(unique_emails) + 1))
    # Store the output in a CSV file
    df_output.to_csv(output_csv_path, index=False)

    print("Unique email addresses have been saved to output.csv")




    # try:
    #     unique_emails = process_file(input_excel_path)
    #     if unique_emails is not None:
    #         # Create a DataFrame with an index
    #         df_output = pd.DataFrame({'Email Addresses': unique_emails}, index=range(1, len(unique_emails) + 1))
        

    #         # Store the output in a CSV file
    #         df_output.to_csv(output_csv_path, index=False)

    
    #     else:
    #         print("Error: The process_excel_file function returned None.")
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()