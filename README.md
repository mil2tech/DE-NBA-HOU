<img src="rockets.jpeg" alt="drawing" width="700" height="405"/>

# <a name="top"></a>Rockets Data Engineer Challenge
![]()


By:  Jarrid Jones 

<p>
  <a href="https://github.com/mil2tech" target="_blank">
    <img alt="Jarrid" src="https://img.shields.io/github/followers/mil2tech?label=Follow_Jarrid&style=social" />
  </a>
</p>


**Tools & Technologies Used:** 

![](https://img.shields.io/static/v1?message=Python&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Pandas&logo=pandas&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=NumPy&logo=numpy&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Markdown&logo=markdown&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=GitHub&logo=github&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=JupyterLab&logo=jupyter&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Conclusion](#conclusion)]
___

## <a name="project_description"></a>Project Description:

The purpose of this project is to integrate and analyze the diverse range of data collected by the Houston Rockets, including ticket transactions, retail sales, and fan surveys. The current challenge lies in the fact that the data is sourced from various systems and formats, making it difficult to gain comprehensive insights about the team's fan base. By creating a unified database table, this project aims to provide the Business Intelligence & Innovation team with a consolidated dataset that can be leveraged to build fan segments and understand their behaviors effectively.

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:

- Review requirements from stakeholder to determine needs.
- Review Project source files.
- Create py scripts for both data acquisition and wrangling.
- Create final notebook for technical review that consist minimum code.
- Draft each section of README as project progresses
- Reach out to stakeholder for review and project completion 

        
### Inital Questions

- What file format will be the data?
- What barriers will I encouter with source data?
- What format is the data? Structure vs unstructure vs semi-structured


### Need to haves (Deliverables):
- First what is needed:
  - Project files
In order to dowload project files, you will need to have navigate to Houston Rockets Github  <a href="https://htxrockets.com/redirect/to/id?id=148" target="_blank">repository</a>.

- Aquire.py - Script of data acquition of all data from project source files.
- Prepare.py - Script of wrangling data to an unified database table that meets the requirements of the stakeholder.
- Final notebook to run project resulting with unified database table.
- README

### Nice to haves (With more time):

- A Dashboard using unified database table.

- EDA notebook to further analyze and investigate and summerize all data sets with visualizations.


***

## <a name="dictionary"></a>Data Dictionary 

<details>
  <summary>Click to expand!</summary>

**Tickets.csv** - Ticket sales transactions over the course of 41 home games.

|   Field Name      |   Description                                                     |
|-------------------|-------------------------------------------------------------------|
|   transaction_id  |   identification number for ticket transaction                    |
|   account_no      |   customer account number                                         |
|   email           |   customer email address                                          |
|   zip             |   customer zip code                                               |
|   phone_no        |   customer phone number                                           |
|   section         |   section of the arena that the tickets were purchased for        |
|   row             |   row of the section that the tickets were purchased for          |
|   qty             |   quantity of tickets purchased in transaction                    |
|   total_price     |   total transaction price                                         |
|   event_id        |   identification number for event the tickets were purchased for  |
|   channel         |   distribution channel for ticket transaction                     |



**Retail.json** - Online retail Purchases

|   Field Name      |   Description                                       |
|-------------------|-----------------------------------------------------|
|   transaction_id  |   identification number for the retail transaction  |
|   email           |   customer email address                            |
|   account_no      |   customer account number                           |
|   product_type    |   type of product purchased                         |
|   quantity        |   quantity of items purchased                       |
|   unit_price      |   price per unit                                    |
|   shipping_cost   |   shipping cost for the transaction                 |



**Surveys.csv**  - Melted response data from post-game surveys

|   Field Name                                                        |   Description                                                                                              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
|   Submission ID                                                     |   unique identifier for each survey submitted (hint: can be used as index for pivot table of responses)    |
|   phone_no                                                          |   survey respondent phone number                                                                           |
|   event_id                                                          |   identification number for the event related to the survey                                                |
|   how_satisfied_were_you_with_this_event                            |   5-point scale response to question: "How satisfied were you with this event?"                            |
|   how_satisfied_were_you_with_your_retail_experience_at_this_event  |   5-point scale response to question: "How satisfied were you with your retail experience at this event?"  |
|   how_likely_are_you_to_attend_this_event_in_the_future             |   5-point scale response to question: "How likely are you to attend this event in the future?"             |
|   what_is_your_birthdate                                            |   survey respondent's date of birth                                                                        |
|   what_is_your_household_income                                     |   survey respondent's household income range                                                               |
|   what_is_your_highest_level_of_education_that_you_have_attained    |   survey respondent's highest level of education                                                           |

**Unified Database** - single table that used the available data sources to create a unified database table that Business Intelligence & Innovation team could leverage to build fan segments and determine their behaviors.

| email                    	| customer email address                                	|
|--------------------------	|-------------------------------------------------------	|
| phone_no                 	| customer phone number                                 	|
| zip                      	| customer zip code                                     	|
| ticketing_account_no     	| customer account number for ticket purchases          	|
| retail_account_no        	| customer account number for retail purchases          	|
| unique_id                	| customer unique identifer (use as primary key)         	|
| retail_spent_sum         	| dollar sum of retail purchases of customer            	|
| ticket_spent_sum         	| dollar sum of ticket purchases of customer            	|
| overall_sum              	| dollar sum of retail and ticket purchases of customer 	|
| total_tickets_purchased  	| overall number of tickets customer purchased          	|
| avg_per_ticket           	| dollar average of customer tickets                    	|
| favorite_section         	| section of the arena where customer is likely to sit  	|
| retail_transaction_count 	| sum of all retail purchases of customer               	|
| ticket_transaction_count 	| sum of all ticket purchases of customer               	|
| survey_submissions       	| sum of survey submissions of customer                 	|
| Hat_purchased            	| number of hats customer purchased                     	|
| Jersey_purchased         	| number of jerseys customer purchased                  	|
| Misc_purchased           	| number of non apparel items customer purchased        	|
| T-shirt_purchased        	| number of t-shirts customer purchased                 	|

</details>

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()
Download project files
- The first step is to <a href="https://htxrockets.com/redirect/to/id?id=148" target="_blank">download</a> project folder .

Review <a href="https://hourockets.github.io/challenge-bde" target="_blank">requirements</a> of the stakeholder .

Acquire.py
  - Import these libraries:
    ```python
        import os
        import pandas as pd
        import json
    ```

  - Create a function that will connect to the API and retrives the access token with similar code:
    ```python
        def import_data(json_file, csv_file1, csv_file2):
   
    # Import JSON file into a dataframe
    with open(json_file) as f:
        json_data = json.load(f)
    retail_data = pd.DataFrame(json_data["retail"], columns=["transaction_id", "email", "account_no", "product_type", "quantity", "unit_price", "shipping_cost"])

    # Import CSV files into dataframes
    survey_data = pd.read_csv(csv_file1)
    ticket_data = pd.read_csv(csv_file2)
    
    return retail_data, survey_data, ticket_data
    ```
 
  - Save acquire.py

- Prepare.py

  - Import these libraries:
  ```python
    import pandas as pd
    import json
    import acquire
    import prepare
    import numpy as np
    import os
  ```
  - Create a function that will import data sources into notebook using import_data function from acquire.py. Next, it will start data wrangling each dataframe and return each dataframe separately.
  ```python
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
  ```
  
  - Assigning the return values of the prep_source_data() function to three separate variables: retail_data, survey_data, and ticket_data.
  ```python
      retail_data, survey_data, ticket_data = prep_source_data()
  ```
  -  Create a function that will create new columns for list objects in a field
  ```python
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
  ```
  - Assigning the return value of the prep_fan_account() function to a variable: new_df
   ```python 
        new_df = prepare.prep_fan_account()
    ```
  - Save prepare.py

  - Execute the follow codeblocks to get unified database:

  Imports data to notebook
   ```python 
        retail_data, survey_data, ticket_data = acquire.import_data(json_file = 'retail.json',
    csv_file1 = 'surveys.csv',
    csv_file2 = 'tickets.csv')
    ```
  Wrangles all source data
    ```python 
        retail_data, survey_data, ticket_data = prepare.prep_source_data()
    ```
  Wrangles cleaned source data that constructs unified database
    ```python 
        new_df = prepare.prep_fan_account()
    ```
  Displays unified database
    ```python 
        new_df
    ```  
  
  
*********************

## <a name="conclusion"></a>Conclusion:

- After acquiring data from data sources provided, I was able to successfully wrangle three data sets to build a unified fan database table that can be used to make business insights. The database is 500 rows and 19 columns.  It contains fans' contact information, summary of spending for retail and ticket purchases for each fan, and an unique identifier for each fan that acts as a primary key.


## Next Steps and Recommendations: 

- Create a Dashboard using unified database
- Add additional demographic data like gender and race.


[[Back to top](#top)]
