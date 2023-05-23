import pandas as pd
import json

 # Usage of function; associate variables with the name of respected file names
json_file = 'retail.json'
csv_file1 = 'surveys.csv'
csv_file2 = 'tickets.csv'

def import_data(json_file, csv_file1, csv_file2):
   
    # Import JSON file into a dataframe
    with open(json_file) as f:
        json_data = json.load(f)
    retail_data = pd.DataFrame(json_data["retail"], columns=["transaction_id", "email", "account_no", "product_type", "quantity", "unit_price", "shipping_cost"])

    # Import CSV files into dataframes
    survey_data = pd.read_csv(csv_file1)
    ticket_data = pd.read_csv(csv_file2)
    
    return retail_data, survey_data, ticket_data