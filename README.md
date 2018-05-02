# WORD COUNTER - Web Application

Demo application to count the number of word entered in a form textbox.

## Getting Started

The web application (hosted on AWS EC2 Ubuntu dev server) can be accessed at: 

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

### Directions to Use
1. Ensure the application is running in the browser
2. Use the text box to enter the text-content
3. Click on count button to count the number of words in the entered text-content

