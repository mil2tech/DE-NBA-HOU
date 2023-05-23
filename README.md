<img src="igdb.jpeg" alt="drawing" width="150"/>

# <a name="top"></a>Videogame-Capstone
![]()
Kalpana Cohort 2022

By:  Jarrid Jones 

<p>
  <a href="https://github.com/lindyc12" target="_blank">
    <img alt="Lindy" src="https://img.shields.io/github/followers/lindyc12?label=Follow_Lindy&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/mil2tech" target="_blank">
    <img alt="Jarrid" src="https://img.shields.io/github/followers/mil2tech?label=Follow_Jarrid&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/GladyBarrios" target="_blank">
    <img alt="Glady" src="https://img.shields.io/github/followers/GladyBarrios?label=Follow_Glady&style=social" />
  </a>
</p>
**Tools & Technologies Used:** 

![](https://img.shields.io/static/v1?message=Python&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Pandas&logo=pandas&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciKit-Learn&logo=scikit-learn&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=SciPy&logo=scipy&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=NumPy&logo=numpy&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=MatPlotLib&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Seaborn&logo=python&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Tableau&logo=tableau&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=Markdown&logo=markdown&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=GitHub&logo=github&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)
![](https://img.shields.io/static/v1?message=JupyterLab&logo=jupyter&labelColor=5c5c5c&color=blueviolet&logoColor=white&label=%20)


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

## <a name="project_description"></a>Project Description:

The purpose of this project is to integrate and analyze the diverse range of data collected by the Houston Rockets, including ticket transactions, retail sales, and fan surveys. The current challenge lies in the fact that the data is sourced from various systems and formats, making it difficult to gain comprehensive insights about the team's fan base. By creating a unified database table, this project aims to provide the Business Intelligence & Innovation team with a consolidated dataset that can be leveraged to build fan segments and understand their behaviors effectively.

[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:


        
### Inital Questions

-  Do video games on certain platforms get better user ratings?
- what is the most common genre in games that are `subperb` (the highest rating)?
  - what about the three lowest ratings ((bad, very bad , awful)) ? what is the overall most highest genre in these low rating games?
  - what about the three highest ratings (good, great, subperb) ? what is the overall most highest genre?
- what is the most common theme in games that are subperb (the highest rating)?
  - what is the most common theme in games that are three highest ratings (good, great, subperb)?
  - what is the most common theme in games that are three lowest ratings ((bad, very bad , awful)
- Do users rate games with online multiplayer modes higher than games that lack online multiplayer modes?  

### Target variable?
  
  Our target variable is to be able to idetify the diffrent variables that make a videogame have a high rating 

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

</details>

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()
Download project files
- The first step is to <a href="https://htxrockets.com/redirect/to/id?id=148" target="_blank">download</a> project folder .

Review <a href="https://hourockets.github.io/challenge-bde" target="_blank">requirements</a> of the stakeholder .

  - Create a .gitignore just in case not cloning our repo to exclude env.py , *.json files.

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
    import time
    import acquire
    import numpy as np
    import seaborn as sns
  ```
  - Create a function that will import json object into notebook if json object is already saved in /data folder into a dictionary. If json not availble, fuction will acquire data from API endpoint and save as .json
  ```python
      def import_table(variable):
        path = variable['path']
        getter = variable['getter']
        if not os.path.exists(path):
            wrapper = acquire.run_wrapper()
            df = getter(wrapper)
            df = df.reset_index().drop(columns=['index'])
            df.to_json(path)
        else:
            df = pd.read_json(path)
        return df
  ```
  - Create dictionary object that will have a keyword assoiated with a path and a function in the acquire.py 

  ```python
      config = {
        'game_library' : {
            'path' : 'data/game_library.json',
            'getter': acquire.get_game_library
        },
        'genres' : {
            'path' : 'data/genres.json',
            'getter': acquire.get_genres
        },
        'age_ratings' : {
            'path' : 'data/age_ratings.json',
            'getter': acquire.get_age_ratings
        },
        'age_rating_desc' : {
            'path' : 'data/age_rating_desc.json',
            'getter': acquire.get_age_rating_desc
        },
        'collections' : {
            'path' : 'data/collections.json',
            'getter': acquire.get_collections
        },
        'game_modes' : {
            'path' : 'data/game_modes.json',
            'getter': acquire.get_game_modes
        },
        'multi_player_modes' : {
            'path' : 'data/multi_player_modes.json',
            'getter': acquire.get_multi_player_modes
        },
        'platforms' : {
            'path' : 'data/platforms.json',
            'getter': acquire.get_platforms
        },
        'platform_families' : {
            'path' : 'data/platform_families.json',
            'getter': acquire.get_platform_families
        },
        'player_perspectives' : {
            'path' : 'data/player_perspectives.json',
            'getter': acquire.get_player_perspectives
        },
        'themes' : {
            'path' : 'data/themes.json',
            'getter': acquire.get_themes
        },
        'game_engines' : {
            'path' : 'data/game_engines.json',
            'getter': acquire.get_game_engines
        },
        'age_rating_desc' : {
            'path' : 'data/age_rating_desc.json',
            'getter': acquire.get_age_rating_desc
        },
    }
  ```
  - Create a function that retrive all tables from the config dict
  ```python
      def get_tables():
          tables = {}
          for key, value in config.items():
              tables[key] = import_table(value)
              # print(f'Completed import for {key}')
          return tables
  ```
  -  Create a function that will create new columns for list objects in a field
  ```python
      def my_list(column, word):
        if word in column:
            return 1
        else:
            return 0
  ```
  - Run the `get_tables()`
  - Create  variable `to_keep` with a list object of columns to keep
  - Add a pointer to the game library dictionary object
    ```python 
        game_library = tables['game_library']
    ```
  - Trim down to only columns we care about
    ```python
        game_library = game_library[to_keep].copy()
    ```
  - Convert `game_library['first_release_date']` to datatime object
  - Add multiplayer_modes to game_library from the multiplayer_modes endpoint
    ```python
        tables['multi_player_modes'].rename(columns={'id': 'multi_player_mode_id'}, inplace=True)
    # dataframe merging game_library and multi_player_modes with left join. 
    game_library = pd.merge(
            game_library, tables['multi_player_modes'], how='left', left_on = 'id', right_on = 'game'
            ).drop(columns=[ 'game', 
                            'checksum', 
                            'multi_player_mode_id', 
                            'platform'
                            ])
    ```
  - Fill in null values and drop `multiplayer_modes`
    ```python
        # fill nulls with 0 or bool lean False
    game_library['campaigncoop'].fillna(False, inplace = True)
    game_library['dropin'].fillna(False, inplace = True)
    game_library['lancoop'].fillna(False, inplace = True)
    game_library['offlinecoop'].fillna(False, inplace = True)
    game_library['offlinemax'].fillna(0, inplace = True)
    game_library['onlinecoop'].fillna(False, inplace = True)
    game_library['splitscreen'].fillna(False, inplace = True)
    game_library['offlinecoopmax'].fillna(0, inplace = True)
    game_library['onlinecoopmax'].fillna(0, inplace = True)
    game_library['onlinemax'].fillna(0, inplace = True)

    game_library.drop(columns=['multiplayer_modes'], inplace=True)
    ```
  - Make a dictionary for id and string to convert id to the nomenclature. Afterwards make new columns for each genre.
    ```python
        # Transform genres list to a list of strings instead of a list of ids
        genres_list = tables['genres'][['id' , 'slug']].sort_values(by='id').reset_index(drop=True)
        genres_dict = genres_list.set_index('id').to_dict()['slug']
        def convert_genres_col(random_list):
            if type(random_list) == list:
                return [genres_dict[i] for i in random_list]
            else:  
                return ['Not available']
        game_library['genres'] = pd.DataFrame(game_library.genres.apply(convert_genres_col))
        # list of genres to add
        genres = ['point-and-click', 'fighting', 'shooter', 'music', 'platform', 'puzzle', 'racing', 'real-time-strategy-rts', 'role-playing-rpg', 'simulator', 'sport', 'strategy', 'turn-based-strategy-tbs', 'tactical', 'hack-and-slash-beat-em-up', 'quiz-trivia', 'pinball', 'adventure', 'indie', 'arcade', 'visual-novel', 'card-and-board-game', 'moba']
        # function to loop through column list and check for genre
        for item in genres:
            game_library[item] = game_library['genres'].apply(my_list, word=item)
    ```
  - above code block was utilized to transform columns `game_modes`, `player_perspectives`, `themes`, and `platforms`.
  - Modified the `dlcs` column to a bootlean column with the following code:
    ```python
        # Modified DLC column
    game_library['dlcs'] = game_library['dlcs'].fillna(0)

    def dlcs_col(df):
        game_library['has_dlcs'] = np.where(game_library.dlcs != 0, 1, 0)  
        return df
    game_library = dlcs_col(game_library)
    ```
  - The `ratings` column was used to create a new column `rating_bin` which contained the rating scale nomenclature.
    ```python
        game_library['rating_bin'] = pd.cut(game_library.rating, 
                           bins = [0,10,20, 30, 40, 50, 60, 70, 80, 90, 100],
                           labels = ['awful','very_bad','bad','unimpressive','average','fair','alright','good','great', 'subperb'])
    ```
  - Create a variable `cols_to_drop` with the list object containing 
        ```python
        'dlcs',
        'game_modes',
        'offlinemax' ,
        'offlinecoopmax',
        'onlinecoopmax',
        'onlinemax',
        'rating',
        'age_ratings' 
        ```
  - Modify `game_libray` with the following:
    ```python
        game_library = game_library.drop(columns=cols_to_drop)
    ```
  - Create a function that will convert all True and False values as 0 and 1. Apply the fuction to `game_library`
    ```python
        def replace_booleans(data):
        for col in data:
            data[col].replace(True, 1, inplace=True)
            data[col].replace(False, 0, inplace=True)

        replace_booleans(game_library)
    ```
  - Create two data frames. One with valid observations in `rating_bin`, and another with null values in 'rating_bin'.
    ```python
        game_ratings = game_library[game_library['rating_bin'].notnull()]
        not_rated = game_library[game_library['rating_bin'].isnull()]
    ```
  - Create a function with all the above code tasks into a function `wrangle_data()` that returns `game_library` , `game_ratings` , `not_rated`
    ```python
        game_library , game_ratings , not_rated = wrangle_data()
    ```
  - Split `game_ratings` into three data samples: train, validate, and test. Create variables `X_train` , `y_train` , `X_validate` , `y_validate` , `X_test`, and `y_test`.
    ```python
       def split(game_ratings, stratify_by='rating_bin'):
          # split df into train_validate 
          train_validate, test = train_test_split(game_ratings, test_size=.20, random_state=13)
          train , validate = train_test_split(train_validate, test_size=.3, random_state=13)
          X_train = train.drop(columns=['rating_bin'])
          y_train = train[['rating_bin']]

          X_validate = validate.drop(columns=['rating_bin'])
          y_validate = validate[['rating_bin']]

          X_test = test.drop(columns=['rating_bin'])
          y_test = test[['rating_bin']]

          return train, X_train, X_validate, X_test, y_train, y_validate, y_test
    ```
  
*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - aquire.py 
    - prepare.py
    


### Takeaways from exploration:
_Question 1 - Do video games on certain platforms get superb user ratings?_

          - the most common platforms are `PC(microsoft Windows)`, `Play Station 4`, `X-Box one`, `Nintendo Switch`
 
  Sub Question 1.1 - What about the three lowest ratings (bad, very bad, awful)?  
  
          - PC (Microsoft Windows)
          - MAC
          - Nintendo Switch
    
_Question 2 - what is the most common genre in games that are superb?¶_

          - the most common platforms are `Indie`, `Adventure`, `Role-Playing-RPG`, `Shooter`
 
   Sub Question 2.1 - What about the three lowest ratings (bad, very bad, awful)?
      
      
         - Indie 
         - adventure
         - simulator
         - indie  


_Question 3 - What is the most common theme in games that are subperb (the highest rating)_ 

         - the most common themes in the subperb is action, fantasy, science fiction, Open World.
    
  Question 3.1 - what is the most common theme in games that are three lowest ratings ((bad, very bad , awful))?
  
          - the most common game these in the lowest ratings Action, Science fiction, Horror, Fantasy 
***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation: 
- Before modeling we had to drop addition columns and used Chi-Squared test for feature selection on the split data. We also made datframes to hold the models predictions.

### Baseline
    
- Baseline Results: Mode of rating class "Alright" for a baseline of 0.28
    

- Chi-Squared selected features:
    - features = ['offlinemax', 'onlinecoop', 'onlinemax', 'shooter', 'indie', 'PC (Microsoft Windows)', 'PlayStation3', 'Xbox360', 'iOS', 'PlayStation4', 'Xbox one', 'Science Fiction', 'Fantasy', 'Historical', 'Stealth', 'Comedy', 'Open world', 'Third person', 'Bird view / Isometric', 'Side view']

***

### Models:
- Will run the following classification models:
  - Random Forest
  - Decision Tree
  - Logistic Regression
  - One Vs. Rest Classifier
  - K-Nearest Neighbor

    

- For the models it was important that features of games (player perspective, genres, themes, ect.) be turned into their own binary columns, as well as converting any boolean columns. Doing this will greatly help the models predictions.
    
    
#### Model 1: Random Forest

- Train data RF best perforance: max depth of 27 and accuracy of 0.66
- Validate data RF best perforance: max depth 15 had accuracy of 0.37

### Model 2 : Decision Tree

- Train data DT best perforance: max depth of 29 and accuracy of 0.63
- Validate data DT best perforance: max depth 9 had accuracy of 0.38

### Model 3 : Logistic Regression

- Train data LR best perforance: 0.34
- Validate data LR best perforance: 0.34

### Model 4: One Vs. Rest

- Train data LR best perforance: 0.34
- Validate data LR best perforance: 0.34

### Model 5: KNN

- Train data KNN best perforance: max depth of 1 with an accuracy of 0.60
- Validate data KNN best perforance: max depth of 23 with an accuracy of 0.34


## Selecting the Best Model: 
  - The best performing model was Random Forest with a max depth of 15 on validate. That will be the model used on test data.

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample accuracy | 
| ---- | ----| 
| Baseline | 0.284647 | 
| Random Forest (RF) | 0.369651 |   
| Decision Tree (DT) | 0.346415	 |  
| Logistic Regression (LR) | 0.344007|  
| K-Nearest Neighbor (KNN) | 0.344148	 |   
| One Vs. Rest | 0.356869 | 

- {Random Forest} model performed the best


## Testing the Model

- Model Testing Results
  - All the models beat baseline on train, validate and test. We trained all of the models in two rounds; the first using Chi-Squared feature selection and the second without using it. All of the models preformed marginally better when trained with with all of the features we created in our dataset. Random Forest preformed the best on validate both with the feature selection and without. We ran it on the test data set and beat baseline with an accuracy of 0.388625
***

## <a name="conclusion"></a>Conclusion:

- After acquiring data from the IGDB API we were able to build five classification models that were trained on games with ratings, and all were able to beat the baseline. We used the model with the highest accuracy, Random Forest, to predict what class games without ratings would have based on their features. Having this insight will greatly improve any video games that will be made in the feature in regards to user ratings.


## Next Steps: 

- Next we would like to acquire more features from other API's like critic ratings and play through length to merge into the game_library dataframe, and giving the models even better accuracy.
- Exploring games with low ratings to see what features contribute to low performance for game reviews.
- Use NLP on reviews to better understand user/critic tone.
- Use regression models to predict numeric ratings.

[[Back to top](#top)]
