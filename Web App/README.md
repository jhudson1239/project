# mcomp_project
Repo for my mcomp project

To get the application up and running follow these steps:

1) Clone the repo
2) Navigate to the root of the cloned folder in a terminal window
3) Run "composer install"
4) Within the root folder the file called ".env.example" rename it to ".env."
5) In the terminal window run the command "php artisan key:generate"
5) Create a new local database called mcomp
6) Connect the new .env file to the local database by changing the following lines of code within the .env file

    DB_DATABASE=homestead


    DB_USERNAME=homestead


    DB_PASSWORD=secret

    to 

    DB_DATABASE=mcomp


    DB_USERNAME=root


    DB_PASSWORD=root

7) Run the following command in terminal "php artisan migrate"
8) Import the sentiment analysis csv files into the database. The CSV files can be found in folder CSV Files
at the root of this repo. Inside this folder navigate into "company results CSV". Now import each of the 
csv files into the correct table in the database, amazon_sentiment imports into the table amazon_data do the same for
google_sentiment and microsoft_sentiment, they import into google_data and microsoft_data. The textblob csv files import
into the matching name in the database e.g. amazon_textblob.csv gets imported into amazon_textblob table.

9) In the same area that the CSV files for the company sentiment analysis is found, a csv called
"company_info.csv" is found. This file is imported into the table called "company_info" which is located in the
database.
10) From here the application is ready to run, in the terminal window run the command "php artisan serve"
. This will start the local server on port 8000
11) Open a browser window and navigate to localhost:8000
    