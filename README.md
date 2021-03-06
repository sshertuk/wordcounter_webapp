# WORD COUNTER - Web Application

Demo application to count the number of word entered in a form textbox.

## Getting Started

The web application (hosted on AWS EC2 Ubuntu dev server) can be accessed at: http://18.217.110.13:8000/

Addtionally, following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following plugins/dependecies have been used for development. Please ensure you have atleast these versions installed.

```
Python 3, Django 1.11, Bootsrap 4, Font-Awesome 5.0.8
```

### Installing
1. Clone the repository in the desired directory and run the following commands to create required migration files
```
git clone https://github.com/sshertuk/wordcounter_webapp.git
python manage.py makemigrations
```
2. Apply created migration files to the database by running
```
python manage.py migrate
```
3. Run application on localhost
```
python manage.py runserver
```
4.
```
Open the browser and visit: http://localhost:8000 (as per your default port config)
```

### Directions to Use
1. Ensure the application is running in the browser
2. Use the text box to enter the text-content
3. Click on count button to count the number of words in the entered text-content

### Assumpotions
1. Strings which contain atleast one valid (alphanumeric) character is considered a word
2. Thus, the number of words have been calculated based on characters comprising each word
3. Regex patterns used
4. Major Trade-off : Used regex for custom consideration to choose accuracy over performance as regex are expensive