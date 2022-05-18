# NBA Hall of Fame Predictions

## Selected topic
NBA Hall of Fame predictions based on players rookie year statistics

## Reason why topic was selected
After brainstorming we found that everyone in the group had an interest in sports. We knew there would be an abundance of data for professional sports leagues and decided to choose a topic involving the National Basketball Association (NBA). 

## Data Source Description
We found several datasets that contained data for this topic, but ultimately chose to use NBA Rookies by Year_Hall of Fame Class.xlsx found on data.world. This file was then converted into a csv (nba_hof_rookies.csv).

<img width="1004" alt="Data_image" src="https://user-images.githubusercontent.com/60076980/167962935-2c5b4c90-f5e9-4a8e-8895-c0e7bf329876.png">

## Questions we hope to answer with the data
- Can we accurately predict an NBA players induction into the Hall of Fame based on their statistics from their rookie season

## Description of the communication protocols
Our group has communicated through a dedicated Slack channel as well as via Zoom.


Segment 2 Rubric
The presentation outlines the project, including the following:

- Selected topic
- Reason topic was selected
- Description of the source of data
- Questions the team hopes to answer with the data
- Description of the data exploration phase of the project
- Description of the analysis phase of the project

Slides
- Presentations are drafted in Google Slides.

- Description of the communication protocols
- Outline of the project (this may include images, but they should be easy to follow and digest)

Machine Learning:
- Description of preliminary data preprocessing

    *   The preliminary data preprocessing began prior to the data being loaded into the database. There were a few irregularies apon first inspection of the data. The first step was replacing any strings representing zeros with the actual interger 0. There were a few number of instantces in the `3P%` column where, rather than a 0, a hyphen was entered. This resulted in the column being labled as an `object` rather than a `float64` using the pandas `.dtypes`. This column would cause errors within our machine leanring process. The hyphens were converted using the pandas `.to_numeric()` function with this code:

        ```rookies_df['3P%'] = rookies_df['3P%'].replace({'-':'0'})```

    *   The next step was filling in any NaNs. The majority of NaNs were found in the `Hall of Fame Class` column since if a player had not been inducted, they would not have a class year assoicated with them. This was addressed by replacing and filling in these with the labels "Hall of Fame Member" and "Not Inducted".

    *   Lastly, using the pandas `.get_dummies()` function our `Hall of Fame Class` column was encoded to separate the "inducted" and "not_inducted" players into separate columns since the "inducted" column will be our target for our machine learning model.   

- Description of preliminary feature engineering and preliminary feature selection, including the decision-making process

    *   Feature selection has been minimal at this point in our project, but at our instructor's advice we began by removing the `year_drafted` and `gp (games played)` columns to allow our machine learning model to focus purly on in-game statics like points, shots made, shot attempts, turnovers, etc.

- Description of how data was split into training and testing sets
- Explanation of model choice, including limitations and benefits

Dashboard (15 points)
- A blueprint for the dashboard is created and includes all of the following:

- Storyboard on a Google Slide(s)
- Description of the tool(s) that will be used to create the final dashboard
- Description of interactive element(s)


