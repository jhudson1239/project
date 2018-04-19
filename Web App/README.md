# mcomp_project
Repo for my mcomp project

To get the application up and running follow these steps:

1) Clone the repo
2) Navigate to the root of the cloned folder in a terminal window
3) Run "composer install"
4) Within the root folder the file called ".env.example" rename it to ".env."
5) In the terminal window run the command "php artisan key:generate"
5) Create a local database called mcomp
6) Connect the new .env file to the local database by changing the following lines of code within the .env file

    DB_DATABASE=homestead
    DB_USERNAME=homestead
    DB_PASSWORD=secret

    to 

    DB_DATABASE=mcomp
    DB_USERNAME=root
    DB_PASSWORD=root

Then run php artisan migrate?
    