# **NBA Hall of Fame Predictions**

## **Selected topic**
Predicting if a National Basketball Association (NBA) player will be inducted into the Hall of Fame (HOF) based only on their draft position and rookie season statistics.

## **Reason why topic was selected**
After brainstorming we found that everyone in the group had an interest in sports. We knew there would be an abundance of data for professional sports leagues and decided to choose a topic involving the NBA. We were interested to see if there was any correlation between a player’s induction into the Hall of Fame and their draft and rookie season statistics.

## **Outline**

- Overview
    - Brainstormed topics
    - Found common interest in sports
    - Chose topic - NBA Hall of Fame predictions based on players draft and rookie season statistics
    
- Preprocessing
    - Inspected data
    - Replaced strings representing zeros with integer 0
    - Converted hyphens using the pandas '.to_numeric()' function
    - Filled in NaNs
    - Used pandas '.get_dummies()' function to separate Hall of Fame class columns into "Inducted" and "Not Inducted"
    
- Database
    - SQL
    - Pandas
    - PgAdmin
    - AWS

- Machine Learning
    - Supervised classification machine learning model was used (scikit-learn logistic regression method for our data fitting)
    - RandomOverSampler
    - SMOTE
    - SVM SMOTE

- Visualizations
    - Tableau dashboard
    - Interactive charts
    - Easy to read graphs that highlight every player from 1980 to 2008
    - Tableau stories
   
- View our [Google Slides presentation here](https://docs.google.com/presentation/d/1KHQcw8sbCei26WB8A8FRXLCDnFFpWTpy9OIAjOntWtc/edit?usp=sharing).

- View our Data files in the [DataPreperation folder]( https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/DataPreparation) or find it above.

- View our Database files in the [DB_Documentation folder](https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/DB_Documentation) or find it above.

- View our machine learning files in the [machine_learning folder]( https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/machine_learning) or find it above.

## **Data Source Description**
We found several datasets that contained data for this topic, but ultimately chose to use NBA Rookies by Year_Hall of Fame Class.xlsx found on [data.world]( https://data.world/gmoney/nba-rookies-by-min-1980-2016). This file was then converted into a csv (nba_hof_rookies.csv).

<img width="1004" alt="Data_image" src="https://user-images.githubusercontent.com/60076980/167962935-2c5b4c90-f5e9-4a8e-8895-c0e7bf329876.png">

## **Questions we hope to answer with the data**
- Can we accurately predict an NBA players induction into the Hall of Fame based on their statistics from their rookie season?
- Was there a correlation between rookie year statistics and length of career for players inducted into the Hall of Fame?

## **Data Exploration Phase**
- Description of preliminary data preprocessing

    *   There were a few irregularities upon first inspection of the data. The first step was replacing any strings representing zeros with the actual integer 0. For example, there were a few number of instances in the `3P%` column withihn the NBA_HOF_Rookies.csv file where, rather than a 0, a hyphen was entered. This resulted in the column being labeled as an `object` rather than a `float64` using the pandas `.dtypes`. This column would cause errors within our machine learning process. The hyphens were converted using the pandas `.to_numeric()` function with this code:

        ```rookies_df['3P%'] = rookies_df['3P%'].replace({'-':'0'})```

    *   The next step was filling in any NaNs. The majority of NaNs were found in the `Hall of Fame Class` and `Pick` columns since if a player had not been inducted or drafted, they would not have a number those cells. This was addressed by replacing and filling in these with the labels "Hall of Fame Member" and "Not Inducted" for the Hall of Fame column and adding a 0 to the Pick column for each respective player.

    *   Lastly, using the pandas `.get_dummies()` function our `Hall of Fame Class` column was encoded to separate the "inducted" and "not_inducted" players into separate columns since the "inducted" column will be our target for our machine learning model.  

To see specificlly how all of our datasets were cleaned and prepared for merging please refer to the [DataPreparation folder](https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/DataPreparation/DataCleaningNotebooks) in the repository.

To see all SQL statements and our Database ERD (image also below) please refer to the [DB_Documentation folder](https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/DB_Documentation) in the repository.

<img width="950" alt="Cleaned_data" src="https://user-images.githubusercontent.com/60076980/169674647-4cfff384-ab03-4f33-a389-6f226e77d5ce.png">

## **Technologies, Languages, Tools, and Algorithms Used**
- Python
    - Pandas
    - SciKit-Learn
    - Imbalanced-Learn
    - Matplotlib
    - Psycopg2
    - Pickle
    - InteractiveShell
- Jupyter Notebook
- PostgreSQL
- SQLAlchemy
- AWS
- PgAdmin
- Tableau

## **Machine Learning**

### **Analysis Phase**
- Description of preliminary feature engineering and preliminary feature selection, including the decision-making process

    *   Feature selection for this project was very straight forward, as most of the features were related to in-game statistics like points, shots made, shot attempts, turnovers, etc. These features were all kept as removing them had a negative impact on our machine learning model (see optimization table below). There were several non-performance related features like number of games played, average minutes played per game, and draft year, etc. These features were dropped since they did not directly relate to a player’s performance and would likely not help with the machine learning model. The only features that were kept for use in the model were those that were related to the players draft position, since these were a strong indication of a players ability coming into the NBA for their rookies season. 
    *   
- Description of how data was split into training and testing sets

    *   The data was shuffled and split into the training and test sets using the default parameters, which is `train_size = 0.25` and `test_size = 0.75` per [the sklearn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

### **Machine Learning Models Table**

This table shows each type of machine learning method that we used and the results. Oversampling was needed due to the highly imbalanced nature of our dataset, and because of this no Logistic Regression model was used without one.  

| **Model**           | **Over Sampler**   | **Results** |
|---------------------|-------------------|-------------|
| Logistic Regression | RandomOverSampler | ![](machine_learning/img/experiments/ros_results.png) |
| Logistic Regression | SMOTE             | ![](machine_learning/img/experiments/smote_results.png) |
| Logistic Regression | SVM SMOTE         | ![](machine_learning/img/experiments/svmsmote_results.png) |
| Decision Tree, Data Scaled    | n/a               | ![](machine_learning/img/experiments/dt_scaled_results.png) |
| Decision Tree, Data Not Scaled       | n/a               | ![](machine_learning/img/experiments/dt_not_scaled_results.png) |

*   To see the files used to run all these experiments, please refer to the [experiments folder](https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/machine_learning/experiments) in our repository.

Based on these results, the best perfoming model was Logistic Regression using sklearn's RandomOverSampler. This is because of the model's high train and test accuracy, low number of false negatives, and best F1 score. This model was used for optimization and deployment

### **Optimization Attempts Table**

This table shows the different optimization attempts made pertaining to feature selection. Each attempt experimented with dropping several related features with the idea being that if there were less features that were essentially saying the same thing, the model would be less confused. This would result in the machine learning model performing better overall. Each attempt was done using the best performing model from the table above, Logistic Regression using RandomOverSampler.

|                    **Dropped Features**                    |                 **Results**                |                                                             **Reason**                                                             |
|:----------------------------------------------------------:|:------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:|
|           Baseline: All Performance Features Kept.          | ![](machine_learning/img/optimization/opt_baseline.png) |                                                                 n/a                                                                |
| Keeping Shots Made Only. Drop: FGA, FG%, 3PA, 3P%, FTA, FT%. |     ![](machine_learning/img/optimization/opt_1.png)    |      Shots made, attempts, and percentage are all related to one another.  Keeping only shots made could help improve resutls.     |
|     Keeping Shots Made and Attempts. Drop: FG%, 3P%, FT%.     |     ![](machine_learning/img/optimization/opt_2.png)    |          Since keeping only shots made did not help improve results,  only dropping percentage to see if results improve.          |
|             Keeping Total Rebounds. Drop: OREB, DREB.             |     ![](machine_learning/img/optimization/opt_3.png)    | REB is the sum of OREB and DREB,  since we have the REB feature they may not be needed. |
|           Dropping All Optimization Attempt Features. Drop: FGA, FG%, 3PA, 3P%, FTA, FT%, OREB, DREB.          |     ![](machine_learning/img/optimization/opt_4.png)    |                        This attempt was a "long shot" type attempt to see the impact of dropping all features already tried at the same time.                        |
|           Dropping draft features. Drop: Pick, numberRound          |     ![](machine_learning/img/optimization/opt_5.png)    |                        This attempt was meant to see how/if only having performance related features improved the model                         |

*   To see the files used to run all these optimization attempts, please refer to the [optimizations folder](https://github.com/Kelcon86/NBA_HOF_Predictions/tree/main/machine_learning/optimizations) in our repository.

Based on these results, the baseline features (draft and all performance stats) had the best outcome. No features will be removed for model training for deployment.  

#### **Benefits and Limitations**

*   The largest limitation of our dataset is that it is highly imbalanced. The basketball Hall of Fame, which has existed since the inaugural class of 1959, has only, at most, **178** players. Our dataset, which has data going as far back as the draft class of 1980, has 42 Hall of Fame players out of the over 1200 usable players in the dataset. Because of this, we ran several imbalanced-learn oversampling methods. Please refer to the **Machine Learning Models Table** above to see the results.

*   Our model choice (Logistic Regression with RandomOverSampler oversampling) has one limitation that was shown in the results above in the Machine Learning Table. During training/testing there were 29 players that were misidentified as Hall of Fame players (false positive) where the SVMSMOTE model only had 17 such players. However, In a dataset as imbalanced as ours even just one Hall of Fame player misidentified as not a Hall of Fame player could have a significant impact, and this logic contributed to our choice to use it as our model for deployment. 

*   One of the benefits of our data is that it includes classifications, the "Hall of Fame Class" column, so we can use a supervised classification machine learning model. Specifically, we are using the **scikit-learn logistic regression** method for our data fitting. In addition, we are using the solver `liblinear` rather than the default solver since, according to [holypython.com](https://holypython.com/log-reg/logistic-regression-optimization-parameters/), it is a more efficient solver with smaller and imbalanced datasets.

#### **Explanation of Changes in Model Choice**

Between segments 2 and 3 was when we found the dataset that included draft information for the players that matched included all players from our dataset being used for training/testing. A decision was made by our group to include this data since, in theory, it would be a very strong indication of a player's anticipated performing in their rookie season, and therefor aid our model and its predictions. 

Upon joining the data and running all the experimental models again to look for differences in performance. We came to two important conclusions. 
*   First, that including the data did in fact improve the performance of our models, justifying its inclusion. 
*   Second, our best performing model had changed from Logistic Regression with the SVMSMOTE over sampler to Logistic Regression with the RandomOverSampler over sampler.

Because the best performing model had changed, all optimization were run again and this new final version of the model was used for deployment on the dataset.

### **Model Accuray**

*   Training Accuray - 88.27%
*   Testing Accuray - 85.08%
*   Deployment Accuary - 88.66%

![](machine_learning/img/CM/cm_sql_query.png)
    
*   Deployment accuracy calculated by taking the number of correct predictions (True Positives + True Negatives) over total rows (1217)

## **Database**
Using a combination of SQL, Pandas, Pgadmin and AWS multiple files were loaded, joined, and used as input to the analysis and modeling process. 

<img width="585" alt="ERD2" src="https://user-images.githubusercontent.com/60076980/172018262-64936ed8-de52-4f4d-9382-39cc9cafd55d.png">

## **Dashboard**
Using Tableau we are able create a story that helps visualize our project using several charts and interactive elements. 

One of our interactive elements is a moveable quadrant graph that highlights every player's Points Per Game(PPG) And Minutes Played(MP) in their rookie season.
   
<img width="760" alt="TableauStory3" src="https://user-images.githubusercontent.com/60076980/172018401-79f305af-9185-42ff-aa23-e56b4a7e6f4d.png">
