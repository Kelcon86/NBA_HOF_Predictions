# NBA Hall of Fame Predictions

view our presentation [[here](url)].

## Selected topic
NBA predictions based on players rookie year statistics.

## Reason why topic was selected
After brainstorming we found that everyone in the group had an interest in sports. We knew there would be an abundance of data for professional sports leagues and decided to choose a topic involving the National Basketball Association (NBA). We initially were interested to see if there was any correlation between a players induction into the Hall of Fame and their rookie year statistics.

## Data Source Description
We found several datasets that contained data for this topic, but ultimately chose to use NBA Rookies by Year_Hall of Fame Class.xlsx found on data.world. This file was then converted into a csv (nba_hof_rookies.csv).

<img width="1004" alt="Data_image" src="https://user-images.githubusercontent.com/60076980/167962935-2c5b4c90-f5e9-4a8e-8895-c0e7bf329876.png">

## Questions we hope to answer with the data
- Can we accurately predict an NBA players induction into the Hall of Fame based on their statistics from their rookie season
- Were rookie players in a certain position more likely to be inducted into the Hall of Fame?
- Was there a correlation between rookie year statistics and length of career for players inducted into the Hall of Fame?

## Description of the communication protocols
Our group has communicated through a dedicated Slack channel as well as via Zoom.

## Data Exploration Phase
- Description of preliminary data preprocessing

    *   The preliminary data preprocessing began prior to the data being loaded into the database. There were a few irregularities upon first inspection of the data. The first step was replacing any strings representing zeros with the actual integer 0. There were a few number of instances in the `3P%` column where, rather than a 0, a hyphen was entered. This resulted in the column being labeled as an `object` rather than a `float64` using the pandas `.dtypes`. This column would cause errors within our machine learning process. The hyphens were converted using the pandas `.to_numeric()` function with this code:

        ```rookies_df['3P%'] = rookies_df['3P%'].replace({'-':'0'})```

    *   The next step was filling in any NaNs. The majority of NaNs were found in the `Hall of Fame Class` column since if a player had not been inducted, they would not have a class year associated with them. This was addressed by replacing and filling in these with the labels "Hall of Fame Member" and "Not Inducted".

    *   Lastly, using the pandas `.get_dummies()` function our `Hall of Fame Class` column was encoded to separate the "inducted" and "not_inducted" players into separate columns since the "inducted" column will be our target for our machine learning model.  

<img width="950" alt="Cleaned_data" src="https://user-images.githubusercontent.com/60076980/169674647-4cfff384-ab03-4f33-a389-6f226e77d5ce.png">



## Machine Learning 

### Analysis Phase
- Description of preliminary feature engineering and preliminary feature selection, including the decision-making process

    *   Feature selection has been minimal at this point in our project, but at our instructor's advice we began by removing the `year_drafted` and `gp (games played)` columns to allow our machine learning model to focus purely on in-game statics like points, shots made, shot attempts, turnovers, etc.

- Description of how data was split into training and testing sets

    *   The data was shuffled and split into the training and test sets using the default parameters, which is `train_size = 0.25` and `test_size = 0.75` per [the sklearn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

- Explanation of model choice, including limitations and benefits


    *   The largest limitation of our dataset is that it is highly imbalanced. The basketball Hall of Fame, which has existed since the inaugural class of 1959, has only, at most, **178** players. Our dataset, which has data going as far back as the draft class of 1980, has less than 40 Hall of Fame players out of the over 1500 players in the dataset. Because of this, we ran several imbalanced-learn oversampling methods following the train-test splitting.
        *   The three oversampling methods we have used so far include:
            *   RandomOverSampler
            *   SMOTE
            *   SVM SMOTE
    *   One of the benefits of our data is that it includes classifications, the "Hall of Fame Class" column, so we can use a supervised classification machine learning model. Specifically we are using the **scikit-learn logistic regression** method for our data fitting. In addition, we experimented with the `solver=liblinear` rather than the default `solver=lbfgs` since according to [this website](https://holypython.com/log-reg/logistic-regression-optimization-parameters/) it is a more efficient solver with smaller datasets. Preliminary results show an improvement in our model accuracy using this solver vs "lbfgs".

## Database
Using a combination of SQL, Pandas, and the Pgadmin tool multiple files were loaded, joined, and used as input to the analysis and modeling process. 

<img width="561" alt="ERD_image" src="https://user-images.githubusercontent.com/60076980/169675214-90f44036-7bb6-4646-9384-ee35dcd8df4a.png">

## Dashboard
We will be using Tableau to create a dashboard. 


Segment 2 Rubric
The presentation outlines the project, including the following:

- Selected topic
- Reason topic was selected
- Description of the source of data
- Questions the team hopes to answer with the data
- Description of the data exploration phase of the project
- Description of the analysis phase of the project


- Description of the communication protocols
- Outline of the project (this may include images, but they should be easy to follow and digest)

Dashboard (15 points)
- A blueprint for the dashboard is created and includes all of the following:

- Storyboard on a Google Slide(s)
- Description of the tool(s) that will be used to create the final dashboard
- Description of interactive element(s)
