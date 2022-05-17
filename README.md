# PROJECT 1: DATA MODELING WITH PostgresSQL
### MOTIVATION
This project uses Sparkify database. Sparkify  wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.
As a data engineer, it is required to create a Postgres database schema and ETL pipeline for this analysis. The data is collected in JSON format and resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
### PROJECT DESCRIPTION
In this we weill define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# SCHEMA DESIGN 
The star schema has 1 fact table (songplays) and 4 dimensions tables(users,songs,time,artists). The pictorial representation is shown below.
![sparkifydb_erd (1)](https://user-images.githubusercontent.com/12171326/168804621-2453f4dd-47d0-49c4-9030-cd0e53b0f9be.png)


# RELEVANT FILES FOR THIS PROJECT
-test.ipynb displays the first few rows of each table to let you check your database.
-create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
-etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
-etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
-sql_queries.py contains all your sql queries, and is imported into the last three files above.
# DATASET
         Data
        data/song_data: contains all files for song data in JSON
        data/log_data: contains all files for log data in JSON.
# PROJECT STEPS
### 1.Create Tables 
   - Write create and drop tables queries in *sql queries.py*
   - Run *create_tables.py* to create your database and tables.
   - Run *test.ipynb* to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.
 
### 2.Build ETL Processes
Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.

### 3.Build ETL Pipeline
Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

### Sanity tests
These are additional tests to foolproof the work and ensure there are no errors.

### EXAMPLE QUERIES AND RESULTS FOR SONGPLAY ANALYSIS
![1](https://user-images.githubusercontent.com/12171326/168804350-f18e4c7d-23c5-4203-b574-800cd7512d82.PNG)
![2](https://user-images.githubusercontent.com/12171326/168804378-4dc5ff61-3fb3-4484-b267-09e631f1390a.PNG)


    
