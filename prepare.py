import pandas as pd
import json
import acquire
import numpy as np
import os



def prep_source_data():
    retail_data, survey_data, ticket_data = acquire.import_data(json_file = 'retail.json',
        csv_file1 = 'surveys.csv',
        csv_file2 = 'tickets.csv')

    # Wrangle Retail_data

    # Add new column with transaction total calculation
    retail_data["transaction_total"] = retail_data["quantity"] * retail_data["unit_price"] + retail_data["shipping_cost"]
    # Rename the 'account_no' column as 'retail_account_no'
    retail_data = retail_data.rename(columns={'account_no': 'retail_account_no'})

    ##############################
    # Wrangle  Survey_data

    # Pivots data on submission ID
    survey_data = survey_data.pivot(index= 'Submission ID', columns= 'Attribute', values = 'Value')

    # Mapping for 'how_likely_are_you_to_attend_this_event_in_the_future'
    likelihood_mapping = {
        '5 - Very Likely': '5 - Very Likely',
        '4': '4 - Likely',
        '3': '3 - Neutral',
        '2': '2 - Unlikely',
        '1 - Very Unlikely': '1 - Very Unlikely'
    }
    survey_data['how_likely_are_you_to_attend_this_event_in_the_future'] = survey_data['how_likely_are_you_to_attend_this_event_in_the_future'].map(likelihood_mapping)

    # Mapping for 'how_satisfied_were_you_with_this_event'
    satisfaction_mapping = {
        '5 - Very Satisfied': '5 - Very Satisfied',
        '4': '4 - Likely',
        '3': '3 - Neutral',
        '2': '2 - Unlikely',
        '1 - Very Dissatisfied': '1 - Very Dissatisfied'
    }
    survey_data['how_satisfied_were_you_with_this_event'] = survey_data['how_satisfied_were_you_with_this_event'].map(satisfaction_mapping)

    # Mapping for 'how_satisfied_were_you_with_your_retail_experience_at_this_event'
    retail_experience_mapping = {
        '5 - Very Satisfied': '5 - Very Satisfied',
        '4': '4 - Likely',
        '3': '3 - Neutral',
        '2': '2 - Unlikely',
        '1 - Very Dissatisfied': '1 - Very Dissatisfied'
    }
    survey_data['how_satisfied_were_you_with_your_retail_experience_at_this_event'] = survey_data['how_satisfied_were_you_with_your_retail_experience_at_this_event'].map(retail_experience_mapping)

    #################################


    # Wangle ticket_data

    # Rename the 'account_no' column as 'ticketing_account_no'
    ticket_data = ticket_data.rename(columns={'account_no': 'ticketing_account_no'})
    
    
    return retail_data, survey_data, ticket_data


##################

retail_data, survey_data, ticket_data = prep_source_data()

def prep_fan_account():
    import prepare
    
    retail_data, survey_data, ticket_data = prepare.prep_source_data()


    # Concatenate the 'email' columns from ticket_data and retail_data dataframes
    emails = pd.concat([retail_data['email'], ticket_data['email']])

    # Create a new dataframe with unique email records
    new_df = pd.DataFrame({'email': emails.unique()})

    # Merge phone_no, zip, retail_account_no, and ticketing_account_no columns from ticket_data and retail_data based on email

    new_df = new_df.merge(ticket_data[['email', 'phone_no', 'zip', 'ticketing_account_no']], on='email', how='left')

    new_df = new_df.merge(retail_data[['email',  'retail_account_no']], on='email', how='left')

    # Fill null values in the specified column with 'N0RAcc0unt'. Value represent fan does not have retail account.
    new_df['retail_account_no'] = new_df['retail_account_no'].fillna('N0RAcc0unt')

    # Drop duplicates based on the email column
    new_df = new_df.drop_duplicates(subset=['email'])

    # Reset the index of the dataframe
    new_df = new_df.reset_index(drop=True)

    # Create a unique ID column using Concatenation 'clutch_' and location + 1 in the dataframe
    new_df['unique_id'] = 'clutch_' + (new_df.index + 1).astype(str)

    # Merge 'new_df' with the sum of 'transaction_total' per 'retail_account_no' from the 'retail_data' DataFrame, and merge the sum of 'total_price' per 'ticketing_account_no' from the 'ticket_data' DataFrame
    new_df = new_df.merge(retail_data.groupby('retail_account_no')['transaction_total'].sum().reset_index().rename(columns={'transaction_total': 'retail_spent_sum'}), on='retail_account_no', how='left') \
                    .merge(ticket_data.groupby('ticketing_account_no')['total_price'].sum().reset_index().rename(columns={'total_price': 'ticket_spent_sum'}), on='ticketing_account_no', how='left')


    # Replace NaN with 0 in column
    new_df['retail_spent_sum'].fillna(0, inplace=True)

    # Create new column with sum of two columns
    new_df['overall_sum'] = new_df['retail_spent_sum'] + new_df['ticket_spent_sum']

    # Get sum of 'qty' per 'ticketing_account_no' and merge it into 'new_df' as 'total_qty' column
    new_df = new_df.merge(ticket_data.groupby('ticketing_account_no')['qty'].sum().reset_index().rename(columns={'qty': 'total_tickets_purchased'}), on='ticketing_account_no', how='left') 
    # Get average of 'ticket_spent_sum' per 'ticketing_account_no' and merge it into 'new_df' as 'avg_per_ticket' column
    new_df['avg_per_ticket'] = new_df['ticket_spent_sum']/ new_df['total_tickets_purchased']


    # Updates column to round to 2 decimal places
    new_df['avg_per_ticket'] = new_df['avg_per_ticket'].round(2)

    # # Group by 'ticketing_account_no', find mode of 'section', merge and create 'favorite_section' column in 'new_df'
    new_df = new_df.merge(ticket_data.groupby('ticketing_account_no')['section'].agg(lambda x: x.mode().iat[0]).reset_index().rename(columns={'section': 'favorite_section'}), on='ticketing_account_no', how='left')

    # Create a new column in  with the retail transaction counts per fan and fill nonmatches with 0
    new_df = new_df.merge(retail_data.groupby('retail_account_no').size().reset_index(name='retail_transaction_count'), on='retail_account_no', how='left').fillna(0)

    # Create a new column in  with the ticket transaction counts per fan and fill nonmatches with 0
    new_df = new_df.merge(ticket_data.groupby('ticketing_account_no').size().reset_index(name='ticket_transaction_count'), on='ticketing_account_no', how='left').fillna(0)

    # Create a new column in  with the survey respone counts per fan and fill nonmatches with 0
    new_df = new_df.merge(survey_data.groupby('phone_no').size().reset_index(name='survey_submissions'), on='phone_no', how='left').fillna(0)


    new_df = new_df.merge(retail_data.groupby('retail_account_no')['product_type'].value_counts().unstack(fill_value=0).reset_index(), on='retail_account_no', how='left').fillna(0)

    columns_to_concat = ['Hat', 'Jersey', 'Misc', 'T-shirt']
    new_df.rename(columns={col: col + '_purchased' for col in columns_to_concat}, inplace=True)

    # Convert columns from float to integer
    columns_to_convert = ['retail_transaction_count', 'survey_submissions', 'Hat_purchased', 'Jersey_purchased', 'Misc_purchased', 'T-shirt_purchased']
    new_df[columns_to_convert] = new_df[columns_to_convert].astype(int)

    return new_df