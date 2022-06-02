# database credentials
host = 'nba-hof-project.cxpeww6dbftb.us-east-2.rds.amazonaws.com'
port = 5432
user = 'postgres'
password = 'tC1sfkNBaUqSH4noRcz6'
database = 'postgres'
engine = 'postgresql+psycopg2://postgres:tC1sfkNBaUqSH4noRcz6@nba-hof-project.cxpeww6dbftb.us-east-2.rds.amazonaws.com:5432/postgres'


# full engine string for writing to the database, if it needs to be referenced

# 'postgresql+psycopg2://postgres:tC1sfkNBaUqSH4noRcz6@nba-hof-project.cxpeww6dbftb.us-east-2.rds.amazonaws.com:5432/postgres'

# f'{c.user}ql+psycopg2://{c.host}:{c.password}@{c.host}:{c.port}/{c.database}'